from .model import Model
import numpy as np

svmParamGridRBF = {
        'kernel' : ['rbf'],
        'gamma' : [1e-1, 1e-2, 1e-3, 1e-4, 1e-5],
        'C' : [1, 5, 10]
    }
svmParamGridPoly = {
        'kernel' : ['poly'],
        'degree' : [2, 3],
        'gamma' : [1e-1, 1e-2, 1e-3],
        'coef0' : [0, 1, 2, 3, 4],
        'C' : [1, 5, 10]
    }
svmParamGridLinear = {
        'kernel' : ['linear'],
        'C' : [1, 5, 10, 15]
    }
rfParamGrid = {
        'n_estimators': [200, 400, 600, 800, 1000],
        'max_depth': [None],
        'max_features': [0.25, 0.5, 0.75, None]
    }
gnbParamGrid = {
        'var_smoothing' : [4, 2, 1, 5e-1, 1e-1, 5e-2, 1e-2, 5e-3, 1e-3, 5e-4, 1e-4, 0]
    }
knnParamGrid = {
        'metric' : ['minkowski', 'cosine'],
        'n_neighbors' : [5, 7, 9]
    }
mlpParamGrid = {
        'activation' : ['relu'],
        'learning_rate_init' : [0.1, 0.01, 0.001, 0.0001],
        'hidden_layer_sizes' : 
            []
            + [(25,), (50,), (75,), (100,), (125,), (150,), (175,), (200,), (225,), (250,), (275,), (300,)]
            + [(25,5), (50,10), (75,15), (100,20), (125,25), (150,30), (175,35), (200,40), (225,45), (250, 50), (275,55), (300, 60)]
            + [(25,12), (50,25), (75,37), (100,50), (125,62), (150,75), (175,87), (200,100), (225,112), (250,125), (275,137), (300,150)]
            + [(25,25), (50,50), (75,75), (100,100), (125,125), (150,150), (175,175), (200,200), (225,225), (250,250), (275,275), (300,300)]
    }


def gen_thresholds(start, stop, step):
    t = start
    thresholds = []
    while t<=stop:
        thresholds.append(t)
        t = t + step
    return thresholds


def grid_search_SVM_RBF(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('Kernel', 'C', 'gamma', 'Min_Dec_Score', 'Max_Dec_Score', 'Threshold', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('SVM', X, y, k)
    for c in svmParamGridRBF['C']:
        for g in svmParamGridRBF['gamma']:
            param = {'kernel' : 'rbf', 'C' : c, 'gamma' : g}
            model.learn(param, scale)
            min_des, max_des = model.get_decision_scores_k_fold(scale)
            thresholds = gen_thresholds(round(min_des, 1), round(max_des, 1), 0.1)
            
            acc = []
            sens = []
            spec = []
            f1s = []
            mcc = []
            ba = []
            for t in thresholds:
                result = model.predict_k_fold(scale=scale, threshold=t)
                acc.append(result[0])
                sens.append(result[1])
                spec.append(result[2])
                f1s.append(result[3])
                mcc.append(result[4])
                ba.append(result[5])
                #print(k, c, g, t, result[0], result[1], result[2], result[3], result[4], result[5])
            #diff = np.absolute(np.array(sens)-np.array(spec))
            #min_index = diff.tolist().index(diff.min())
            min_index = mcc.index(max(mcc))
            print('RBF', c, g, round(min_des, 1), round(max_des, 1), round(thresholds[min_index], 5), round(acc[min_index], 3), round(sens[min_index], 3), round(spec[min_index], 3), round(f1s[min_index], 3), round(mcc[min_index], 3), round(ba[min_index], 3))
            
            if do_blind == True:
                acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_SVM_RBF_wo_threshold(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('Kernel', 'C', 'gamma', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('SVM', X, y, k)
    for c in svmParamGridRBF['C']:
        for g in svmParamGridRBF['gamma']:
            param = {'kernel' : 'rbf', 'C' : c, 'gamma' : g}
            model.learn(param, scale)
            #min_des, max_des = model.get_decision_scores_k_fold(scale)
            #print('RBF', c, g, round(min_des, 3), round(max_des, 3))
            acc, sens, spec, f1s, mcc, ba = model.predict_k_fold(scale)
            print('RBF', c, g, round(acc, 3), round(sens, 3), round(spec, 3), round(f1s, 3), round(mcc, 3), round(ba, 3))
            
            if do_blind == True:
                acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale)
                acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale)
                print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_SVM_poly(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('Kernel', 'C', 'degree', 'gamma', 'coef0', 'Min_Dec_Score', 'Max_Dec_Score', 'Threshold', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('SVM', X, y, k)
    for c in svmParamGridPoly['C']:
        for deg in svmParamGridPoly['degree']:
            for g in svmParamGridPoly['gamma']:
                for coeff in svmParamGridPoly['coef0']:
                    param = {'kernel': 'poly', 'C': c, 'degree': deg, 'gamma': g, 'coef0': coeff}
                    model.learn(param, scale)
                    min_des, max_des = model.get_decision_scores_k_fold(scale)
                    thresholds = gen_thresholds(round(min_des, 1), round(max_des, 1), 0.1)
                    
                    acc = []
                    sens = []
                    spec = []
                    f1s = []
                    mcc = []
                    ba = []
                    for t in thresholds:
                        result = model.predict_k_fold(scale=scale, threshold=t)
                        acc.append(result[0])
                        sens.append(result[1])
                        spec.append(result[2])
                        f1s.append(result[3])
                        mcc.append(result[4])
                        ba.append(result[5])
                        #print(k, c, g, t, result[0], result[1], result[2], result[3], result[4], result[5])
                    #diff = np.absolute(np.array(sens)-np.array(spec))
                    #min_index = diff.tolist().index(diff.min())
                    min_index = mcc.index(max(mcc))
                    
                    print('poly', c, deg, g, coeff, round(min_des, 1), round(max_des, 1), round(thresholds[min_index], 5), round(acc[min_index], 3), round(sens[min_index], 3), round(spec[min_index], 3), round(f1s[min_index], 3), round(mcc[min_index], 3), round(ba[min_index], 3))
                    
                    if do_blind == True:
                        acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                        acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                        print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_SVM_poly_wo_threshold(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('Kernel', 'C', 'degree', 'gamma', 'coef0', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('SVM', X, y, k)
    for c in svmParamGridPoly['C']:
        for deg in svmParamGridPoly['degree']:
            for g in svmParamGridPoly['gamma']:
                for coeff in svmParamGridPoly['coef0']:
                    param = {'kernel': 'poly', 'C': c, 'degree': deg, 'gamma': g, 'coef0': coeff}
                    model.learn(param, scale)
                    acc, sens, spec, f1s, mcc, ba = model.predict_k_fold(scale)
                    print('poly', c, deg, g, coeff, round(acc, 3), round(sens, 3), round(spec, 3), round(f1s, 3), round(mcc, 3), round(ba, 3))
                    
                    if do_blind == True:
                        acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale)
                        acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale)
                        print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_SVM_linear(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('Kernel', 'C', 'Min_Dec_Score', 'Max_Dec_Score', 'Threshold', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('SVM', X, y, k)
    for c in svmParamGridLinear['C']:
        param = {'kernel': 'linear', 'C': c}
        model.learn(param, scale)
        min_des, max_des = model.get_decision_scores_k_fold(scale)
        thresholds = gen_thresholds(round(min_des, 1), round(max_des, 1), 0.1)
        
        acc = []
        sens = []
        spec = []
        f1s = []
        mcc = []
        ba = []
        for t in thresholds:
            result = model.predict_k_fold(scale=scale, threshold=t)
            acc.append(result[0])
            sens.append(result[1])
            spec.append(result[2])
            f1s.append(result[3])
            mcc.append(result[4])
            ba.append(result[5])
            #print(k, c, g, t, result[0], result[1], result[2], result[3], result[4], result[5])
        #diff = np.absolute(np.array(sens)-np.array(spec))
        #min_index = diff.tolist().index(diff.min())
        min_index = mcc.index(max(mcc))
        
        print('linear', c, round(min_des, 1), round(max_des, 1), round(thresholds[min_index], 5), round(acc[min_index], 3), round(sens[min_index], 3), round(spec[min_index], 3), round(f1s[min_index], 3), round(mcc[min_index], 3), round(ba[min_index], 3))
        
        if do_blind == True:
            acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
            acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
            print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_SVM_linear_wo_threshold(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('Kernel', 'C', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('SVM', X, y, k)
    for c in svmParamGridLinear['C']:
        param = {'kernel' : 'linear', 'C' : c}
        model.learn(param, scale)
        acc, sens, spec, f1s, mcc, ba = model.predict_k_fold(scale)
        print('linear', c, round(acc, 3), round(sens, 3), round(spec, 3), round(f1s, 3), round(mcc, 3), round(ba, 3))
        
        if do_blind == True:
            acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale)
            acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale)
            print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_RF(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('n_estimators', 'max_depth', 'max_features', 'Min_Dec_Score', 'Max_Dec_Score', 'Threshold', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('RF', X, y, k)
    for ne in rfParamGrid['n_estimators']:
        for md in rfParamGrid['max_depth']:
            for mf in rfParamGrid['max_features']:
                param = {'n_estimators': ne, 'max_depth': md, 'max_features': mf}
                model.learn(param, scale)
                #min_des, max_des = model.get_decision_scores_k_fold(scale)
                min_des, max_des = 0, 1.0001
                thresholds = gen_thresholds(round(min_des, 1), round(max_des, 1), 0.1)
                
                acc = []
                sens = []
                spec = []
                f1s = []
                mcc = []
                ba = []
                for t in thresholds:
                    result = model.predict_k_fold(scale=scale, threshold=t)
                    acc.append(result[0])
                    sens.append(result[1])
                    spec.append(result[2])
                    f1s.append(result[3])
                    mcc.append(result[4])
                    ba.append(result[5])
                    #print(k, c, g, t, result[0], result[1], result[2], result[3], result[4], result[5])
                #diff = np.absolute(np.array(sens)-np.array(spec))
                #min_index = diff.tolist().index(diff.min())
                min_index = mcc.index(max(mcc))
                
                print(ne, md, mf, round(min_des, 1), round(max_des, 1), round(thresholds[min_index], 5), round(acc[min_index], 3), round(sens[min_index], 3), round(spec[min_index], 3), round(f1s[min_index], 3), round(mcc[min_index], 3), round(ba[min_index], 3))
                
                if do_blind == True:
                    acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                    acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                    print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_RF_wo_threshold(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('n_estimators', 'max_depth', 'max_features', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('RF', X, y, k)
    for ne in rfParamGrid['n_estimators']:
        for md in rfParamGrid['max_depth']:
            for mf in rfParamGrid['max_features']:
                param = {'n_estimators': ne, 'max_depth': md, 'max_features': mf}
                model.learn(param, scale)
                acc, sens, spec, f1s, mcc, ba = model.predict_k_fold(scale)
                print(ne, md, mf, round(acc, 3), round(sens, 3), round(spec, 3), round(f1s, 3), round(mcc, 3), round(ba, 3))
                
                if do_blind == True:
                    acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale)
                    acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale)
                    print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_GNB(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    import warnings
    warnings.filterwarnings('ignore', category=RuntimeWarning)
    print('smoothing', 'Min_Dec_Score', 'Max_Dec_Score', 'Threshold', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('GNB', X, y, k)
    for s in gnbParamGrid['var_smoothing']:
        param = {'var_smoothing': s}
        model.learn(param, scale)
        #min_des, max_des = model.get_decision_scores_k_fold(scale)
        min_des, max_des = 0, 1.0001
        thresholds = gen_thresholds(round(min_des, 1), round(max_des, 1), 0.1)
        
        acc = []
        sens = []
        spec = []
        f1s = []
        mcc = []
        ba = []
        for t in thresholds:
            result = model.predict_k_fold(scale=scale, threshold=t)
            acc.append(result[0])
            sens.append(result[1])
            spec.append(result[2])
            f1s.append(result[3])
            mcc.append(result[4])
            ba.append(result[5])
            #print(k, c, g, t, result[0], result[1], result[2], result[3], result[4], result[5])
        #diff = np.absolute(np.array(sens)-np.array(spec))
        #min_index = diff.tolist().index(diff.min())
        min_index = mcc.index(max(mcc))
        
        print(s, round(min_des, 1), round(max_des, 1), round(thresholds[min_index], 5), round(acc[min_index], 3), round(sens[min_index], 3), round(spec[min_index], 3), round(f1s[min_index], 3), round(mcc[min_index], 3), round(ba[min_index], 3))
        
        if do_blind == True:
            acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
            acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
            print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))
    warnings.filterwarnings('default', category=RuntimeWarning)


def grid_search_GNB_wo_threshold(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    import warnings
    warnings.filterwarnings('ignore', category=RuntimeWarning)
    print('smoothing', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('GNB', X, y, k)
    for s in gnbParamGrid['var_smoothing']:
        param = {'var_smoothing' : s}
        model.learn(param, scale)
        acc, sens, spec, f1s, mcc, ba = model.predict_k_fold(scale)
        print(s, round(acc, 3), round(sens, 3), round(spec, 3), round(f1s, 3), round(mcc, 3), round(ba, 3))
        
        if do_blind == True:
            acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale)
            acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale)
            print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))
    warnings.filterwarnings('default', category=RuntimeWarning)


def grid_search_MLP(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('activation', 'layers', 'learning_rate', 'Min_Dec_Score', 'Max_Dec_Score', 'Threshold', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('MLP', X, y, k)
    for a in mlpParamGrid['activation']:
        for hls in mlpParamGrid['hidden_layer_sizes']:
            for lr in mlpParamGrid['learning_rate_init']:
                param = {'activation': a, 'hidden_layer_sizes': hls, 'learning_rate_init': lr}
                model.learn(param, scale)
                #min_des, max_des = model.get_decision_scores_k_fold(scale)
                min_des, max_des = 0, 1.0001
                thresholds = gen_thresholds(round(min_des, 1), round(max_des, 1), 0.1)
                
                acc = []
                sens = []
                spec = []
                f1s = []
                mcc = []
                ba = []
                for t in thresholds:
                    result = model.predict_k_fold(scale=scale, threshold=t)
                    acc.append(result[0])
                    sens.append(result[1])
                    spec.append(result[2])
                    f1s.append(result[3])
                    mcc.append(result[4])
                    ba.append(result[5])
                    #print(k, c, g, t, result[0], result[1], result[2], result[3], result[4], result[5])
                #diff = np.absolute(np.array(sens)-np.array(spec))
                #min_index = diff.tolist().index(diff.min())
                min_index = mcc.index(max(mcc))
                
                print(a, hls, lr, round(min_des, 1), round(max_des, 1), round(thresholds[min_index], 5), round(acc[min_index], 3), round(sens[min_index], 3), round(spec[min_index], 3), round(f1s[min_index], 3), round(mcc[min_index], 3), round(ba[min_index], 3))
                
                if do_blind == True:
                    acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                    acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                    print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_MLP_wo_threshold(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('activation', 'layers', 'learning_rate', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('MLP', X, y, k)
    for a in mlpParamGrid['activation']:
        for hls in mlpParamGrid['hidden_layer_sizes']:
            for lr in mlpParamGrid['learning_rate_init']:
                param = {'activation': a, 'hidden_layer_sizes': hls, 'learning_rate_init': lr}
                model.learn(param, scale)
                acc, sens, spec, f1s, mcc, ba = model.predict_k_fold(scale)
                print(a, hls, lr, round(acc, 3), round(sens, 3), round(spec, 3), round(f1s, 3), round(mcc, 3), round(ba, 3))
                
                if do_blind == True:
                    acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale)
                    acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale)
                    print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_KNN(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('metric', 'n_neighbors', 'Min_Dec_Score', 'Max_Dec_Score', 'Threshold', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('KNN', X, y, k)
    for m in knnParamGrid['metric']:
        for k in knnParamGrid['n_neighbors']:
            param = {'metric': m, 'n_neighbors': k}
            model.learn(param, scale)
            #min_des, max_des = model.get_decision_scores_k_fold(scale)
            min_des, max_des = 0, 1.0001
            thresholds = gen_thresholds(round(min_des, 1), round(max_des, 1), 0.1)
            
            acc = []
            sens = []
            spec = []
            f1s = []
            mcc = []
            ba = []
            for t in thresholds:
                result = model.predict_k_fold(scale=scale, threshold=t)
                acc.append(result[0])
                sens.append(result[1])
                spec.append(result[2])
                f1s.append(result[3])
                mcc.append(result[4])
                ba.append(result[5])
                #print(k, c, g, t, result[0], result[1], result[2], result[3], result[4], result[5])
            #diff = np.absolute(np.array(sens)-np.array(spec))
            #min_index = diff.tolist().index(diff.min())
            min_index = mcc.index(max(mcc))
            
            print(m, k, round(min_des, 1), round(max_des, 1), round(thresholds[min_index], 5), round(acc[min_index], 3), round(sens[min_index], 3), round(spec[min_index], 3), round(f1s[min_index], 3), round(mcc[min_index], 3), round(ba[min_index], 3))
            
            if do_blind == True:
                acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale, threshold=thresholds[min_index])
                print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


def grid_search_KNN_wo_threshold(X, y, k=5, scale=True, blind_X=None, blind_y=None, do_blind=False):
    print('metric', 'n_neighbors', 'Accuracy', 'Sensitivity', 'Specificity', 'F1-score', 'MCC', 'BA')
    model = Model('KNN', X, y, k)
    for m in knnParamGrid['metric']:
        for k in knnParamGrid['n_neighbors']:
            param = {'metric': m, 'n_neighbors': k}
            model.learn(param, scale)
            acc, sens, spec, f1s, mcc, ba = model.predict_k_fold(scale)
            print(m, k, round(acc, 3), round(sens, 3), round(spec, 3), round(f1s, 3), round(mcc, 3), round(ba, 3))
            
            if do_blind == True:
                acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_X, blind_y, scale=scale)
                acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_X, blind_y, scale=scale)
                print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))


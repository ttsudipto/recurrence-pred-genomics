from .resource import get_ip_data_file_name, get_ip_target_file_name, read_data, print_data_summary
from .data_preprocessing import get_top_features, split_blind_data, perform_oversampling
from .optimal_gs_params import get_optimal_params, get_optimal_no_of_features
from .model import Model
from sklearn.metrics import roc_curve, auc, precision_recall_curve
import numpy as np
from numpy import interp


def read_input(dataset, os, fs, n_features):
    selected_features = get_top_features(dataset, n_features, fs, verbose=False)
    res = read_data(get_ip_data_file_name(dataset), get_ip_target_file_name(dataset), 'Recurrence', verbose=False, fs=selected_features)
    cv_res, blind_res = split_blind_data(res, test_size=0.2, modify_pids=False)
    if os == 'smote':
        cv_res = perform_oversampling(cv_res)
    return cv_res, blind_res


def create_model(dataset, os, fs, model_id, do_learn=True):
    n_features = get_optimal_no_of_features(dataset, os, fs, model_id)
    cv_res, blind_res = read_input(dataset, os, fs, n_features)
    model = Model(model_id, cv_res.data, cv_res.target)
    if do_learn == True:
        params = get_optimal_params(dataset, os, fs, model_id)
        model.learn(params)
        print(dataset, os, fs, model_id, n_features, params) 
        #print('\t', model.predict_k_fold())
    return model


def plot_roc(model, verbose=False):
    tprs = []
    aucs = []
    mean_fpr = np.linspace(0, 1, 100)

    for i in range(len(model.estimators)):
        X_test = model.dataScaler.transform(model.data[model.test_indices[i]])
        y_test = model.target[model.test_indices[i]]
        #probas = model.get_decision_score(model.estimators[i], X_test)
        if model.estimator_id == 'SVM':
            probas = model.estimators[i].decision_function(X_test)
            fpr, tpr, thresholds = roc_curve(y_test, probas)
        elif model.estimator_id == 'MLP':
            probas = model.estimators[i].predict_proba(X_test)
            fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
        elif model.estimator_id == 'RF':
            probas = model.estimators[i].predict_proba(X_test)
            fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
        else :
            raise ValueError('Invalid estimator ID')
        tprs.append(interp(mean_fpr, fpr, tpr))
        tprs[-1][0] = 0.0
        roc_auc = auc(fpr, tpr)
        aucs.append(roc_auc)
        #print('AUC(CV ' + str(i) + ') = ' + str(roc_auc))

    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    std_auc = np.std(aucs)
    
    if verbose == True :
        print('\tMean AUC = ' + str(mean_auc) + ' (+/- ' + str(std_auc) + ')')
    
    #------ Print as CSV ------#
    #heading = ['FPR']
    #for i in range(len(model.estimators)) :
        #heading.append('TPR' + str(i) + ' AUC = ' + str(round(aucs[i], 4)))
    #heading.append('Mean TPR' + ' AUC = ' + str(round(mean_auc, 4)) + ' (+/- ' + str(round(std_auc, 4)) + ')')
    #print(', '.join(heading))
    #for i in range(100) :
        #row = [mean_fpr[i]]
        #for j in range(len(model.estimators)) :
            #row.append(tprs[j][i])
        #row.append(mean_tpr[i])
        #print(','.join(map(str,row)))
    #------ Print as CSV ------#
    
    return mean_fpr, mean_tpr, mean_auc, std_auc


def plot_blind_roc(model, b_res, verbose=False):
    X_test = model.dataScaler.transform(b_res.data)
    y_test = b_res.target
    #probas = model.get_decision_score(model.estimators[i], X_test)
    if model.estimator_id == 'SVM':
        probas = model.total_estimator.decision_function(X_test)
        fpr, tpr, thresholds = roc_curve(y_test, probas)
    elif model.estimator_id == 'MLP':
        probas = model.total_estimator.predict_proba(X_test)
        fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
    elif model.estimator_id == 'RF':
        probas = model.total_estimator.predict_proba(X_test)
        fpr, tpr, thresholds = roc_curve(y_test, probas[:, 1])
    else :
        raise ValueError('Invalid estimator ID')
    roc_auc = auc(fpr, tpr)
    if verbose:
        print(roc_auc)
    return roc_auc

#n_features = get_optimal_no_of_features('dataset1', 'original', 'MCFS', 'RF')
#cv_res, blind_res = read_input('dataset1', 'original', 'MCFS', n_features)
#plot_blind_roc(create_model('dataset1', 'original', 'MCFS', 'RF'), blind_res, verbose=True) # Optimal RF
#n_features = get_optimal_no_of_features('dataset1', 'original', 'MCFS', 'MLP')
#cv_res, blind_res = read_input('dataset1', 'original', 'MCFS', n_features)
#plot_blind_roc(create_model('dataset1', 'original', 'MCFS', 'MLP'), blind_res, verbose=True) # Optimal MLP
#n_features = get_optimal_no_of_features('dataset1', 'original', 'MCFS', 'SVM')
#cv_res, blind_res = read_input('dataset1', 'original', 'MCFS', n_features)
#plot_blind_roc(create_model('dataset1', 'original', 'MCFS', 'SVM'), blind_res, verbose=True) # Optimal SVM
#n_features = get_optimal_no_of_features('dataset1', 'original', 'Boruta', 'RF')
#cv_res, blind_res = read_input('dataset1', 'original', 'Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'original', 'Boruta', 'RF'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'original', 'Boruta', 'MLP')
#cv_res, blind_res = read_input('dataset1', 'original', 'Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'original', 'Boruta', 'MLP'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'original', 'Boruta', 'SVM')
#cv_res, blind_res = read_input('dataset1', 'original', 'Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'original', 'Boruta', 'SVM'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'original', 'Combined_MCFS_Boruta', 'RF')
#cv_res, blind_res = read_input('dataset1', 'original', 'Combined_MCFS_Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'RF'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'original', 'Combined_MCFS_Boruta', 'MLP')
#cv_res, blind_res = read_input('dataset1', 'original', 'Combined_MCFS_Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'MLP'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'original', 'Combined_MCFS_Boruta', 'SVM')
#cv_res, blind_res = read_input('dataset1', 'original', 'Combined_MCFS_Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'SVM'), blind_res, verbose=True)

#n_features = get_optimal_no_of_features('dataset1', 'smote', 'MCFS', 'RF')
#cv_res, blind_res = read_input('dataset1', 'smote', 'MCFS', n_features)
#plot_blind_roc(create_model('dataset1', 'smote', 'MCFS', 'RF'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'smote', 'MCFS', 'MLP')
#cv_res, blind_res = read_input('dataset1', 'smote', 'MCFS', n_features)
#plot_blind_roc(create_model('dataset1', 'smote', 'MCFS', 'MLP'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'smote', 'MCFS', 'SVM')
#cv_res, blind_res = read_input('dataset1', 'smote', 'MCFS', n_features)
#plot_blind_roc(create_model('dataset1', 'smote', 'MCFS', 'SVM'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'smote', 'Boruta', 'RF')
#cv_res, blind_res = read_input('dataset1', 'smote', 'Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'smote', 'Boruta', 'RF'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'smote', 'Boruta', 'MLP')
#cv_res, blind_res = read_input('dataset1', 'smote', 'Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'smote', 'Boruta', 'MLP'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'smote', 'Boruta', 'SVM')
#cv_res, blind_res = read_input('dataset1', 'smote', 'Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'smote', 'Boruta', 'SVM'), blind_res, verbose=True)
#n_features = get_optimal_no_of_features('dataset1', 'smote', 'Combined_MCFS_Boruta', 'RF')
#cv_res, blind_res = read_input('dataset1', 'smote', 'Combined_MCFS_Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'RF'), blind_res, verbose=True) # Optimal RF
#n_features = get_optimal_no_of_features('dataset1', 'smote', 'Combined_MCFS_Boruta', 'MLP')
#cv_res, blind_res = read_input('dataset1', 'smote', 'Combined_MCFS_Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'MLP'), blind_res, verbose=True) # Optimal MLP
#n_features = get_optimal_no_of_features('dataset1', 'smote', 'Combined_MCFS_Boruta', 'SVM')
#cv_res, blind_res = read_input('dataset1', 'smote', 'Combined_MCFS_Boruta', n_features)
#plot_blind_roc(create_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'SVM'), blind_res, verbose=True) # Optimal SVM


############# Dataset 1 #############
#plot_roc(create_model('dataset1', 'original', 'MCFS', 'SVM'), verbose=True) # Optimal SVM
#plot_roc(create_model('dataset1', 'original', 'MCFS', 'MLP'), verbose=True) # Optimal MLP
#plot_roc(create_model('dataset1', 'original', 'MCFS', 'RF'), verbose=True) # Optimal RF
#plot_roc(create_model('dataset1', 'original', 'Boruta', 'SVM'), verbose=True)
#plot_roc(create_model('dataset1', 'original', 'Boruta', 'MLP'), verbose=True)
#plot_roc(create_model('dataset1', 'original', 'Boruta', 'RF'), verbose=True)
#plot_roc(create_model('dataset1', 'original', 'ANOVA', 'SVM'), verbose=True)
#plot_roc(create_model('dataset1', 'original', 'ANOVA', 'MLP'), verbose=True)
#plot_roc(create_model('dataset1', 'original', 'ANOVA', 'RF'), verbose=True)
#plot_roc(create_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'SVM'), verbose=True)
#plot_roc(create_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'MLP'), verbose=True)
#plot_roc(create_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'RF'), verbose=True)

#plot_roc(create_model('dataset1', 'smote', 'MCFS', 'SVM'), verbose=True)
#plot_roc(create_model('dataset1', 'smote', 'MCFS', 'MLP'), verbose=True)
#plot_roc(create_model('dataset1', 'smote', 'MCFS', 'RF'), verbose=True)
#plot_roc(create_model('dataset1', 'smote', 'Boruta', 'SVM'), verbose=True)
#plot_roc(create_model('dataset1', 'smote', 'Boruta', 'MLP'), verbose=True)
#plot_roc(create_model('dataset1', 'smote', 'Boruta', 'RF'), verbose=True)
#plot_roc(create_model('dataset1', 'smote', 'ANOVA', 'SVM'), verbose=True)
#plot_roc(create_model('dataset1', 'smote', 'ANOVA', 'MLP'), verbose=True)
#plot_roc(create_model('dataset1', 'smote', 'ANOVA', 'RF'), verbose=True)
#plot_roc(create_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'SVM'), verbose=True) # Optimal SVM
#plot_roc(create_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'MLP'), verbose=True) # Optimal MLP
#plot_roc(create_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'RF'), verbose=True) # Optimal RF


############# Dataset 2 #############
#plot_roc(create_model('dataset2', 'original', 'MCFS', 'SVM'), verbose=True)
#plot_roc(create_model('dataset2', 'original', 'MCFS', 'MLP'), verbose=True)
#plot_roc(create_model('dataset2', 'original', 'MCFS', 'RF'), verbose=True)
#plot_roc(create_model('dataset2', 'original', 'Boruta', 'SVM'), verbose=True) # Optimal SVM
#plot_roc(create_model('dataset2', 'original', 'Boruta', 'MLP'), verbose=True)
#plot_roc(create_model('dataset2', 'original', 'Boruta', 'RF'), verbose=True)
#plot_roc(create_model('dataset2', 'original', 'ANOVA', 'SVM'), verbose=True)
#plot_roc(create_model('dataset2', 'original', 'ANOVA', 'MLP'), verbose=True)
#plot_roc(create_model('dataset2', 'original', 'ANOVA', 'RF'), verbose=True)
#plot_roc(create_model('dataset2', 'original', 'Combined_MCFS_Boruta', 'SVM'), verbose=True)
#plot_roc(create_model('dataset2', 'original', 'Combined_MCFS_Boruta', 'MLP'), verbose=True) # Optimal MLP
#plot_roc(create_model('dataset2', 'original', 'Combined_MCFS_Boruta', 'RF'), verbose=True) # Optimal RF

#plot_roc(create_model('dataset2', 'smote', 'MCFS', 'SVM'), verbose=True)
#plot_roc(create_model('dataset2', 'smote', 'MCFS', 'MLP'), verbose=True) # Optimal MLP
#plot_roc(create_model('dataset2', 'smote', 'MCFS', 'RF'), verbose=True)
#plot_roc(create_model('dataset2', 'smote', 'Boruta', 'SVM'), verbose=True)
#plot_roc(create_model('dataset2', 'smote', 'Boruta', 'MLP'), verbose=True)
#plot_roc(create_model('dataset2', 'smote', 'Boruta', 'RF'), verbose=True)
#plot_roc(create_model('dataset2', 'smote', 'ANOVA', 'SVM'), verbose=True)
#plot_roc(create_model('dataset2', 'smote', 'ANOVA', 'MLP'), verbose=True)
#plot_roc(create_model('dataset2', 'smote', 'ANOVA', 'RF'), verbose=True)
#plot_roc(create_model('dataset2', 'smote', 'Combined_MCFS_Boruta', 'SVM'), verbose=True) # Optimal SVM
#plot_roc(create_model('dataset2', 'smote', 'Combined_MCFS_Boruta', 'MLP'), verbose=True)
#plot_roc(create_model('dataset2', 'smote', 'Combined_MCFS_Boruta', 'RF'), verbose=True) # Optimal RF


############# Dataset 3 #############
#plot_roc(create_model('dataset3', 'original', 'MCFS', 'SVM'), verbose=True) # Optimal SVM
#plot_roc(create_model('dataset3', 'original', 'MCFS', 'MLP'), verbose=True) # Optimal MLP
#plot_roc(create_model('dataset3', 'original', 'MCFS', 'RF'), verbose=True) # Optimal RF
#plot_roc(create_model('dataset3', 'original', 'Boruta', 'SVM'), verbose=True)
#plot_roc(create_model('dataset3', 'original', 'Boruta', 'MLP'), verbose=True)
#plot_roc(create_model('dataset3', 'original', 'Boruta', 'RF'), verbose=True)
#plot_roc(create_model('dataset3', 'original', 'ANOVA', 'SVM'), verbose=True)
#plot_roc(create_model('dataset3', 'original', 'ANOVA', 'MLP'), verbose=True)
#plot_roc(create_model('dataset3', 'original', 'ANOVA', 'RF'), verbose=True)
#plot_roc(create_model('dataset3', 'original', 'Combined_MCFS_Boruta', 'SVM'), verbose=True)
#plot_roc(create_model('dataset3', 'original', 'Combined_MCFS_Boruta', 'MLP'), verbose=True)
#plot_roc(create_model('dataset3', 'original', 'Combined_MCFS_Boruta', 'RF'), verbose=True)

#plot_roc(create_model('dataset3', 'smote', 'MCFS', 'SVM'), verbose=True)
#plot_roc(create_model('dataset3', 'smote', 'MCFS', 'MLP'), verbose=True)
#plot_roc(create_model('dataset3', 'smote', 'MCFS', 'RF'), verbose=True)
#plot_roc(create_model('dataset3', 'smote', 'Boruta', 'SVM'), verbose=True)
#plot_roc(create_model('dataset3', 'smote', 'Boruta', 'MLP'), verbose=True)
#plot_roc(create_model('dataset3', 'smote', 'Boruta', 'RF'), verbose=True)
#plot_roc(create_model('dataset3', 'smote', 'ANOVA', 'SVM'), verbose=True)
#plot_roc(create_model('dataset3', 'smote', 'ANOVA', 'MLP'), verbose=True)
#plot_roc(create_model('dataset3', 'smote', 'ANOVA', 'RF'), verbose=True)
#plot_roc(create_model('dataset3', 'smote', 'Combined_MCFS_Boruta', 'SVM'), verbose=True) # Optimal SVM
#plot_roc(create_model('dataset3', 'smote', 'Combined_MCFS_Boruta', 'MLP'), verbose=True) # Optimal MLP
#plot_roc(create_model('dataset3', 'smote', 'Combined_MCFS_Boruta', 'RF'), verbose=True) # Optimal RF

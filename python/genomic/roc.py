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
    return model, cv_res, blind_res


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
    mean_fpr = np.linspace(0, 1, 100)
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
    mean_tpr = interp(mean_fpr, fpr, tpr)
    mean_tpr[-1] = 0.0
    mean_tpr[-1] = 1.0
    roc_auc = auc(mean_fpr, mean_tpr)

    #------ Print as CSV ------#
    #heading = ['FPR']
    #heading.append('Mean TPR' + ' AUC = ' + str(round(roc_auc, 4)))
    #print(', '.join(heading))
    #for i in range(100) :
        #row = [mean_fpr[i]]
        #row.append(mean_tpr[i])
        #print(','.join(map(str,row)))
    #------ Print as CSV ------#

    if verbose:
        print('\tBlind AUC = ' + str(roc_auc))
    return roc_auc


############# Dataset 1, Original, MCFS #############

# model, cv_res, blind_res = create_model('dataset1', 'original', 'MCFS', 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', 'MCFS', 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', 'MCFS', 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

############# Dataset 1, Original, Boruta #############

# model, cv_res, blind_res = create_model('dataset1', 'original', 'Boruta', 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', 'Boruta', 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', 'Boruta', 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

############# Dataset 1, Original, ANOVA #############

# model, cv_res, blind_res = create_model('dataset1', 'original', 'ANOVA', 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', 'ANOVA', 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', 'ANOVA', 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

############# Dataset 1, Original, Combined_MCFS_Boruta #############

# model, cv_res, blind_res = create_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

############# Dataset 1, Original, None #############

# model, cv_res, blind_res = create_model('dataset1', 'original', None, 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', None, 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'original', None, 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

############# Dataset 1, SMOTE, MCFS #############

# model, cv_res, blind_res = create_model('dataset1', 'smote', 'MCFS', 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', 'MCFS', 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', 'MCFS', 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

############# Dataset 1, SMOTE, Boruta #############

# model, cv_res, blind_res = create_model('dataset1', 'smote', 'Boruta', 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', 'Boruta', 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', 'Boruta', 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

############# Dataset 1, SMOTE, ANOVA #############

# model, cv_res, blind_res = create_model('dataset1', 'smote', 'ANOVA', 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', 'ANOVA', 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', 'ANOVA', 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

############# Dataset 1, SMOTE, Combined_MCFS_Boruta #############

# model, cv_res, blind_res = create_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

############# Dataset 1, SMOTE, None #############

# model, cv_res, blind_res = create_model('dataset1', 'smote', None, 'RF')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', None, 'MLP')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)
# model, cv_res, blind_res = create_model('dataset1', 'smote', None, 'SVM')
# plot_roc(model, verbose=True)
# plot_blind_roc(model, blind_res, verbose=True)

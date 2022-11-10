from .resource import get_ip_data_file_name, get_ip_target_file_name, read_data, print_data_summary
from .data_preprocessing import get_top_features, split_blind_data, perform_oversampling
from .optimal_gs_params import get_optimal_params, get_optimal_no_of_features, get_optimal_threshold
from .model import Model


def read_input(dataset, os, selected_features, do_split=True):
    res = read_data(get_ip_data_file_name(dataset), get_ip_target_file_name(dataset), 'Recurrence', verbose=False, fs=selected_features)
    #print(dataset, res.gene_names)
    if do_split == True:
        cv_res, blind_res = split_blind_data(res, test_size=0.2, modify_pids=False)
        if os == 'smote':
            cv_res = perform_oversampling(cv_res)
        return cv_res, blind_res
    if os == 'smote':
        res = perform_oversampling(res)
    return res


def cross_dataset_validate_model(train_dataset, os, fs, model_id, test_dataset):
    threshold = get_optimal_threshold(train_dataset, os, fs, model_id)
    n_features = get_optimal_no_of_features(train_dataset, os, fs, model_id)
    selected_features = get_top_features(train_dataset, n_features, fs, verbose=False)
    cv_res, blind_res = read_input(train_dataset, os, selected_features)
    model = Model(model_id, cv_res.data, cv_res.target)
    
    params = get_optimal_params(train_dataset, os, fs, model_id)
    model.learn(params)
    #print(train_dataset, os, fs, model_id, n_features, params) 
    #print(model.predict_k_fold(threshold=threshold))
    #acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_data(blind_res.data, blind_res.target, threshold=threshold)
    #acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_without_CV(blind_res.data, blind_res.target, threshold=threshold)
    #print('\t', round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3))
    
    val_res = read_input(test_dataset, 'original', selected_features, do_split=False)
    acc1, sens1, spec1, f1s1, mcc1, ba1 = model.predict_blind_without_CV(val_res.data, val_res.target)
    acc2, sens2, spec2, f1s2, mcc2, ba2 = model.predict_blind_data(val_res.data, val_res.target)
    print(train_dataset, os, model_id, fs, n_features, params, test_dataset, 
          round(acc1, 3), round(sens1, 3), round(spec1, 3), round(f1s1, 3), round(mcc1, 3), round(ba1, 3), 
          round(acc2, 3), round(sens2, 3), round(spec2, 3), round(f1s2, 3), round(mcc2, 3), round(ba2, 3)
    )
    
    return model


print('Train_dataset', 'Oversampling', 'ML', 'FS', 'Feature_size', 'Params', 'Test_dataset', 'Accuracy_bcv', 'Sensitivity_bcv', 'Specificity_bcv', 'F1-score_bcv', 'MCC_bcv', 'BA_bcv', 'Accuracy_blind', 'Sensitivity_blind', 'Specificity_blind', 'F1-score_blind', 'MCC_blind', 'BA_blind')
#cross_dataset_validate_model('dataset1', 'original', 'MCFS', 'RF', 'dataset2')
#cross_dataset_validate_model('dataset1', 'original', 'Boruta', 'RF', 'dataset2')
#cross_dataset_validate_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'RF', 'dataset2')
#cross_dataset_validate_model('dataset1', 'original', 'MCFS', 'MLP', 'dataset2')
#cross_dataset_validate_model('dataset1', 'original', 'Boruta', 'MLP', 'dataset2')
#cross_dataset_validate_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'MLP', 'dataset2')
#cross_dataset_validate_model('dataset1', 'original', 'MCFS', 'SVM', 'dataset2')
#cross_dataset_validate_model('dataset1', 'original', 'Boruta', 'SVM', 'dataset2')
#cross_dataset_validate_model('dataset1', 'original', 'Combined_MCFS_Boruta', 'SVM', 'dataset2')

#cross_dataset_validate_model('dataset1', 'smote', 'MCFS', 'RF', 'dataset2')
#cross_dataset_validate_model('dataset1', 'smote', 'Boruta', 'RF', 'dataset2')
#cross_dataset_validate_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'RF', 'dataset2')
#cross_dataset_validate_model('dataset1', 'smote', 'MCFS', 'MLP', 'dataset2')
#cross_dataset_validate_model('dataset1', 'smote', 'Boruta', 'MLP', 'dataset2')
#cross_dataset_validate_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'MLP', 'dataset2')
#cross_dataset_validate_model('dataset1', 'smote', 'MCFS', 'SVM', 'dataset2')
#cross_dataset_validate_model('dataset1', 'smote', 'Boruta', 'SVM', 'dataset2')
#cross_dataset_validate_model('dataset1', 'smote', 'Combined_MCFS_Boruta', 'SVM', 'dataset2')

#cross_dataset_validate_model('dataset2', 'original', 'MCFS', 'RF', 'dataset1')
#cross_dataset_validate_model('dataset2', 'original', 'Boruta', 'RF', 'dataset1')
#cross_dataset_validate_model('dataset2', 'original', 'Combined_MCFS_Boruta', 'RF', 'dataset1')
#cross_dataset_validate_model('dataset2', 'original', 'MCFS', 'MLP', 'dataset1')
#cross_dataset_validate_model('dataset2', 'original', 'Boruta', 'MLP', 'dataset1')
#cross_dataset_validate_model('dataset2', 'original', 'Combined_MCFS_Boruta', 'MLP', 'dataset1')
#cross_dataset_validate_model('dataset2', 'original', 'MCFS', 'SVM', 'dataset1')
#cross_dataset_validate_model('dataset2', 'original', 'Boruta', 'SVM', 'dataset1')
#cross_dataset_validate_model('dataset2', 'original', 'Combined_MCFS_Boruta', 'SVM', 'dataset1')

#cross_dataset_validate_model('dataset2', 'smote', 'MCFS', 'RF', 'dataset1')
#cross_dataset_validate_model('dataset2', 'smote', 'Boruta', 'RF', 'dataset1')
#cross_dataset_validate_model('dataset2', 'smote', 'Combined_MCFS_Boruta', 'RF', 'dataset1')
#cross_dataset_validate_model('dataset2', 'smote', 'MCFS', 'MLP', 'dataset1')
#cross_dataset_validate_model('dataset2', 'smote', 'Boruta', 'MLP', 'dataset1')
#cross_dataset_validate_model('dataset2', 'smote', 'Combined_MCFS_Boruta', 'MLP', 'dataset1')
#cross_dataset_validate_model('dataset2', 'smote', 'MCFS', 'SVM', 'dataset1')
#cross_dataset_validate_model('dataset2', 'smote', 'Boruta', 'SVM', 'dataset1')
#cross_dataset_validate_model('dataset2', 'smote', 'Combined_MCFS_Boruta', 'SVM', 'dataset1')

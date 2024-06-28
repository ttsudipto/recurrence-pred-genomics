from .resource import get_ip_data_file_name, get_ip_target_file_name, read_data, print_data_summary
from .data_preprocessing import get_top_features, split_blind_data, perform_oversampling
from .grid_search import grid_search_SVM_RBF, grid_search_SVM_RBF_wo_threshold
from .grid_search import grid_search_SVM_poly, grid_search_SVM_poly_wo_threshold
from .grid_search import grid_search_SVM_linear, grid_search_SVM_linear_wo_threshold
from .grid_search import grid_search_RF, grid_search_RF_wo_threshold
from .grid_search import grid_search_GNB, grid_search_GNB_wo_threshold
from .grid_search import grid_search_KNN, grid_search_KNN_wo_threshold
from .grid_search import grid_search_MLP, grid_search_MLP_wo_threshold
from sklearn.model_selection import train_test_split

#---- Select dataset ----#
dataset = 'dataset1'
#dataset = 'dataset2'
#dataset = 'dataset3'

#----Perform ANOVA ----#
#from .data_preprocessing import perform_ANOVA
#res = read_data(get_ip_data_file_name(dataset), get_ip_target_file_name(dataset), 'Recurrence', verbose=True)
#perform_ANOVA(res, verbose=True)

#---- Select features ----#
selected_features = None  # select all features
#n_features = 140
#selected_features = get_top_features(dataset, n_features, 'MCFS', verbose=True)
#selected_features = get_top_features(dataset, n_features, 'Boruta', verbose=True)
#selected_features = get_top_features(dataset, n_features, 'ANOVA', verbose=True)
#selected_features = get_top_features(dataset, n_features, 'SVM-t-RFE', verbose=True)
#selected_features = get_top_features(dataset, n_features, 'Combined_MCFS_Boruta', verbose=True)
#selected_features = get_top_features(dataset, n_features, 'Combined_MCFS_ANOVA', verbose=True)
#selected_features = get_top_features(dataset, n_features, 'Combined_Boruta_ANOVA', verbose=True)
#selected_features = get_top_features(dataset, n_features, 'Combined_all', verbose=True)
#print(selected_features)

#---- Read data ----#
res = read_data(get_ip_data_file_name(dataset), get_ip_target_file_name(dataset), 'Recurrence', verbose=True, fs=selected_features)
cv_res, blind_res = split_blind_data(res, test_size=0.2, modify_pids=True)
print(cv_res.data.shape, cv_res.target.shape)
print(blind_res.data.shape, blind_res.target.shape)
print_data_summary(cv_res)
print_data_summary(blind_res)

#---- Perform oversampling using SMOTE ----#
#os_cv_res = perform_oversampling(cv_res)
#print(os_cv_res.data.shape, os_cv_res.target.shape)
#os_blind_res = perform_oversampling(blind_res)
#print(os_blind_res.data.shape, os_blind_res.target.shape)

#---- Grid Search Original models ----#
#grid_search_SVM_RBF(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_RBF_wo_threshold(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_poly(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_poly_wo_threshold(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_linear(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_linear_wo_threshold(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_RF(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_RF_wo_threshold(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_GNB(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_GNB_wo_threshold(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_KNN(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_KNN_wo_threshold(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_MLP(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_MLP_wo_threshold(cv_res.data, cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)

#---- Grid Search SMOTE models ----#
#grid_search_SVM_RBF(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_RBF_wo_threshold(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_poly(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_poly_wo_threshold(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_linear(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_SVM_linear_wo_threshold(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_RF(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_RF_wo_threshold(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_GNB(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_GNB_wo_threshold(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_KNN(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_KNN_wo_threshold(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_MLP(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)
#grid_search_MLP_wo_threshold(os_cv_res.data, os_cv_res.target, blind_X=blind_res.data, blind_y=blind_res.target, do_blind=True)


# print('---------------------------------------------------------------')
# from .optimal_gs_params import get_optimal_no_of_features
# n_features = get_optimal_no_of_features('dataset1', 'smote', 'Boruta', 'SVM')
# n_features = get_optimal_no_of_features('dataset1', 'smote', 'Boruta', 'MLP')
# n_features = get_optimal_no_of_features('dataset1', 'smote', 'Combined_MCFS_Boruta', 'RF')
# selected_features = get_top_features(dataset, n_features, 'Boruta', verbose=False)
# res = read_data(get_ip_data_file_name(dataset), get_ip_target_file_name(dataset), 'Recurrence', fs=selected_features)
# print_data_summary(res)
# print('\t'.join(['PID', 'Recurrence'] + list(res.gene_names)))
# for i in range(res.data.shape[0]):
#     row = [str(x) for x in list(res.data[i])]
#     print('\t'.join([res.pids[i], str(res.target[i])] + row))


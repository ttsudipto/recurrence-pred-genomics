from .resource import DataResource
from sklearn.model_selection import train_test_split
from sklearn.feature_selection import f_classif
from imblearn.over_sampling import SMOTE
from csv import DictReader
from math import isnan

path_prefix = 'output/'

file_name = {'MCFS': 'FS/MCFS/features_MCFS_300ps_scaled.csv',
             'Boruta': 'FS/Boruta/features_boruta_1000p0.01.csv',
             'ANOVA': 'FS/ANOVA/features_ANOVA.csv',
             'SVM-t-RFE': 'FS/SVM-t-RFE/features_SVM-t-RFE.csv',
             'Combined_MCFS_Boruta': 'FS/Combined_MCFS_Boruta/features_combined_MCFS_Boruta.csv',
             'Combined_MCFS_ANOVA': 'FS/Combined_MCFS_ANOVA/features_combined_MCFS_ANOVA.csv',
             'Combined_Boruta_ANOVA': 'FS/Combined_Boruta_ANOVA/features_combined_Boruta_ANOVA.csv',
             'Combined_all': 'FS/Combined_all/features_combined_all.csv'
             }


def get_file_name_prefix(dataset):
    return path_prefix + dataset + '/'


def get_top_features(dataset, num_features, fs_algo, verbose=False):
    if fs_algo is None:
        return None
    f = open(get_file_name_prefix(dataset) + file_name[fs_algo], 'r')
    reader = DictReader(f, delimiter=',')
    indices = []
    gene_names = []
    k = 0
    
    for row in reader:
        if k < num_features:
            indices.append(int(row['Index']) - 1)
            gene_names.append(row['attribute'])
        k = k + 1
    f.close()
    
    if verbose == True:
        print(indices)
        print(gene_names)
    
    return indices


def get_top_feature_names(dataset, num_features, fs_algo, verbose=False):
    f = open(get_file_name_prefix(dataset) + file_name[fs_algo], 'r')
    reader = DictReader(f, delimiter=',')
    gene_names = []
    k = 0
    for row in reader:
        if k < num_features:
            gene_names.append(row['attribute'])
        k = k + 1
    f.close()
    
    if verbose == True:
        print(gene_names)
    
    return gene_names


def split_blind_data(res, test_size=0.2, modify_pids=False):
    XTrain, XTest, yTrain, yTest = train_test_split(res.data, res.target, test_size=test_size, random_state=42, stratify=res.target)
    cv_res = DataResource(res.genomic_file_name, res.label_file_name)
    cv_res.data = XTrain
    cv_res.target = yTrain
    cv_res.gene_names = res.gene_names
    blind_res = DataResource(res.genomic_file_name, res.label_file_name)
    blind_res.data = XTest
    blind_res.target = yTest
    blind_res.gene_names = res.gene_names
    if modify_pids == True:
        pidTrain, pidTest, yTrain, yTest = train_test_split(res.pids, res.target, test_size=test_size, random_state=42, stratify=res.target)
        cv_res.pids = list(pidTrain)
        blind_res.pids = list(pidTest)
    return cv_res, blind_res


def perform_oversampling(res, verbose=False):
    os_res_data, os_res_target = SMOTE(sampling_strategy='minority', random_state=42, n_jobs=-1).fit_resample(res.data, res.target)
    os_res = DataResource(res.genomic_file_name, res.label_file_name)
    os_res.data = os_res_data
    os_res.target = os_res_target
    os_res.gene_names = res.gene_names
    
    if verbose == True:
        print(res.target)
        print(os_res.data.shape, os_res.target.shape)
        print(os_res.target)
    
    return os_res


def perform_ANOVA(res, verbose=False):
    fval, pval = f_classif(res.data, res.target)
    
    results = []
    for i in range(res.data.shape[1]):
        if isnan(fval[i]):
            fval[i] = float('-inf')
        if isnan(pval[i]):
            pval[i] = float('-inf')
        results.append((i, fval[i], pval[i]))
    results = sorted(results, key=lambda x: x[1], reverse=True)
    
    if verbose == True:
        print("Index", "position", "attribute", "F_val", "p_val")
        for i in range(len(results)):
            print(results[i][0]+1, i+1, res.gene_names[results[i][0]], results[i][1], results[i][2])

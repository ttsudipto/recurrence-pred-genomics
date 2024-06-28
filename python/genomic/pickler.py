from .resource import get_ip_data_file_name, get_ip_target_file_name, read_data
from .data_preprocessing import get_top_features, split_blind_data, perform_oversampling
from .optimal_gs_params import get_optimal_params, get_optimal_no_of_features, get_optimal_threshold
from .model import Model
from copy import deepcopy
import pickle
import joblib
import sys


class ModelMetadata:
    def __init__(self, model: Model) -> None:
        self.estimator_id = model.estimator_id
        self.n_folds = model.n_folds
        # self.estimators = []
        # self.total_estimator = None
        self.train_indices = model.train_indices
        self.test_indices = model.test_indices
        self.data = model.data
        self.target = model.target
        self.dataScaler = model.dataScaler

    def get_model(self) -> Model:
        model = Model(self.estimator_id, X=deepcopy(self.data), y=deepcopy(self.target),
                      k=self.n_folds, do_shuffle=False)
        model.train_indices = deepcopy(self.train_indices)
        model.test_indices = deepcopy(self.test_indices)
        model.dataScaler = deepcopy(self.dataScaler)
        return model


def read_input(dataset, os, fs, n_features):
    selected_features = get_top_features(dataset, n_features, fs, verbose=False)
    res = read_data(get_ip_data_file_name(dataset),
                    get_ip_target_file_name(dataset),
                    'Recurrence', fs=selected_features, verbose=False)
    cv_res, blind_res = split_blind_data(res, test_size=0.2, modify_pids=False)
    if os == 'smote':
        cv_res = perform_oversampling(cv_res)
    return cv_res, blind_res


def create_model(dataset, os, fs, model_id, n_features, do_learn=True):
    cv_res, blind_res = read_input(dataset, os, fs, n_features)
    model = Model(model_id, cv_res.data, cv_res.target)
    if do_learn:
        params = get_optimal_params(dataset, os, fs, model_id)
        model.learn(params)
        print(dataset, os, fs, model_id, n_features, params)
        # print('\t', model.predict_k_fold())
    return model


def dump_model_to_file(model: Model, path_prefix: str = '') -> None:
    old_rec_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(0x1000)
    joblib.dump(model.total_estimator, path_prefix + 'total_estimator.joblib')
    for i in range(len(model.estimators)):
        joblib.dump(model.estimators[i], path_prefix + 'estimator_' + str(i) + '.joblib')
    sys.setrecursionlimit(old_rec_limit)
    md = ModelMetadata(model)
    metadata_file = open(path_prefix + 'metadata.pkl', 'wb')
    pickle.dump(md, metadata_file)
    metadata_file.close()


def load_model_from_file(path_prefix: str = '') -> Model:
    metadata_file = open(path_prefix + 'metadata.pkl', 'rb')  # load metadata
    md = pickle.load(metadata_file, encoding='latin1')
    metadata_file.close()
    model = md.get_model()  # `model` without estimators
    model.total_estimator = joblib.load(path_prefix + 'total_estimator.joblib')  # load total_estimator
    for i in range(model.n_folds):
        model.estimators.append(joblib.load(path_prefix + 'estimator_' + str(i) + '.joblib'))
    return model


# dataset = 'dataset1'
# dataset = 'dataset2'
# dataset = 'dataset3'

# os = 'smote'
# os = 'original'

# fs = 'MCFS'
# fs = 'Boruta'
# fs = 'ANOVA'
# fs = 'Combined_MCFS_Boruta'
# fs = None

# model_id = 'RF'
# model_id = 'MLP'
# model_id = 'SVM'


# n_features = get_optimal_no_of_features(dataset, os, fs, model_id)
#
# threshold = get_optimal_threshold(dataset, os, fs, model_id)  # 0.4
# # print(threshold)
#
# m = create_model(dataset, os, fs, model_id, n_features, do_learn=True)
# print(m.predict_k_fold(threshold=threshold))
#
# prefix = 'output/' + dataset + '/models/' + \
#          dataset + '_' + os + '_' + fs + '_' + model_id + '_' + str(n_features) + '/'
# print(prefix)
#
# # dump_model_to_file(m, path_prefix=prefix)
#
# m1 = load_model_from_file(path_prefix=prefix)
# print(m1.predict_k_fold(threshold=threshold))

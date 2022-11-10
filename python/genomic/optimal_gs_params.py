
optimal_no_of_features = {
    'dataset1' : {
        'smote': {
            'MCFS': {'SVM': 60, 'RF': 100, 'MLP': 120}, 
            'Boruta': {'SVM': 140, 'RF': 100, 'MLP': 120}, 
            'ANOVA': {'SVM': 120, 'RF': 140, 'MLP': 140}, 
            'Combined_MCFS_Boruta': {'SVM': 60, 'RF': 100, 'MLP': 140}
        }, 'original': {
            'MCFS': {'SVM': 140, 'RF': 20, 'MLP': 140}, 
            'Boruta': {'SVM': 20, 'RF': 60, 'MLP': 140}, 
            'ANOVA': {'SVM': 140, 'RF': 40, 'MLP': 120}, 
            'Combined_MCFS_Boruta': {'SVM': 60, 'RF': 60, 'MLP': 120}
        }
    }, 'dataset2' : {
        'smote': {
            'MCFS': {'SVM': 120, 'RF': 120, 'MLP': 120}, 
            'Boruta': {'SVM': 60, 'RF': 80, 'MLP': 140}, 
            'ANOVA': {'SVM': 80, 'RF': 80, 'MLP': 120}, 
            'Combined_MCFS_Boruta': {'SVM': 120, 'RF': 100, 'MLP': 80}
        }, 'original': {
            'MCFS': {'SVM': 140, 'RF': 20, 'MLP': 140}, 
            'Boruta': {'SVM': 120, 'RF': 20, 'MLP': 120}, 
            'ANOVA': {'SVM': 60, 'RF': 40, 'MLP': 100}, 
            'Combined_MCFS_Boruta': {'SVM': 40, 'RF': 20, 'MLP': 40}
        }
    },'dataset3' : {
        'smote': {
            'MCFS': {'SVM': 140, 'RF': 140, 'MLP': 120}, 
            'Boruta': {'SVM': 100, 'RF': 80, 'MLP': 80}, 
            'ANOVA': {'SVM': 140, 'RF': 120, 'MLP': 120}, 
            'Combined_MCFS_Boruta': {'SVM': 120, 'RF': 140, 'MLP': 120}
        }, 'original': {
            'MCFS': {'SVM': 140, 'RF': 80, 'MLP': 140}, 
            'Boruta': {'SVM': 140, 'RF': 20, 'MLP': 120}, 
            'ANOVA': {'SVM': 60, 'RF': 40, 'MLP': 20}, 
            'Combined_MCFS_Boruta': {'SVM': 120, 'RF': 20, 'MLP': 120}
        }
    }
}


optimal_thresholds = {
    'dataset1' : {
        'smote': {
            'MCFS': {'SVM': 0, 'RF': None, 'MLP': None}, 
            'Boruta': {'SVM': 0.4, 'RF': None, 'MLP': None}, 
            'ANOVA': {'SVM': -0.1, 'RF': None, 'MLP': None}, 
            'Combined_MCFS_Boruta': {'SVM': 0.4, 'RF': None, 'MLP': None}
        }, 'original': {
            'MCFS': {'SVM': -0.3, 'RF': None, 'MLP': None}, 
            'Boruta': {'SVM': -0.1, 'RF': None, 'MLP': None}, 
            'ANOVA': {'SVM': -0.1, 'RF': None, 'MLP': None}, 
            'Combined_MCFS_Boruta': {'SVM': -0.3, 'RF': None, 'MLP': None}
        }
    }, 'dataset2' : {
        'smote': {
            'MCFS': {'SVM': 0.3, 'RF': None, 'MLP': None}, 
            'Boruta': {'SVM': -0.2, 'RF': None, 'MLP': None}, 
            'ANOVA': {'SVM': 0.3, 'RF': None, 'MLP': None}, 
            'Combined_MCFS_Boruta': {'SVM': -0.2, 'RF': None, 'MLP': None}
        }, 'original': {
            'MCFS': {'SVM': 0.1, 'RF': None, 'MLP': None}, 
            'Boruta': {'SVM': -0.3, 'RF': None, 'MLP': None}, 
            'ANOVA': {'SVM': -0.1, 'RF': None, 'MLP': None}, 
            'Combined_MCFS_Boruta': {'SVM': -0.8, 'RF': None, 'MLP': None}
        }
    }, 'dataset3' : {
        'smote': {
            'MCFS': {'SVM': 0.3, 'RF': None, 'MLP': None}, 
            'Boruta': {'SVM': 0.1, 'RF': None, 'MLP': None}, 
            'ANOVA': {'SVM': 0.6, 'RF': None, 'MLP': None}, 
            'Combined_MCFS_Boruta': {'SVM': 0.2, 'RF': None, 'MLP': None}
        }, 'original': {
            'MCFS': {'SVM': -0.2, 'RF': None, 'MLP': None}, 
            'Boruta': {'SVM': -0.1, 'RF': None, 'MLP': None}, 
            'ANOVA': {'SVM': 0.1, 'RF': None, 'MLP': None}, 
            'Combined_MCFS_Boruta': {'SVM': -0.2, 'RF': None, 'MLP': None}
        }
    }
}


optimal_params = {
    'dataset1': {
        'smote': {
            'MCFS': {
                'SVM': {'kernel': 'poly', 'C': 1, 'degree': 3, 'gamma': 0.1, 'coef0': 1},
                'RF': {'n_estimators': 400, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (300, 60), 'learning_rate_init': 0.0001}
            }, 'Boruta': {
                'SVM': {'kernel': 'poly', 'C': 5, 'degree': 2, 'gamma': 0.01, 'coef0': 1},
                'RF': {'n_estimators': 400, 'max_depth': None, 'max_features': 0.5},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (200, 100), 'learning_rate_init': 0.0001}
            }, 'ANOVA': {
                'SVM': {'kernel': 'rbf', 'C': 10, 'degree': 0, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 200, 'max_depth': None, 'max_features': 0.5},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (50, 50), 'learning_rate_init': 0.01}
            }, 'Combined_MCFS_Boruta': {
                'SVM': {'kernel': 'poly', 'C': 1, 'degree': 2, 'gamma': 0.1, 'coef0': 1},
                'RF': {'n_estimators': 400, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (250, 250), 'learning_rate_init': 0.0001}
            }
        }, 'original': {
            'MCFS': {
                'SVM': {'kernel': 'rbf', 'C': 1, 'degree': 0, 'gamma': 0.001, 'coef0': 0},
                'RF': {'n_estimators': 200, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (175, 87), 'learning_rate_init': 0.001}
            }, 'Boruta': {
                'SVM': {'kernel': 'rbf', 'C': 5, 'degree': 0, 'gamma': 0.1, 'coef0': 0},
                'RF': {'n_estimators': 200, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (200, 200), 'learning_rate_init': 0.0001}
            }, 'ANOVA': {
                'SVM': {'kernel': 'rbf', 'C': 5, 'degree': 0, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 200, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (50,25), 'learning_rate_init': 0.1}
            }, 'Combined_MCFS_Boruta': {
                'SVM': {'kernel': 'rbf', 'C': 5, 'degree': 0, 'gamma': 0.0001, 'coef0': 0},
                'RF': {'n_estimators': 400, 'max_depth': None, 'max_features': None},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (50,25), 'learning_rate_init': 0.001}
            }
        }
    }, 'dataset2': {
        'smote': {
            'MCFS': {
                'SVM': {'kernel': 'poly', 'C': 1, 'degree': 2, 'gamma': 0.1, 'coef0': 0},
                'RF': {'n_estimators': 1000, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (225, 225), 'learning_rate_init': 0.0001}
            }, 'Boruta': {
                'SVM': {'kernel': 'rbf', 'C': 5, 'degree': 0, 'gamma': 0.1, 'coef0': 0},
                'RF': {'n_estimators': 200, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (50, 25), 'learning_rate_init': 0.001}
            }, 'ANOVA': {
                'SVM': {'kernel': 'poly', 'C': 1, 'degree': 2, 'gamma': 0.1, 'coef0': 1},
                'RF': {'n_estimators': 400, 'max_depth': None, 'max_features': 0.5},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (150,), 'learning_rate_init': 0.01}
            }, 'Combined_MCFS_Boruta': {
                'SVM': {'kernel': 'poly', 'C': 10, 'degree': 3, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 600, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (250, 250), 'learning_rate_init': 0.001}
            }
        }, 'original': {
            'MCFS': {
                'SVM': {'kernel': 'rbf', 'C': 5, 'degree': 0, 'gamma': 0.0001, 'coef0': 0},
                'RF': {'n_estimators': 600, 'max_depth': None, 'max_features': 0.5},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (175, 35), 'learning_rate_init': 0.01}
            }, 'Boruta': {
                'SVM': {'kernel': 'rbf', 'C': 1, 'degree': 0, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 400, 'max_depth': None, 'max_features': None},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (200,200), 'learning_rate_init': 0.001}
            }, 'ANOVA': {
                'SVM': {'kernel': 'rbf', 'C': 1, 'degree': 0, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 200, 'max_depth': None, 'max_features': 0.5},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (175,), 'learning_rate_init': 0.01}
            }, 'Combined_MCFS_Boruta': {
                'SVM': {'kernel': 'poly', 'C': 1, 'degree': 2, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 200, 'max_depth': None, 'max_features': None},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (25,5), 'learning_rate_init': 0.01}
            }
        }
    }, 'dataset3': {
        'smote': {
            'MCFS': {
                'SVM': {'kernel': 'rbf', 'C': 10, 'degree': 0, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 200, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (275, 275), 'learning_rate_init': 0.001}
            }, 'Boruta': {
                'SVM': {'kernel': 'poly', 'C': 1, 'degree': 3, 'gamma': 0.1, 'coef0': 1},
                'RF': {'n_estimators': 600, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (275, 55), 'learning_rate_init': 0.001}
            }, 'ANOVA': {
                'SVM': {'kernel': 'poly', 'C': 1, 'degree': 3, 'gamma': 0.1, 'coef0': 2},
                'RF': {'n_estimators': 400, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (275, 55), 'learning_rate_init': 0.001}
            }, 'Combined_MCFS_Boruta': {
                'SVM': {'kernel': 'rbf', 'C': 10, 'degree': 0, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 200, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (200, 40), 'learning_rate_init': 0.0001}
            }
        }, 'original': {
            'MCFS': {
                'SVM': {'kernel': 'rbf', 'C': 10, 'degree': 0, 'gamma': 0.001, 'coef0': 0},
                'RF': {'n_estimators': 1000, 'max_depth': None, 'max_features': None},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (300, 300), 'learning_rate_init': 0.0001}
            }, 'Boruta': {
                'SVM': {'kernel': 'rbf', 'C': 5, 'degree': 0, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 400, 'max_depth': None, 'max_features': 0.5},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (25,), 'learning_rate_init': 0.0001}
            }, 'ANOVA': {
                'SVM': {'kernel': 'rbf', 'C': 1, 'degree': 0, 'gamma': 0.01, 'coef0': 0},
                'RF': {'n_estimators': 600, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (50,25), 'learning_rate_init': 0.001}
            }, 'Combined_MCFS_Boruta': {
                'SVM': {'kernel': 'poly', 'C': 10, 'degree': 3, 'gamma': 0.001, 'coef0': 1},
                'RF': {'n_estimators': 400, 'max_depth': None, 'max_features': 0.25},
                'MLP': {'activation': 'relu', 'hidden_layer_sizes': (200,40), 'learning_rate_init': 0.0001}
            }
        }
    }
}


def get_optimal_params(dataset, os, fs, model_id):
    return optimal_params[dataset][os][fs][model_id]


def get_optimal_no_of_features(dataset, os, fs, model_id):
    return optimal_no_of_features[dataset][os][fs][model_id]


def get_optimal_threshold(dataset, os, fs, model_id):
    return optimal_thresholds[dataset][os][fs][model_id]


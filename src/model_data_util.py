"""

The script declares the functions used in 'model_data.py'

"""
import pandas as pd
from logzero import logger, logfile
import numpy as np

from sklearn.ensemble import RandomForestRegressor
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.ensemble import AdaBoostRegressor
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import BaggingRegressor

from xgboost import XGBRegressor
from catboost import CatBoostRegressor
from lightgbm import LGBMRegressor
import catboost as cb

from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score
from sklearn.metrics import mean_squared_error

import matplotlib.pyplot as plt

from utility import parse_config


##################################################
#-----------------Reading Config------------------
##################################################

config_path = "config/config.yaml"   
config = parse_config(config_path)   # read config file

##################################################
#-----------------Declaring Functions-------------
##################################################

def compare_models(train_data, train_labels, test_data, test_labels, n_estimators):
    
    model_comparison = pd.DataFrame()
    model_names = [ExtraTreesRegressor, AdaBoostRegressor, BaggingRegressor, 
                   GradientBoostingRegressor, RandomForestRegressor, XGBRegressor, 
                   CatBoostRegressor, LGBMRegressor]
    
    for model_name in model_names:
        model = model_name(n_estimators = n_estimators)   # learning_rate does not work here
        model.fit(train_data, train_labels)
        
        # Evaluating the Model
        pred = model.predict(test_data)
        mse = mean_squared_error(pred, test_labels)
        r2 = r2_score(pred, test_labels)
        model_comparison = model_comparison.append({'model_name': model_name, 
                                                    'Mean Squared Error': mse, 
                                                    'R2 Score': r2}, ignore_index = True)
    
    model_comparison.sort_values(by = ['R2 Score'], ascending = False, inplace = True ) 
    
    # x = model_comparison.iloc[0][0]
    
    model_comparison.reset_index(drop = True)
    return model_comparison


def feature_importance(train_data, train_labels, best_model):

    best_model = best_model()
    best_model.fit(train_data, train_labels) 
    feature_importance = best_model.feature_importances_
    
    feature_importance_normalized = np.std([tree.feature_importances_ for tree in 
                                            best_model.estimators_],
                                            axis = 0)       # Normalizing the individual importances
    return feature_importance_normalized    


def evaluate_model(train_data, train_labels, test_data, test_labels, model_name):
  # Declaring Model
  model = model_name(n_estimators = 100) 
  model.fit(train_data, train_labels)

  # Evaluating Model
  pred = model.predict(test_data)    
  mse = mean_squared_error(pred, test_labels)    
  r2 = r2_score(pred, test_labels)
  return r2, mse, model


def plot_feature_importance(train_data, feature_importance):
    plt.bar(train_data.columns, feature_importance)
    plt.xlabel(config["model_data"]["feature_importance"]["xlabel"])
    plt.ylabel(config["model_data"]["feature_importance"]["ylabel"])
    plt.title(config["model_data"]["feature_importance"]["title"])
    plt.xticks(rotation = 'vertical')
    plt.savefig('visualizations/feature_importance.png')

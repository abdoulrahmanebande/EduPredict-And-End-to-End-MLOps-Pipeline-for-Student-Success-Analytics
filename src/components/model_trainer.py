import sys 
import os 

from src.logger import logging 
from src.exception import CustomException 
from src.utils import evaluate_models, save_object 
from dataclasses import dataclass

from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import (
  RandomForestRegressor,
  AdaBoostRegressor
)
from xgboost import XGBRegressor
from sklearn.linear_model import LinearRegression, Ridge, Lasso 
from sklearn.neighbors import KNeighborsRegressor

from typing import List

@dataclass 
class ModelTrainerConfig:
  trained_model_file_path: str=os.path.join('artifacts', 'model.pkl')
  
class ModelTrainer:
  def __init__(self):
    self.model_trainer_config = ModelTrainerConfig()
    
  def initiate_model_trainer(self, train_arr, test_arr):
    try: 
      logging.info('Splitting train and test arrays')
      X_train, y_train, X_test, y_test = (train_arr[:,:-1], train_arr[:,-1], test_arr[:,:-1], test_arr[:,-1])
      
      models = {
        'DecisionTreeRegressor': DecisionTreeRegressor(),
        'RandomForestRegressor': RandomForestRegressor(),
        'AdaBoostRegressor': AdaBoostRegressor(),
        'XGBRegressor': XGBRegressor(),
        'LinearRegression': LinearRegression(),
        'Ridge': Ridge(),
        'Lasso': Lasso(),
        'KNeighborsRegressor': KNeighborsRegressor()
      }
      
      model_report: dict= evaluate_models(X_train, y_train, X_test, y_test, models)
      
      # To get best model metrics from dictionary
      best_model_score = max(sorted(model_report.values()))
      
      # To get best model name from dictionary 
      best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]
      
      best_model = models[best_model_name]
      
      if best_model_score < 0.75: # Test r2_score
        logging.info('No best model found!')  # We need to really do something
        raise CustomException('No best model found!', sys)
      
      logging.info('Saving the model object as pickle file!')
      save_object(file_path=self.model_trainer_config.trained_model_file_path, obj=best_model)
      
      y_train_pred = best_model.predict(X_train)
      y_test_pred = best_model.predict(X_test)
      
      train_r2_score = r2_score(y_train, y_train_pred)
      test_r2_score = r2_score(y_test, y_test_pred)
      
      train_mae = mean_absolute_error(y_train, y_train_pred)
      test_mae = mean_absolute_error(y_test, y_test_pred)
      
      return f"Best model name: {best_model_name}\nTrain R2: {train_r2_score}\nTest R2: {test_r2_score}\nTrain MAE: {train_mae}\nTest MAE: {test_mae}"
    
    except Exception as e:
      logging.info(e)
      raise CustomException(e, sys)
    
    
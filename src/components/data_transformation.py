import sys
import os 

import numpy as np
import pandas as pd 

from sklearn.compose import ColumnTransformer 
from sklearn.preprocessing import OneHotEncoder, RobustScaler
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from src.logger import logging 
from src.exception import CustomException 
from src.utils import save_object 
from dataclasses import dataclass 

@dataclass 
class DataTransformationConfig:
  preprocessor_obj_file_path: str=os.path.join('artifacts', 'preprocessor.pkl')
  
class DataTransformation:
  def __init__(self):
    self.data_transformation_config = DataTransformationConfig()
    
  def get_data_transformer_object(self):
    
    try:
      numerical_features = ['writing_score', 'reading_score']
      categorical_features = ['gender', 'race_ethnicity', 'parental_level_of_education', 'lunch', 'test_preparation_course']
      
      logging.info('Entering data pre-processing and feature engineering stage!')
      num_pipeline = Pipeline(
        steps=[
          ('impute', SimpleImputer(strategy='median')), # 'median' is good for outliers. But our dataset
          ('scaler', RobustScaler())                    # does not have any missing values.
        ]
      )
      
      cat_pipeline = Pipeline(
        steps= [
          ('impute', SimpleImputer(strategy='most_frequent')),
          ('one_hot_encoder', OneHotEncoder())
          # No need to scaling categorical features
        ]
      )
      logging.info('Data pre-processing and feature engineering completed!')
      
      preprocessor = ColumnTransformer([
        ('numerical_pipeline', num_pipeline, numerical_features),
        ('categorical_pipeline', cat_pipeline, categorical_features)
      ])
      return preprocessor
    
    except Exception as e:
      logging.info(e)
      raise CustomException(e, sys)
    
  def initiate_data_transformation(self, train_path, test_path):
    try:
      
      train_df = pd.read_csv(train_path)
      test_df = pd.read_csv(test_path)
      logging.info('Read train and test DataFrames')
      
      logging.info('Initializing preprocessor object!')
      preprocessor_obj = self.get_data_transformer_object() 
      target_feature_name = 'math_score'
      
      input_features_train_df = train_df.drop(target_feature_name, axis=1)
      target_feature_train_df = train_df[target_feature_name]
      
      input_features_test_df = test_df.drop(target_feature_name, axis=1)
      target_feature_test_df = test_df[target_feature_name]
      
      logging.info('Initiating the fit and transform process!')
      
      input_features_train_arr = preprocessor_obj.fit_transform(input_features_train_df)
      input_features_test_arr = preprocessor_obj.transform(input_features_test_df)
      logging.info('Fit and transform completed')
      
      logging.info('Combining data as array initiated!')
      train_arr = np.c_[input_features_train_arr, np.array(target_feature_train_df)]
      test_arr = np.c_[input_features_test_arr, np.array(target_feature_test_df)]
      logging.info('Arrays combination completed')
      
      save_object(self.data_transformation_config.preprocessor_obj_file_path, preprocessor_obj)
      
      return (
        train_arr, 
        test_arr, 
        self.data_transformation_config.preprocessor_obj_file_path
      )
      
    except Exception as e:
      logging.info(e)
      raise CustomException(e, sys)
    
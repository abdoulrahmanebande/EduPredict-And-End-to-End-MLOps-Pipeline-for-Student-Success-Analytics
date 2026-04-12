import pandas as pd

from src.exception import CustomException
from src.logger import logging 
from src.utils import load_object

import sys


class PredictPipeline:
  def __init__(self):
    pass
  
  def predict(self, features):
    try:
      logging.info('Loding models!')
      model = load_object('artifacts/model.pkl')
      preprocessor = load_object('artifacts/preprocessor.pkl')
      
      logging.info('Transforming the features taken from the EduPredict website.')
      data_scaled = preprocessor.transform(features)
      
      logging.info("Predicting the student's math score")
      preds = model.predict(data_scaled)
      
      final_prediction = preds[0]
      
      # Post-processing: Ensure score is between 0 and 100
      final_prediction = preds[0]
      if final_prediction < 0:
          final_prediction = 0
      elif final_prediction > 100:
          final_prediction = 100
          
      return round(final_prediction, 2)
    
    except Exception as e:
      logging.info(e)
      raise CustomException(e, sys)

class CustomData:
  def __init__(
    self,
    gender: str,
    race_ethnicity: str,
    parental_level_of_education: str,
    lunch: str,
    test_preparation_course: str,
    reading_score: int,
    writing_score: int):
    self.gender = gender
    self.race_ethnicity = race_ethnicity
    self.parental_level_of_education = parental_level_of_education
    self.lunch = lunch
    self.test_preparation_course = test_preparation_course
    self.reading_score = reading_score
    self.writing_score = writing_score
    
  def get_custom_data_as_data_frame(self):
    custom_data = {
      'gender': [self.gender],
      'race_ethnicity': [self.race_ethnicity],
      'parental_level_of_education': [self.parental_level_of_education],
      'lunch': [self.lunch],
      'test_preparation_course': [self.test_preparation_course],
      'reading_score': [self.reading_score],
      'writing_score': [self.writing_score]
    }
    
    data_df = pd.DataFrame(custom_data)
    return data_df
import sys 
import os 
import dill

from src.logger import logging
from src.exception import CustomException 

from sklearn.metrics import r2_score

def save_object(file_path, obj):
  
  try:
    directory_name = os.path.dirname(file_path)
    os.makedirs(directory_name, exist_ok=True)
    
    logging.info('Initialization of object saving !')
    with open(file_path, "wb") as file_obj:
      dill.dump(obj, file_obj)
    logging.info('Object saved !') 
    
  except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)
  
  
def evaluate_models(X_train, y_train, X_test, y_test, models):
  try:
    report = {}
    for i in range(len(list(models))):
      model = list(models.values())[i]
      
      logging.info('Initiating model training!')
      model.fit(X_train, y_train)
      
      logging.info('Making prediction on test dataset!')
      y_test_pred = model.predict(X_test)
      
      logging.info('Computing R2 metric!')

      test_r2_score = r2_score(y_test, y_test_pred)
    
      report[list(models.keys())[i]] = test_r2_score
      
    return report
    
  except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)
  
def load_object(file_path):
  try:
    with open(file_path, 'rb') as file_obj:
      return dill.load(file_obj)
  
  except Exception as e:
    logging.info(e)
    raise CustomException(e, sys)
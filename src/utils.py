import sys 
import os 
import dill

from src.logger import logging
from src.exception import CustomException 

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
  
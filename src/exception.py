import sys 

def error_message_details(error, error_detail: sys):
  '''
  Customizing the look of any error message we get
  '''
  _,__,exc_tb = error_detail.exc_info()
  
  file_name = exc_tb.tb_frame.f_code.co_filename
  error_message = "Error occurred in python script name {} line number {} error message {}".format(
    file_name,
    exc_tb.tb_lineno,
    str(error)
  )
  return error_message

class CustomException(Exception):
  def __init__(self, error_message, error_detail: sys):
    super().__init__(error_message)
    
    self.error_message = error_message_details(error_message, error_detail=error_detail)
    
  def __str__(self):
    return self.error_message
  
if __name__== '__main__':
  try:
    a = 1/0
  except Exception as e:
    from src.logger import logging
    logging.info('Error: {}'.format(str(e)))
    raise CustomException(e, sys)
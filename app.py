from flask import Flask, request, render_template 
from src.pipeline.predict_pipeline import PredictPipeline, CustomData

application = Flask(__name__)
app = application

@app.route('/')
@app.route('/home')
def home():
  return render_template('home.html')

@app.route('/contact-me')
def contact():
  return render_template('contact.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
  if request.method == 'GET':
    return render_template('predict.html')
  
  else: 
    request_data = CustomData(
      gender = request.form.get('gender'),
      race_ethnicity = request.form.get('race_ethnicity'),
      parental_level_of_education = request.form.get('parental_level_of_education'),
      lunch= request.form.get('lunch'),
      test_preparation_course = request.form.get('test_preparation_course'),
      reading_score = request.form.get('reading_score'),
      writing_score = request.form.get('writing_score')
    )
    
    pred_df = request_data.get_custom_data_as_data_frame()
    
    predict_pipeline = PredictPipeline()
    result = predict_pipeline.predict(pred_df)
    
    return render_template('predict.html', result = result)
  
  
if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)
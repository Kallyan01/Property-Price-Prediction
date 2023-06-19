from flask import Flask ,request, jsonify
from flask_restful import Resource, Api
import pandas as pd
import pickle

app = Flask(__name__)
data = pd.read_csv('cleaned_data.csv')
pipe = pickle.load(open('Model2.pkl','rb'))


@app.route('/')
def hello():
        return "Hello World"
    
@app.route('/predict',methods=['POST'])
def predict():
      data = request.get_json()
      bhk = data['bhk']
      sqft_living = data['sqft']
      zipcode = data['zipcode']
      print(bhk,sqft_living,zipcode)
      input = pd.DataFrame([[bhk,sqft_living,zipcode]],columns=['bhk','sqft_living','zipcode'])
      result = round(pipe.predict(input)[0],2)
      if(result):
            return jsonify({"price":  result })
      return jsonify({"message":  "Something Went Wrong !" })

      
if __name__ == '__main__':
    app.run(debug=True, port = 5001)
    
         


         
        
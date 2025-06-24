import pandas as pd
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
data = pd.read_csv('CleanedData.csv')
pipe = pickle.load(open("RidgeModel.pkl", 'rb'))

@app.route('/')
def index():
    locations = sorted(data['location'].unique())
    return render_template('index.html', locations=locations)

@app.route('/predict', methods=['POST'])
def predict():
    location = request.form.get('location')
    bhk = float(request.form.get('bhk'))
    bath = float(request.form.get('bath'))
    sqft = float(request.form.get('total_sqft'))

    input_df = pd.DataFrame([{
        'location': location,
        'total_sqft': sqft,
        'bath': bath,
        'bhk': bhk
    }])

    prediction = pipe.predict(input_df)[0] * 1e5

    return str(round(prediction, 2))  # Optional: round to 2 decimal places

if __name__ == "__main__":
    #app.run(debug=True, port=5001)
    app.run(host='0.0.0.0', port=10000)



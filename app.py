import pickle
from flask import Flask, request, app, jsonify, render_template, url_for
import numpy as np
import pandas as pd

# Starting point of the app
app = Flask(__name__)

# Loading the model
regrModel = pickle.load(open('RegrModel.pkl', 'rb'))
scalar = pickle.load(open('scaling.pkl', 'rb'))

# Home page route
@app.route('/')
def homePage():
    return render_template('HomePage.html')

# Predict api route
@app.route('/predict_api', methods=['POST'])
def predict_api():
    data = request.json['data']
    print(data)
    print(np.array(list(data.values())).reshape(1,-1))
    new_data = scalar.transform(np.array(list(data.values())).reshape(1,-1))
    output = regrModel.predict(new_data)
    print(output[0])
    return jsonify(output[0])

#
@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    final_input = scalar.transform(np.array(data).reshape(1,-1))
    print(final_input)
    output = regrModel.predict(final_input)[0]
    return render_template("HomePage.html", prediction_text="The house price would be: {}".format(output))


if __name__ == "__main__":
    app.run(debug=True)

    


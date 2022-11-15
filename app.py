from flask import Flask, render_template, request, jsonify
import json
import numpy as np
from json import JSONEncoder
from feature import feature_extraction
from model_predict import prediction

app = Flask(__name__, template_folder='templates')

UPLOAD_FOLDER = 'D:/appntu/static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# อนุญาติเฉพาะภาพเท่านั้น
ALLOWED_EXTENSIONS = ['png', 'jpg', 'jpeg']

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Function to load and prepare the image in right shape


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])    
def predict():
    file = request.files['file']
    if file:
        feature_extraction(file)
        mypredict = prediction(file)
        output = round(mypredict[0], 2)
        encodedoutput = json.dumps(output, cls=NumpyArrayEncoder)
        return jsonify(encodedoutput)
    return jsonify({"error": "Missing data!"})

# แสดง error
if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')


class NumpyArrayEncoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

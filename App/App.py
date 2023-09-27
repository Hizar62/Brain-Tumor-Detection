from flask import Flask, render_template, request
import numpy as np
import os
from model import image_pre, predict

app = Flask(__name__)

UPLOAD_FOLDER = 'C:\\Users\\Hizar\\Downloads\\anotherone\\Brain-Tumor-Detection\\App\\static'
ALLOWED_EXTENSHIONS = set({'png','jpg','jpeg'})
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file1' not in request.files:
            return 'There is no File in Form'
        file1 = request.files['file1']
        path = os.path.join(app.config['UPLOAD_FOLDER'], 'output.jpg')
        file1.save(path)

        data = image_pre(path)
        s = predict(data)
        if s == 1:
            result = "No Brain Cancer"
        else:
            return "Brain Cancer"
    return render_template('index.html', result = result)




if __name__ == '__main__':
    app.run(debug=True)

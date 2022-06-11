from flask import Flask, render_template, request
import numpy as np
import pickle
import os
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)
        return render_template('upload.html', path = file_path)
    return render_template('upload.html', path = "")

if __name__ == '__main__':
    app.run(debug=True)
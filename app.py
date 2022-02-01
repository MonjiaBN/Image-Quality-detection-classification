from flask import Flask, flash, request, redirect, render_template
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import io
from PIL import Image
import base64
from Helpers import *


app = Flask(__name__)

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def upload_form():
    return render_template('upload.html')


@app.route('/', methods=['POST'])
def upload_image():
    images = []
    for file in request.files.getlist("file[]"):
         
        print("image: ", file)
        # If the user does not select a file, the browser submits an
        # empty file without a filename.

        if file.filename == '':
            flash('Please select image to upload')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            # sanitize a file's name before storing it
            filename = secure_filename(file.filename)
            print("image uploaded successfully")
            filestr = file.read()
            # convert string data to numpy array
            npimg = np.frombuffer(filestr, np.uint8)
            # convert numpy array to image

            image = cv2.imdecode(npimg, cv2.IMREAD_UNCHANGED)
            ratio = image.shape[0] / 400.0
            orig = image.copy()
            image = Helpers.resize(image, height=400,width=400)

            gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            fm = cv2.Laplacian(gray, cv2.CV_64F).var()
            quality = "Clear image"

            if fm < 300:
                quality = "Blurry image"

            sharpness_value = "{:.0f}".format(fm)
            message = [quality, sharpness_value]

            img = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # using BytesIO we get the in-memory info to save the image we just read
            file_object = io.BytesIO()
            img = Image.fromarray(Helpers.resize(img,height=400, width=300))
            
            img.save(file_object, 'PNG')
            # display image in html
            # base64encode to transfer the image we saved as in-memory to html.
            base64img = "data:image/png;base64," + \
                base64.b64encode(file_object.getvalue()).decode('ascii')
            images.append([message, base64img])

    print("images:", len(images))
    return render_template('upload.html', images=images)


if __name__ == "__main__":
    app.run(debug=True)

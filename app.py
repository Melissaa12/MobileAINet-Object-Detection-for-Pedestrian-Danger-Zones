from flask import Flask,render_template, request, flash
from flask.helpers import url_for
from werkzeug.utils import redirect, secure_filename
import os
import predicty
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import pathlib
import sys
from PIL import Image

app = Flask(__name__)

UPLOAD_FOLDER = 'static/uploads/'
app.secret_key = "melissa"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['png','JPG','jpeg','gif','txt','pdf','jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    print('Home page!', file=sys.stderr)

    return render_template("index.html")

@app.route('/',methods =['POST'])
def upload_image():
    print('image loaded!', file=sys.stderr)

    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('no image selected')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename= "image.jpg"
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
        image = Image.open('static/uploads/image.jpg')
        new_image = image.resize((640, 640))
        new_image.save('static/uploads/image.jpg')
        return render_template('index.html',filename=filename)
    else: 
        flash('not allowed image')
        return redirect(request.url)

@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static',filename='uploads/'+filename),code=301)


@app.route("/predict", methods=['GET', 'POST'])
def index():
    print("predict", file=sys.stderr)

    print(request.method, file=sys.stderr)
    if request.method == 'POST':
        if request.form.get('Predict') == 'Predict':
            # pass
            print("Predict")
            newfilename = predict()
            return render_template('index.html',filename=newfilename)
        else:
            # pass # unknown
            return render_template("index.html")
    elif request.method == 'GET':
        # return render_template("index.html")
        print("No Post Back Call")
        return render_template("index.html")

def predict():
    # Load the TFLite model and allocate tensors.
    interpreter = tf.lite.Interpreter(model_path="predict.tflite")
    interpreter.allocate_tensors()

    # Get input and output tensors.
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()
    
    for file in pathlib.Path('static/uploads').iterdir():
        img = cv2.imread(r"{}".format(file.resolve()))
        new_img = cv2.resize(img, (640, 640))
        new_img2 = new_img.astype(np.float32)
        new_img2 /= 255.0
        bordersize = 0
        border = cv2.copyMakeBorder(
        new_img,
        top=bordersize,
        bottom=bordersize,
        left=bordersize,
        right=bordersize,
        borderType=cv2.BORDER_CONSTANT)
        interpreter.set_tensor(input_details[0]['index'], [new_img2])
        interpreter.invoke()
        output_data = interpreter.get_tensor(output_details[0]['index'])  # get tensor  x(1, 25200, 7)

        xyxy, classes, scores = predicty.YOLOdetect(output_data) #boxes(x,y,x,y), classes(int), scores(float) [25200]
        maxscore_0= 0
        target_indices_0 = 0
        maxscore_1= 0
        target_indices_1 = 0
        maxscore_2= 0
        target_indices_2 = 0
        maxscore_3= 0
        target_indices_3 = 0
        maxscore_4= 0
        target_indices_4 = 0
        maxscore_5= 0
        target_indices_5 = 0

        for i in range(len(scores)):
            if ((scores[i] > 0.1) and (scores[i] <= 1.0)):
                if(classes[i]==0):
                    if(scores[i]>maxscore_0):
                        maxscore_0 = scores[i]
                        target_indices_0 = i 
                if(classes[i]==1):
                    if(scores[i]>maxscore_1):
                        maxscore_1 = scores[i]
                        target_indices_1 = i 
                if(classes[i]==2):
                    if(scores[i]>maxscore_2):
                        maxscore_2 = scores[i]
                        target_indices_2 = i                         
                if(classes[i]==3):
                    if(scores[i]>maxscore_3):
                        maxscore_3 = scores[i]
                        target_indices_3 = i 
                if(classes[i]==4):
                    if(scores[i]>maxscore_4):
                        maxscore_4 = scores[i]
                        target_indices_4 = i 
                if(classes[i]==5):
                    if(scores[i]>maxscore_5):
                        maxscore_5 = scores[i]
                        target_indices_5 = i    
        list_indices = [target_indices_0,target_indices_1,target_indices_2,target_indices_3,target_indices_4,target_indices_5]

        for i in list_indices:
            if i != 0:
                H = new_img2.shape[0]
                W = new_img2.shape[1]
                xmin = int(max(1,(xyxy[0][i] * W)))
                ymin = int(max(1,(xyxy[1][i] * H)))
                xmax = int(min(H,(xyxy[2][i] * W)))
                ymax = int(min(W,(xyxy[3][i] * H)))
                label = predicty.label_name(classes[i])
                color = predicty.label_color(classes[i])
                cv2.rectangle(border, (xmin,ymin), (xmax,ymax), color, 2)   
                cv2.putText(border,label+ "   " + str(scores[i]),(xmin,ymax+20),cv2.FONT_HERSHEY_SIMPLEX,0.7,color,2)

        cv2.imwrite('static/uploads/image.jpg',border)
    return "image.jpg"

if __name__ == "__main__":
    app.run(debug=True)            


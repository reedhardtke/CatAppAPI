from flask import Flask
from flask_restful import reqparse, abort, Api, Resource
from flask import request, jsonify
from tensorflow import keras
import numpy as np
import json
from PIL import Image


model = keras.models.load_model('../model/model.py')

# open image, resize, reshape, predict
def get_img(path_name):
    # '/Users/reedhardtke/Downloads/archive_cat/CAT_00/00000455_010.jpg'
    path_name = '/' + path_name
    image = Image.open(path_name)
    img_resized = image.resize((32,32))
    img_arr = np.asarray(img_resized)
    img_reshaped = img_arr.reshape(1,32,32,3)
    result = model.predict(img_reshaped)
    return label_name(result)

# take result data and return a label string
def label_name(result):
    labels = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
    
    for ind, a in enumerate(result[0]):
        if result[0][ind] > 0.2:
            result[0][ind] = 1.0
        else:
            result[0][ind] = 0.0
    
    for ind, a in enumerate(result[0]):
        if result[0][ind] == 1:
            return labels[ind]
    return 'unknown'


app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def hello_world():
    return 'Hello world'

@app.route('/api', methods=['GET'])
def retrieve_label():
    # check for img
    if 'img' in request.args:
        path = request.args['img']
    else:
        return "Error"
    
    label = get_img(path)
    print(label)


    ret_label = {'label': label}

    ret_json = jsonify(ret_label)
    #print('\n\n\n\n\n')
    #print(ret_json)
    return ret_json

if __name__ == '__main__':
    app.run()
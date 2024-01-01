from flask import Flask, request, render_template, jsonify
import numpy as np
import os
os.environ['CUDA_VISIBLE_DEVICES'] = ''
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf

import tensorflow_hub as hub
from io import BytesIO
from PIL import Image
from keras.preprocessing import image
import base64
import json
import cv2
from tensorflow.keras.models import load_model

app = Flask(__name__)
# CORS(app)  # Enable CORS for all routes

model = load_model('stacked_unet_29.h5')

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/faq')
def faq():
    return render_template('faq.html')
@app.route('/aboutus')
def aboutus():
    return render_template('aboutus.html')


@app.route('/convert', methods=['POST'])
def upload_image():
    try:
        file = request.files['image']

        if file:
            img = Image.open(BytesIO(file.read()))

            img_array = np.array(img)

            if img_array.shape != (128, 128):
                # Resize ảnh về kích thước 128x128
                img_array = cv2.resize(img_array, (128, 128), interpolation=cv2.INTER_AREA)

            img_array_normalize = img_array / 255.0
            print(img_array_normalize.shape)
            print(np.max(img_array_normalize))
            # 128x128


            img_array_1 = np.expand_dims(img_array_normalize, axis=-1)
            print(img_array_1.shape)
            #128x128x1

            image_to_predict = np.expand_dims(img_array_1, axis=0)
            predictions = model.predict(image_to_predict)
            reconstructed_image = predictions[0]
            print("Shape of the reconstructed_image array:",reconstructed_image.shape)
            ##128x128x1
            
            result = np.squeeze(reconstructed_image)
            print("Shape of the result array:",result.shape)

            result = (result * 255).astype(np.uint8)
            ## result shape = 128x128

            # Resize result từ 128x128 thành 512x512
            result_resized = cv2.resize(result, (512, 512))

            # Mã hóa mảng NumPy thành base64
            _, buffer = cv2.imencode('.png', result_resized)
            img_base64 = base64.b64encode(buffer).decode('utf-8')

            return jsonify({
                "img": img_base64
            })
            # return render_template('result.html', image_array=img_base64)
    except Exception as e:
        return jsonify({"error": str(e)})



if __name__ == '__main__':
    app.run(debug=True)
    

from flask import Flask, render_template, request, redirect, url_for, send_from_directory, abort, make_response, current_app, jsonify
import numpy as np
import cv2
from datetime import datetime
import os
import string
import random

from predict_kao import predict_kao
from predict_PC import predict_PC
import sys
import json

out="UDN_Ver_1.0"
SAVE_DIR = "./images"
if not os.path.isdir(SAVE_DIR):
    os.mkdir(SAVE_DIR)

app = Flask(__name__, static_url_path="")

def random_str(n):
    return ''.join([random.choice(string.ascii_letters + string.digits) for i in range(n)])

@app.route('/')
def index():
    
    #return render_template('index.html', images=os.listdir(SAVE_DIR)[::-1],out=out)
    return render_template('index.html')

@app.route('/images/<path:path>')
def send_js(path):
    return send_from_directory(SAVE_DIR, path)


@app.route('/upload', methods=['POST'])
def upload():
    if request.files['image']:
        # 画像として読み込み
        stream = request.files['image'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)



        # 保存
        #dt_now = datetime.now().strftime("test") + random_str(5)
        dt_now='image'
        save_path = os.path.join(SAVE_DIR, dt_now + ".png")
        cv2.imwrite(save_path, img)
        print("save", save_path)
        print("ok---------------")

        name_kao=predict_kao(save_path)
        name_PC=predict_PC(save_path)

        #return redirect('/')
        return render_template('ans.html',name_kao=name_kao,name_PC=name_PC)
    else:
        return render_template('index.html')


#元ans2
'''
@app.route('/upload2', methods=['POST'])
def upload2():
    if request.files['image']:
        # 画像として読み込み
        stream = request.files['image'].stream
        img_array = np.asarray(bytearray(stream.read()), dtype=np.uint8)
        img = cv2.imdecode(img_array, 1)



        # 保存
        #dt_now = datetime.now().strftime("test") + random_str(5)
        dt_now='image2'
        save_path = os.path.join(SAVE_DIR, dt_now + ".png")
        cv2.imwrite(save_path, img)
        print("save", save_path)
        print("ok---------------")

        name,pasent=predict2(save_path)

        #return redirect('/')
        return render_template('ans2.html',name=name,p=pasent)
    else:
        return render_template('index2.html')
'''

@app.route('/ans', methods=['POST'])
def post():
    return render_template('index.html')

@app.route('/re', methods=['POST'])
def post3():
    #return render_template('home.html')
    return redirect('/')

if __name__ == '__main__':
    app.run()

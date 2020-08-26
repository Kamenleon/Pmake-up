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
        print("ok----------------")

        pk1,pk2,pk3,pk4,pk5,kname,km=predict_kao(save_path)
        pp1,pp2,pp3,pp4,pname,pm=predict_PC(save_path)

        #return redirect('/')
        return render_template('ans.html',kname=kname,pk1=pk1,pk2=pk2,pk3=pk3,pk4=pk4,pk5=pk5,pp1=pp1,km=km,pname=pname,pp2=pp2,pp3=pp3,pp4=pp4,pm=pm)
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

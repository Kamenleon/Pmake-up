#from phlatib import Path
from pathlib import Path
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from io import BytesIO


#####  mike=0,siro=1  ######


def predict_kao(path):



    model_path = "./logdir/model_file_kao.hdf5"


    #classes = ["maru","omonaga","sankaku","sikaku","tamago"]
    classes = ["丸","面長","逆三角","四角","卵"]
    # load model
    model = load_model(model_path)


    image_size=64

    X = []

    image=path

    image=Image.open(image)
    #image = Image.open(pil_img)
    image = image.convert("RGB")
    image = image.resize((image_size, image_size))
    data = np.asarray(image)
    X.append(data)
    X = np.array(X)
    #正規化(0-1)
    X = X.astype('float32')
    X = X / 255.0

    result = model.predict([X])[0]
    predicted = result.argmax()
    #percentage = int(result[predicted] * 100)
    #return "{0}({1} %)".format(classes[predicted],percentage)

    #return classes[predicted],str(percentage)
    #return classes[predicted]

    result2= [int(n*100) for n in result]
    return result2[0],result2[1],result2[2],result2[3],result2[4],classes[predicted]










#print('ok')
#print(predict('./sample_image/yosida.jpg'))


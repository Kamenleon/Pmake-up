#from phlatib import Path
from pathlib import Path
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from io import BytesIO


#####  mike=0,siro=1  ######


def predict(path):

    
    #model_path = "./logdir/model_file.hdf5"
    model_path = "./logdir/model_file2.hdf5"
    

    classes = ["ムロツヨシ","阿部寛","吉沢亮","吉田沙保里","橋本環奈","広瀬すず","山崎賢人","篠原涼子","石原さとみ","大泉洋","北川景子","木村拓哉"]
    # load model
    model = load_model(model_path)

    #image_size=100
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
    percentage = int(result[predicted] * 100)
    #return "{0}({1} %)".format(classes[predicted],percentage)

    return classes[predicted],str(percentage)

    #if result[predicted]>0.25:
    #    return "This is {}".format(classes[predicted])
    #else:
    #    return "Cat is not exist"




   
    
#print('ok')
#print(predict('./sample_image/yosida.jpg'))


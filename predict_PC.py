#from phlatib import Path
from pathlib import Path
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from io import BytesIO





def predict_PC(image):
    
    model_path = "./logdir/model_file_PC.hdf5"

    classes = ['夏','秋','春','冬']
    # load model
    model = load_model(model_path)

    image_size=64

    X = []
    
    image=Image.open(image)
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
    #return classes[predicted],str(percentage)

    #return classes[predicted]

    #夏冬春秋に並び変える
    result2=[result[0],result[3],result[2],result[1]]

    result3= [int(n*100) for n in result2]
    return result3[0],result3[1],result3[2],result3[3],classes[predicted],max(result3)  

    
#print('ok')
#print(predict('./python/datasetmaker/mendata/うどん/images.jpg'))


#from phlatib import Path
from pathlib import Path
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import load_model
from io import BytesIO





def predict2(image):

    model_path = "./logdir/model_file3.hdf5"

    classes = ['うどん','そば','パスタ','らーめん']
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
    percentage = int(result[predicted] * 100)
    return classes[predicted],str(percentage)

    
#print('ok')
#print(predict('./python/datasetmaker/mendata/うどん/images.jpg'))


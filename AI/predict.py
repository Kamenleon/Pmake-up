from pathlib import Path
import numpy as np
from PIL import Image
from keras.models import load_model
import glob

#####  mike=0,siro=1  ######

#model_path = "logdir/model_file.hdf5"
#model_path = "/Users/ryunosuke/Desktop/python/original_aug/logdir/model_file.hdf5"
#images_folder = "/Users/ryunosuke/Desktop/python/original_aug/sample_images"

model_path = "./logdir/model_file_PC.hdf5"
images_folder = "./test_image"

classes = ["夏","秋","春","冬"]

# load model
model = load_model(model_path)

#image_size=100
image_size=64
X = []

#dir = "/Users/ryunosuke/Desktop/python/original_aug/sample_images"
#dir = "./sample_image"
dir = images_folder
#パスの確認
#print(dir)

files = glob.glob(dir + "/*.jpg")
for i, file in enumerate(files):
    image = Image.open(file)
    image = image.convert("RGB")
    image = image.resize((image_size, image_size))
    data = np.asarray(image)
    X.append(data)
    
 
X = np.array(X)


#正規化(0-1)
X = X.astype('float32')
X = X / 255.0

print(len(files))
'''
##softmax
for w in range(len(files)):

    result = model.predict([X])[w]
    predicted = result.argmax()
    percentage = int(result[predicted] * 100)
    print(files[w].strip(dir))
    print("{0}({1} %)".format(classes[predicted],percentage))
'''


#各値を返す。（並び変えてる）
result = model.predict([X])[0]
#predicted = result.argmax()
#percentage = int(result[predicted] * 100)
result2=[result[0],result[3],result[2],result[1]]
print(result2)




#test
#print(model.predict_classes(X))


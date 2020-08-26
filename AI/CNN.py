#元々の実行環境
# tf2.0
# keras 2.1.2以上

#DATADIR=open("/Users/ryunosuke/Desktop/python/original/dataset","r")

import keras
from keras.utils import np_utils
from keras.models import Sequential
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Dense, Dropout, Activation, Flatten
from keras.layers import BatchNormalization
from keras.optimizers import SGD
import numpy as np
from sklearn.model_selection import train_test_split
from PIL import Image
import glob

from PIL import Image
import matplotlib.pyplot as plt

import os
from keras.callbacks import TensorBoard,ModelCheckpoint



#ハイパーパラメーター
hp1 = {}
hp1['class_num'] = 4 # クラス数
hp1['batch_size'] = 64 # バッチサイズ #####32
hp1['epoch'] = 20 #エポック数



#データセットのロード
X_train, X_test, y_train, y_test = np.load("./dataset/PC.npy", allow_pickle=True)


#入力サイズ
input_shape=X_train.shape[1:]

# CNNを構築
def CNN(input_shape):
        model = Sequential()
 
        model.add(Conv2D(32, (3, 3), padding='same',input_shape=input_shape))
        model.add(Activation('relu'))
        model.add(Conv2D(32, (3, 3)))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(64, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(Conv2D(64, (3, 3)))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))

        model.add(Conv2D(128, (3, 3), padding='same'))
        model.add(Activation('relu'))
        model.add(Conv2D(128, (3, 3)))
        model.add(BatchNormalization())
        model.add(Activation('relu'))

        model.add(MaxPooling2D(pool_size=(2, 2)))
        model.add(Dropout(0.25))


        model.add(Flatten())
        model.add(Dense(512))
        model.add(BatchNormalization())
        model.add(Activation('relu'))
        model.add(Dropout(0.5))
        model.add(Dense(hp1['class_num']))
        model.add(Activation('softmax'))
    
        return model
 

#モデルを選択
model=CNN(input_shape)



#コンパイル

model.compile(loss='categorical_crossentropy',optimizer='SGD',metrics=['accuracy'])


#データの記録
log_dir = os.path.join(os.path.dirname(__file__), "logdir")
model_file_name="model_file.hdf5"

#訓練
history = model.fit(
        X_train, y_train,
         epochs=hp1['epoch'],
         validation_split = 0.2,
         callbacks=[
                TensorBoard(log_dir=log_dir),
                ModelCheckpoint(os.path.join(log_dir,model_file_name),save_best_only=True)
                ]
        )

#評価 & 評価結果出力


loss,accuracy = model.evaluate(X_test, y_test, batch_size=hp1['batch_size'])

# 損失の履歴をプロット
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Learning loss')
plt.xlabel('epoch')
plt.ylabel('loss')
plt.legend(['model1 loss', 'model1 val_loss'], loc='upper right')
plt.show()

# 精度の履歴をプロット
#keras2.1.2を使用
#plt.plot(history.history['acc'])
#plt.plot(history.history['val_acc'])

#keras 2.1.2以上を使う場合
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Learning  accuracy')
plt.xlabel('epoch')
plt.ylabel('accuracy')
plt.legend(['model1 acc', 'model1 val_acc'], loc='lower right')
plt.show()



print('loss=',loss,'accuracy=',accuracy)


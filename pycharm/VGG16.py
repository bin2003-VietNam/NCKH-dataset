# import cv2
# import keras
# import numpy as np
# from keras.layers import Conv2D, MaxPooling2D
# import matplotlib.pyplot as plt
# import tensorflow as tf
# from keras.src.layers import Flatten, Dense
#
# tf.random.set_seed(0)
#
# model = keras.Sequential()
#
# img = cv2.imread("img.jpg")
# img = cv2.resize(img, (224, 224))
# # cv2.imshow("img",img)
# # cv2.waitKey(0)
#
# #block 1
# model.add(Conv2D(64, kernel_size=(3, 3), padding="same", activation="relu", input_shape=(224, 224, 3)))
# model.add(Conv2D(64, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
#
# #block 2
# model.add(Conv2D(128, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(Conv2D(128, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
#
# #block 3
# model.add(Conv2D(256, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(Conv2D(256, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(Conv2D(256, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
#
# #block 4
# model.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
#
# #block 5
# model.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(Conv2D(512, kernel_size=(3, 3), padding="same", activation="relu"))
# model.add(MaxPooling2D(pool_size=(2, 2), strides=(2, 2)))
#
# #Top
# model.add(Flatten())
# model.add(Dense(4896, activation="relu"))
# model.add(Dense(4896, activation="relu"))
# model.add(Dense(3, activation="softmax"))
#
# model.build()
# model.summary()
#
# result = model.predict(np.array([img]))
#
# # for i in range(64):
# #     feature_img = result[0, :, :, i]
# #     ax = plt.subplot(8, 8, i + 1)
# #     ax.set_xticks([])
# #     ax.set_yticks([])
# #     plt.imshow(feature_img, cmap="gray")
# # plt.show()

import tensorflow as tf

print("TensorFlow version:", tf.__version__)
print("GPU Available:", tf.config.list_physical_devices('GPU'))


import tensorflow as tf
# from tensorflow.keras.models import Sequential
# from tensorflow.keras.layers import LSTM, Dense
from keras import layers, models
import cv2


# 간단한 LSTM 모델 예제
model = models.Sequential([
    layers.LSTM(50, return_sequences=True, input_shape=(10, 5)),  # (timesteps=10, features=5)
    layers.LSTM(50),
    layers.Dense(1, activation='sigmoid')
])

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
model.summary()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov  7 14:20:07 2023

@author: soumensmacbookair
"""

#%% Imports
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#%% Load MNIST dataset
fashion_mnist = tf.keras.datasets.fashion_mnist
(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

#%% Data preprocessing
train_images_pp = train_images / 255.0
test_images_pp = test_images / 255.0
train_labels_pp = tf.keras.utils.to_categorical(train_labels, num_classes=10)
test_labels_pp = tf.keras.utils.to_categorical(test_labels, num_classes=10)

#%% Build the FFNN model
model = tf.keras.Sequential([
    tf.keras.layers.Flatten(input_shape=(28, 28)),
    tf.keras.layers.Dense(128, activation='relu'),
    tf.keras.layers.Dense(10),
    tf.keras.layers.Softmax()
])

model.compile(optimizer='adam',
              loss=tf.keras.losses.CategoricalCrossentropy(from_logits=False),
              metrics=['accuracy'])

#%% Train the model
model.fit(train_images_pp, train_labels_pp, epochs=10)

#%% Test the model
test_loss, test_acc = model.evaluate(test_images_pp, test_labels_pp)
print('\nTest accuracy:', test_acc)

#%% Predict the output
predictions = model.predict(test_images_pp)

#%% Plot the data
fig, axes = plt.subplots(5, 5, figsize=(10,10))
for i in range(5):
    for j in range(5):
        ax = axes[i,j]
        ax.imshow(test_images[5*i+j])
        ax.set_title("True: " + class_names[test_labels[5*i+j]] +
                     "\nPred: " + class_names[np.argmax(predictions[5*i+j])])

plt.tight_layout()









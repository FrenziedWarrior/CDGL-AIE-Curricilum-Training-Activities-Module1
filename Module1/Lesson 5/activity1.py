import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# This line loads the MNIST dataset using TensorFlow’s built-in method. 
# The MNIST dataset consists of 28x28 grayscale images of handwritten digits (0-9) 
# along with the corresponding labels.
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()


# Normalizing the data
x_train, x_test = x_train / 255.0, x_test / 255.0


# Builds a sequential model using Keras.
model = models.Sequential([
    layers.Flatten(input_shape=(28,28)),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])


# Model configuration step
model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)


# Train the model
model.fit(x_train, y_train, epochs=5)


# Evaluate the model
test_loss, test_acc = model.evaluate(x_test, y_test)
print(f"Test accuracy: {test_acc}")


# Make predictions
predictions = model.predict(x_test)


# Display the first image and prediction
plt.imshow(x_test[0], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[0].argmax()}")
plt.show()
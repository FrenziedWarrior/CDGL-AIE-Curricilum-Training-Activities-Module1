# STEP 1: Import libraries
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt

# STEP 2: Load MNIST Dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

# STEP 3: Normalize the data
x_train, x_test = x_train / 255.0, x_test / 255.0


# STEP 4: Build the model
model = models.Sequential([
    layers.Flatten(input_shape=(28, 28)),
    layers.Dense(128, activation="relu"),
    layers.Dense(10, activation="softmax")
])

# STEP 5: Compile the model
model.compile(
    optimizer="adam",
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)


# STEP 6: Train the model
model.fit(x_train, y_train, epochs=5)


# STEP 7: Evaluate the model
# Let's say the passing marks in an exam is 30, you got 90 and I got 40.
# We both passed - We're both Accurately PASS
# But our Loss is different - You're closer to 100 than me. I need to tweak my performance more than you.
test_loss, test_acc = model.evaluate(x_test, y_test)


# STEP 8: Make predictions
predictions = model.predict(x_test)


# STEP 9: Display ANY test image and the model's prediction for it
i = 0
plt.imshow(x_test[i], cmap=plt.cm.binary)
plt.title(f"Predicted: {predictions[i].argmax()}")
plt.show()
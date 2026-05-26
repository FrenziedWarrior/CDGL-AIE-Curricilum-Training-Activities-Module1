# STEP 1: Import libraries
import tensorflow as tf
from tensorflow.keras import layers, models
import matplotlib.pyplot as plt
import numpy as np

# STEP 2: Load MNIST Dataset
(x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

def print_raw_digit(digit):
    for pixels in digit:
        for p in pixels:
            print("." if p == 0 else p, end=" ")
        print()

print_raw_digit(x_train[19])



# # STEP 3: Normalize the data
# x_train, x_test = x_train/255.0, x_test/255.0


# # STEP 4: Build the model
# model = models.Sequential([
#     layers.Flatten(input_shape=(28, 28)),
#     layers.Dense(128, activation="relu"),
#     layers.Dense(10, activation="softmax")
# ])


# # STEP 5: Compile the model
# model.compile(
#     optimizer="adam",
#     loss="sparse_categorical_crossentropy",
#     metrics=["accuracy"]
# )


# # STEP 6: Train the model
# model.fit(x_train, y_train, epochs=5)


# # STEP 7: Evaluate the model
# test_loss, test_acc = model.evaluate(x_test, y_test)
# print(f"Test accuracy: {test_acc}, {test_loss}")

# # Let's say the passing marks in an exam is 30, you got 90 and I got 40.
# # We both passed - We're both Accurately PASS
# # But our Loss is different - You're closer to 100 than me. I need to tweak my performance more than you.


# # STEP 8: Make predictions
# predictions = model.predict(x_test)


# # STEP 9: Display ANY test image and the model's prediction for it
# test_index = 578
# plt.imshow(x_test[test_index], cmap=plt.cm.binary)
# plt.title(f"Predicted: {predictions[test_index].argmax()}")
# plt.show()


# STEP 10: WHERE DID IT GO WRONG?
# 1. Convert raw probabilities to hard digit guesses (0 to 9)
predicted_labels = np.argmax(predictions, axis=1)

# 2. Handle True Labels 
# If your y_test is one-hot encoded (e.g., [0,0,0,1,0...]), convert it back to integers.
# If your y_test is already integers (0-9), you can just use: true_labels = y_test
true_labels = np.argmax(y_test, axis=1) if len(y_test.shape) > 1 else y_test

# 3. Find indices where the prediction does NOT match the true label
misclassified_indices = np.where(predicted_labels != true_labels)[0]

# 4. Print out a quick summary
print(f"Total misclassified digits: {len(misclassified_indices)} out of {len(x_test)}")

# Let's look at the first 3 mistakes the model made
for i in misclassified_indices[:3]:
    print(f"Image Index: {i}")
    print(f"  True Label:      {true_labels[i]}")
    print(f"  Model's Guess:   {predicted_labels[i]}")
    
    # Optional: Display the image using Matplotlib
    # (Reshaping back to 28x28 in case your model flattened it to 784)
    plt.imshow(x_test[i].reshape(28, 28), cmap='gray')
    plt.title(f"True: {true_labels[i]}, Predicted: {predicted_labels[i]}")
    plt.show()
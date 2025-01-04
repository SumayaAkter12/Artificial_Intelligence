#Write a Python program to display values of y when 'x' is an independent variable having values [-10, 10, step_size = 0.1] and:

#y = g3(f3(v)) where f3(v) = w3y1 + w4y2 + b, w = f3(v), and g3(w) = 1/ (1 + e^(-w))

import numpy as np
import matplotlib.pyplot as plt

# Constants for the linear combination function f3(v) = w3 * y1 + w4 * y2 + b
w3 = 1   # Weight for y1 (can change)
w4 = 1   # Weight for y2 (can change)
b = 0    # Bias (can change)

# Define the sigmoid function g3(w) = 1 / (1 + e^(-w))
def g3(w):
    return 1 / (1 + np.exp(-w))

# Define the sigmoid function (used for y1 and y2)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Generate values for x from -10 to 10 with step size 0.1
x = np.arange(-10, 10.1, 0.1)

# Calculate y1 and y2 using the sigmoid function
y1 = sigmoid(x)  # y1 = sigmoid(x)
y2 = sigmoid(x)  # y2 = sigmoid(x) (can be modified to different function if needed)

# Compute f3(v) = w3 * y1 + w4 * y2 + b
f3_v = w3 * y1 + w4 * y2 + b

# Compute y = g3(f3(v))
y = g3(f3_v)

# Display results for x and y
for xi, yi in zip(x, y):
    print(f"x: {xi:.1f}, y: {yi:.5f}")

# Plot the result
plt.plot(x, y, label=r"$y = g_3(f_3(v)) = \frac{1}{1 + e^{-f_3(v)}}$", color="purple")
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"Plot of $y = g_3(f_3(v)) = \frac{1}{1 + e^{-f_3(v)}}$")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")  # x-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")  # y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

#Write a Python program to display values of y when 'x' is an independent variable having values [-10, 10, step_size = 0.1] and:

#y1 = g1(f1(x)) where f1(x) = w1x + b1, u1 = f1(x), and g1(u1) = 1/ (1 + e^(-u1))

import numpy as np
import matplotlib.pyplot as plt

# Constants for the linear function f1(x) = w1 * x + b1
w = float(input("Enter the value for w (constant): "))
b = float(input("Enter the value for b (constant): "))

# Define the linear function f1(x) = w1 * x + b1
def f1(x):
    return w * x + b

# Define the sigmoid function g1(u1) = 1 / (1 + e^(-u1))
def g1(u1):
    return 1 / (1 + np.exp(-u1))

# Generate values for x from -10 to 10 with step size 0.1
x = np.arange(-10, 10.1, 0.1)

# Compute f1(x) and then g1(f1(x)) to get y1
u1 = f1(x)  # Apply f1(x)
y1 = g1(u1)  # Apply g1(u1) to get y1


# Display results
for xi, yi in zip(x, y1):
    print(f"x: {xi:.1f}, y1: {yi:.5f}")

# Plot the result
plt.plot(x, y1, label=r"$y_1 = g_1(f_1(x)) = \frac{1}{1 + e^{-f_1(x)}}$", color="green")
plt.xlabel("x")
plt.ylabel("y1")
plt.title(r"Plot of $y_1 = g_1(f_1(x)) = \frac{1}{1 + e^{-f_1(x)}}$")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")  # x-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")  # y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

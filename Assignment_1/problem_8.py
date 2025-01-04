#Write a Python program to display values of y when 'x' is an independent variable having values [-10, 10, step_size = 0.1] and:

 #y2 = g2(f2(x)) where f2(x) = w2x + b2, u2 = f2(x), and g2(u2) = 1/ (1 + e^(-u2))

import numpy as np
import matplotlib.pyplot as plt

# Constants for the linear function f2(x) = w2 * x + b2
w = float(input("Enter the value for w (constant): "))
b = float(input("Enter the value for b (constant): "))

# Define the linear function f2(x) = w2 * x + b2
def f2(x):
    return w * x + b

# Define the sigmoid function g2(u2) = 1 / (1 + e^(-u2))
def g2(u2):
    return 1 / (1 + np.exp(-u2))

# Generate values for x from -10 to 10 with step size 0.1
x = np.arange(-10, 10.1, 0.1)

# Compute f2(x) and then g2(f2(x)) to get y2
u2 = f2(x)  # Apply f2(x)
y2 = g2(u2)  # Apply g2(u2) to get y2

# Display results
for xi, yi in zip(x, y2):
    print(f"x: {xi:.1f}, y2: {yi:.5f}")

# Plot the result
plt.plot(x, y2, label=r"$y_2 = g_2(f_2(x)) = \frac{1}{1 + e^{-f_2(x)}}$", color="blue")
plt.xlabel("x")
plt.ylabel("y2")
plt.title(r"Plot of $y_2 = g_2(f_2(x)) = \frac{1}{1 + e^{-f_2(x)}}$")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")  # x-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")  # y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

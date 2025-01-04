#Write a Python program to display values of y when 'x' is an independent variable having values [-10, 10, step_size = 0.1] and:

#y = g(f(x)) where u = f(x) = wx + b and y = g(u) = 1/ (1 + e^(-u))

import numpy as np
import matplotlib.pyplot as plt

# Constants for the linear function f(x) = wx + b
w = float(input("Enter the value for w (constant): "))
b = float(input("Enter the value for b (constant): "))

# Define the function f(x) = wx + b
def f(x):
    return w * x + b

# Define the function g(u) = 1 / (1 + e^(-u))
def g(u):
    return 1 / (1 + np.exp(-u))

# Generate values for x from -10 to 10 with step size 0.1
x = np.arange(-10, 10.1, 0.1)

# Compute f(x) and then g(f(x)) to get y
u = f(x)  # Apply f(x)
y = g(u)  # Apply g(u) to get y

# Display results
for xi, yi in zip(x, y):
    print(f"x: {xi:.1f}, y: {yi:.5f}")

# Plot the result
plt.plot(x, y, label=r"$y = g(f(x)) = \frac{1}{1 + e^{-f(x)}}$", color="green")
plt.xlabel("x")
plt.ylabel("y")
plt.title(r"Plot of $y = g(f(x)) = \frac{1}{1 + e^{-f(x)}}$")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")  # x-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")  # y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

#Write a Python program to display values of y when 'x' is an independent variable having values [-10, 10, step_size = 0.1] and:
#y = 1/ (1 + e^(-x)); where ^ means 'to the power

import numpy as np
import matplotlib.pyplot as plt

# Generate values for x
x = np.arange(-10, 10.1, 0.1)  # Step size is 0.1

# Calculate y = 1 / (1 + e^(-x))
y = 1 / (1 + np.exp(-x))

# Display results
for xi, yi in zip(x, y):
    print(f"x: {xi:.1f}, y: {yi:.5f}")

# Optional: Plotting the results
plt.plot(x, y, label="y = 1 / (1 + e^(-x))", color="green")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sigmoid Function")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

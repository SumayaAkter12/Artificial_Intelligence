
#Write a Python program to display values of y when 'x' is an independent variable having values [-10, 10, step_size = 0.1] and:
#y = x^2

import numpy as np
import matplotlib.pyplot as plt

# Generate values for x
x = np.arange(-10, 10.1, 0.1)  # Step size is 0.1

# Calculate y = x^2
y = x**2

# Display results
for xi, yi in zip(x, y):
    print(f"x: {xi:.1f}, y: {yi:.2f}")

# Optional: Plotting the results
plt.plot(x, y, label="y = x^2", color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Quadratic Function: y = x^2")
plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()
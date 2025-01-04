#rite a Python program to display values of y when 'x' is an independent variable having values [-10, 10, step_size = 0.1] and:
#y = wx + b; where 'w' and 'b' are constants

import numpy as np
import matplotlib.pyplot as plt

# Constants
w = float(input("Enter the value for w (constant): "))
b = float(input("Enter the value for b (constant): "))
#w = 2  # Set the value of w
#b = 5  # Set the value of b

# Generate values for x
x = np.arange(-10, 10.1, 0.1)  # Step size is 0.1

# Calculate y
y = w * x + b

# Display results
for xi, yi in zip(x, y):
    print(f"x: {xi:.1f}, y: {yi:.1f}")

# Optional: Plotting the results
plt.plot(x, y, label=f"y = {w}x + {b}")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Linear Function: y = wx + b")
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(color = 'gray', linestyle = '--', linewidth = 0.5)
plt.legend()
plt.show()

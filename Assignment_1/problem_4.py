
#Write a Python program to display values of y when 'x' is an independent variable having values [-10, 10, step_size = 0.1] and:
#y = (e^x - e^(-x)) / (e^x - e^(-x))
import numpy as np
import matplotlib.pyplot as plt

# Generate values for x
x = np.arange(-10, 10.1, 0.1)  # Step size is 0.1

# Calculate y = (e^x - e^(-x)) / (e^x - e^(-x))
numerator = np.exp(x) - np.exp(-x)
denominator = np.exp(x) - np.exp(-x)
y = numerator / denominator

# Display results
for xi, yi in zip(x, y):
    print(f"x: {xi:.1f}, y: {yi:.1f}")

# Plot the result
plt.plot(x, y, label="y = (e^x - e^(-x)) / (e^x - e^(-x))", color="blue")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Plot of y = (e^x - e^(-x)) / (e^x - e^(-x))")
plt.axhline(0, color='black', linewidth=0.5, linestyle="--")  # x-axis
plt.axvline(0, color='black', linewidth=0.5, linestyle="--")  # y-axis
plt.grid(color='gray', linestyle='--', linewidth=0.5)
plt.legend()
plt.show()

    

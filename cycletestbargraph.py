import numpy as np
import matplotlib.pyplot as plt

# List of marks
marks = [78, 85, 92, 68, 75, 81]

# Calculate quartiles
q1, median, q3 = np.percentile(marks, [25, 50, 75])
minimum, maximum = min(marks), max(marks)

# X-axis categories
categories = ["Cycle Test 1", "Cycle Test 2", "Cycle Test 3", "Cycle Test 4", "Cycle Test 5", "Cycle Test 6"]

# Create a bar plot
plt.bar(categories, marks)

# Set the title and axis labels
plt.title("Marks scored in cycle tests")
plt.xlabel("Cycle tests")
plt.ylabel("Marks")

# Add quartile lines
plt.axhline(y=q1, color='r', linestyle='--')
plt.axhline(y=median, color='g', linestyle='--')
plt.axhline(y=q3, color='r', linestyle='--')

# Display the plot
plt.show()

# Print statistics
print("Minimum: ", minimum)
print("First quartile: ", q1)
print("Median: ", median)
print("Third quartile: ", q3)
print("Maximum: ", maximum)

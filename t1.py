# LIBS

import matplotlib.pyplot as plt
import matplotlib
import numpy as np
matplotlib.use('TkAgg')

#=================
# MAIN
#=================


# Your data points
x = [1, 2, 3, 4, 5]
y = [2, 4, 5, 4, 5]

# Perform linear regression with polyfit
m, b, c = np.polyfit(x, y, 2)  # 1 for linear regression

# Create the regression line function
regression_line = np.poly1d([m, b, c])

# Plot the scatter points
plt.scatter(x, y)

# Plot the regression line
plt.plot(x, regression_line(x))

# Label and title the plot
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Scatter Plot with Regression Line")

# Show the plot
plt.show()

# plottask.py
# Plot normal distribution and cube function
# Author: Colleen King
import matplotlib.pyplot as plt

# Get random from the numpy package to generate normally distributed random numbers
# https://www.w3schools.com/python/numpy/numpy_random_normal.asp#:~:text=Use%20the%20random.normal(),the%20graph%20distribution%20should%20be.
import numpy as np

normal_data = np.random.normal(loc=5, scale=2, size=1000)

# plot a histogram
# https://www.w3schools.com/python/matplotlib_histograms.asp
#
# Add lables and title to plot
# https://www.w3schools.com/python/matplotlib_labels.asp
#
# Save the plot to a file
# https://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it
# 
# add a theme to make the plot look nicer
# https://matplotlib.org/stable/gallery/style_sheets/style_sheets_reference.html
#
# add a legend
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html
plt.style.use("ggplot")
plt.hist(normal_data, color='lightblue', label='Count')
plt.title("Normal Distribution N(5, 2)")
plt.ylabel("Count")
plt.legend()
plt.savefig("plots/normal.png")
plt.show()
plt.close()


# plot a function x**3 between 0 and 10
# use numpy to get x points between 0 and 10, cube those points to get y values, then plot them
# https://stackoverflow.com/questions/72501910/how-to-create-a-graph-of-function-in-matplotlib
#
# Display superscript 3 instead of x**3
# https://stackoverflow.com/questions/21226868/superscript-in-python-plots
x_points = np.linspace(0, 10, 1000)
y_points = x_points**3

plt.plot(x_points, y_points, color='lightblue', label='x$^3$')
plt.title("Graph of h(x) = x$^3$")
plt.xlabel("x")
plt.ylabel("x$^3$")
plt.legend()
plt.savefig("plots/cubed.png")
plt.show()
plt.close()
import matplotlib.pyplot as plt
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([2, 3, 5, 7, 11])

plt.plot(x, y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Basic Plot")
# Save the plot as a PNG file
plt.savefig("basic_plot.png")
# Save the plot as a PDF file
plt.savefig("basic_plot.pdf")
# Save the plot as a SVG file
plt.savefig("basic_plot.svg")
# supported formats: eps, jpeg, jpg, pdf, pgf, png, ps, raw, rgba, svg, svgz, tif, tiff, webp

plt.show()  # Display the plot
plt.close()
# Note: plt.savefig() should be called before plt.show() to ensure the plot is saved correctly.
# plt.close() is used to close the plot and free up memory.

year = [1950, 1970, 1990, 2010]
pop = [2.519, 3.692, 5.263, 6.972]
plt.plot(year, pop)
plt.show()
plt.close()

# Scatter plot
plt.scatter(year, pop)
plt.show()
plt.close()

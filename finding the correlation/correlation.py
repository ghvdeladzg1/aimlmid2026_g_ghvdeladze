import numpy as np
import matplotlib.pyplot as plt

points = [
    (-9, 6),
    (-7.4, 5),
    (-5, 3),
    (-3, 4),
    (-1, 1),
    (1, 0),
    (3, -2),
    (5, -3),
    (7, -4),
    (9, -5)
]

x = np.array([p[0] for p in points])
y = np.array([p[1] for p in points])

r = np.corrcoef(x, y)[0, 1]
print("Pearson correlation coefficient r =", r)

# regression line
m, b = np.polyfit(x, y, 1)
y_line = m * x + b

plt.scatter(x, y, label="Data points")
plt.plot(x, y_line, label="Trend line")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.title("Scatter plot with trend line")
plt.legend()
plt.grid(True)
plt.savefig("correlation_plot.png")
plt.show()

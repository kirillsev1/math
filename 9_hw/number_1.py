import numpy as np
from polynoms import create_plot

if __name__ == "__main__":
    x = [1800, 1850, 1900, 2000]
    y = [280, 283, 291, 370]
    x_graph = np.linspace(min(x), max(x), 1000)
    x_label, y_label = "Год", "Содержание CO2"
    create_plot(x, y, x_graph, x_label, y_label, "number_1")

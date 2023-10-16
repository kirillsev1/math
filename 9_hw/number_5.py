from polynoms import create_plot
import numpy as np

if __name__ == "__main__":
    x = [1994, 1995, 1996, 1997]
    y = [67.052, 68.008, 69.803, 72.024]
    x_graph = np.linspace(1994, 1998, 100)
    x_label, y_label = "Год", "Bbl/day(x10^6)"
    last_value = create_plot(x, y, x_graph, x_label, y_label, "number_5")
    print(last_value)

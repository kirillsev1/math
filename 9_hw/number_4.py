from polynoms import create_plot
import numpy as np

if __name__ == "__main__":
    x = [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003]
    y = [67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777]
    x_graph = np.linspace(1994, 2010, 100)
    x_label, y_label = "Год", "Bbl/day(x10^6)"
    last_value = create_plot(x, y, x_graph, x_label, y_label, "number_4")
    print(last_value)

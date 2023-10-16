from polynoms import create_plot
import numpy as np

if __name__ == "__main__":
    x = [1970, 1990]
    y = [3707475887, 5281653820]
    x_graph = np.linspace(min(x), max(x), 1000)
    x_label, y_label = "Год", "Численность населения"
    result = create_plot(x, y, x_graph, x_label, y_label, "number_2a")
    print(f"a) 4 494 564 854: {result}\n")

    x = [1960, 1970, 1990]
    y = [3039585530, 3707475887, 5281653820]
    x_graph = np.linspace(min(x), max(x), 1000)
    x_label, y_label = "Год", "Численность населения"
    result = create_plot(x, y, x_graph, x_label, y_label, "number_2b")
    print(f"b) 4 454 831 984: {result}\n")

    x = [1960, 1970, 1990, 2000]
    y = [3039585530, 3707475887, 5281653820, 6079603571]
    x_graph = np.linspace(min(x), max(x), 1000)
    x_label, y_label = "Год", "Численность населения"
    result = create_plot(x, y, x_graph, x_label, y_label, "graph_9_2c")
    print(f"c) 4 472 888 288: {result}")


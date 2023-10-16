import numpy as np
from polynoms import create_graph

if __name__ == '__main__':
    x = [1800, 1850, 1900, 2000]
    y = [280, 283, 291, 370]
    x_graph = np.linspace(min(x), max(x), 1000)
    x_label, y_label = 'Год', 'Содержание CO2'
    create_graph(x, y, x_graph, x_label, y_label, 'graph_9_1')

    print('-- 2 --')
    x = [1970, 1990]
    y = [3707475887, 5281653820]
    x_graph = np.linspace(min(x), max(x), 1000)
    x_label, y_label = 'Год', 'Численность населения'
    create_graph(x, y, x_graph, x_label, y_label, 'graph_9_2a')
    print('Примерная численность населения в 1980 году по графику: 4 494 564 854', end='\n\n')

    x = [1960, 1970, 1990]
    y = [3039585530, 3707475887, 5281653820]
    x_graph = np.linspace(min(x), max(x), 1000)
    x_label, y_label = 'Год', 'Численность населения'
    create_graph(x, y, x_graph, x_label, y_label, 'graph_9_2b')
    print('Примерная численность населения в 1980 году по графику: 4 454 831 984', end='\n\n')

    x = [1960, 1970, 1990, 2000]
    y = [3039585530, 3707475887, 5281653820, 6079603571]
    x_graph = np.linspace(min(x), max(x), 1000)
    x_label, y_label = 'Год', 'Численность населения'
    create_graph(x, y, x_graph, x_label, y_label, 'graph_9_2c')
    print('Примерная численность населения в 1980 году по графику: 4 472 888 288', end='\n\n')

    print('Известное население в 1980 году: 4 452 584 592', end='\n\n')

    print('-- 3 --')
    x = np.linspace(0, np.pi / 2, 4)
    y = np.sin(x)
    x_graph = np.linspace(-2 * np.pi, 2 * np.pi, 1000)
    x_label, y_label = 'x', 'y'
    create_graph(x, y, x_graph, x_label, y_label, 'graph_9_3', 3)

    print('-- 4 --')
    x = [1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003]
    y = [67.052, 68.008, 69.803, 72.024, 73.400, 72.063, 74.669, 74.487, 74.065, 76.777]
    x_graph = np.linspace(1994, 2010, 100)
    x_label, y_label = 'Год', 'Bbl/day(x10^6)'
    last_value = create_graph(x, y, x_graph, x_label, y_label, 'graph_9_4')
    print(f'Оценочное кол-во добываемой нефти в 2010 году: {last_value}', end='\n\n')
    print(
        """
        В данном случае происходит интерполяция полинома довольно высокой степени.
        Из-за этого на конце графика можно заметить нежелательню осциляцию.
        Даже по графику можно заметить, что интерполирующщий полином
        не совсем корректно моделирует приведенные данные из-за аппроксимации.
        Для подобных прогнозов лучше использовать экономические модели.
        """
    )

    print('-- 5 --')
    x = [1994, 1995, 1996, 1997]
    y = [67.052, 68.008, 69.803, 72.024]
    x_graph = np.linspace(1994, 1998, 100)
    x_label, y_label = 'Год', 'Bbl/day(x10^6)'
    # last_value = create_graph(x, y, x_graph, x_label, y_label, 'graph_9_5')
    print(f'Оценочное кол-во добываемой нефти в 1998 году: {last_value}', end='\n\n')
    print(
        """
        Так как степень полинома не очень высока, феномен Рунге проявляется не так сильно
        и аппроксимированное значение близко к реальному.
        """
    )

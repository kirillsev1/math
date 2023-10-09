import matplotlib.pyplot as plt

years = [1960, 1970, 1990, 2000]
population = [3039585530, 3707475887, 5281653820, 6079603571]

year_to_estimate = 1980

population_linear = population[1] + (population[2] - population[1]) / (years[2] - years[1]) * (
            year_to_estimate - years[1])

a = (population[0] + population[2]) / 2
b = (population[1] - population[0]) / (years[1] - years[0])
c = (population[2] - a) / ((years[2] - years[0]) ** 2)
population_quadratic = a + b * (year_to_estimate - years[0]) + c * (year_to_estimate - years[0]) ** 2


def cubic_interpolation(x, x_data, y_data):
    n = len(x_data)
    for i in range(n - 1):
        if x_data[i] <= x <= x_data[i + 1]:
            h = x_data[i + 1] - x_data[i]
            t = (x - x_data[i]) / h
            y = (1 - t) * (1 - t) * (1 - t) * y_data[i] + t * (1 - t) * (1 - t) * y_data[i + 1] + t * t * (1 - t) * (
                        (y_data[i + 1] - y_data[i]) / h) + t * t * t * ((y_data[i + 1] - y_data[i]) / h)
            return y


population_cubic = cubic_interpolation(year_to_estimate, years, population)

plt.figure(figsize=(10, 6))
plt.plot(years, population, marker='o', label="Исходные данные")
plt.scatter(year_to_estimate, population_linear, color='red', label="Оценка (а)")
plt.scatter(year_to_estimate, population_quadratic, color='green', label="Оценка (б)")
plt.scatter(year_to_estimate, population_cubic, color='blue', label="Оценка (в)")
plt.xlabel('Год')
plt.ylabel('Численность населения')
plt.title('Оценка населения в 1980 году')
plt.legend()
plt.grid(True)
plt.show()

def simpson_integration(func, a, b, n):
    h = (b - a) / n
    x = a
    integral = func(a) + func(b)

    for i in range(1, n):
        x += h
        if i % 2 == 0:
            integral += 2 * func(x)
        else:
            integral += 4 * func(x)

    integral *= h / 3
    return integral

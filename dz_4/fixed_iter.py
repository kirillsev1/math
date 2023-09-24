def fixed_iter(fun, initial, n):
    x = initial
    for i in range(n):
        x = fun(x)
    return x

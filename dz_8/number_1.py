def jacoby(diag_main, diag_upper, diag_lower, b, x0, eps, max_iteration):
    iteration = 0
    x = x0
    n = len(b)
    err = 1
    while iteration < max_iteration and err > eps:
        err = 0
        for i in range(n):
            xn = b[i]
            if i > 0:
                xn -= diag_upper[i - 1] * x[i - 1]
            if i < n - 1:
                xn -= diag_lower[i] * x[i + 1]
            xn = xn / diag_main[i]
            err = max(err, abs(xn - x[i]))
            x[i] = xn
        iteration += 1
    return x, err, iteration

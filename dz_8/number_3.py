def gauss_seidel(main_diag, upper_diag, lower_diag, b, x0, eps, max_iter):
    iteration = 0
    x = x0
    n = len(b)
    err = 1
    while iteration < max_iter and err > eps:
        err = 0
        for i in range(n):
            xi = b[i]
            if i > 0:
                xi -= lower_diag[i] * x[i - 1]
            if i < n - 1:
                xi -= upper_diag[i] * x[i + 1]
            xi *= 1.0 / main_diag[i]
            err = max(err, abs(xi - x[i]))
            x[i] = xi
        iteration += 1
    return x, err, iteration


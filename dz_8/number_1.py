def jacoby(lower_diag, main_diag, upper_diag, b, x0, eps, max_iter, x_exact):
    n = len(b)
    x = x0
    xn = x
    max_exact = max([abs(x) for x in x_exact])
    max_vector = max(b)
    for iteration in range(max_iter):
        rel_error = 0
        rev_error = 0
        for i in range(n):
            if i > 0:
                left_x_prev = lower_diag[i] * x[i - 1]
            else:
                left_x_prev = 0

            if i < n - 1:
                right_x = upper_diag[i] * x[i + 1]
            else:
                right_x = 0

            if i > 0:
                left_x = lower_diag[i] * xn[i - 1]
            else:
                left_x = 0
            xn[i] = (b[i] - left_x_prev - right_x) / main_diag[i]
            rel_error = max(abs(xn[i] - x_exact[i]) / max_exact, rel_error)
            rev_error = max(abs(xn[i] * main_diag[i] + left_x + right_x - b[i]) / max_vector, rev_error)
        x = xn
        if rel_error <= eps:
            break
    return x, iteration + 1, rel_error, rev_error

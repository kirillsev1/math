def tridiag_solve(n, c, a, b, r):
    x = [0] * n
    x[-1] = r[-1] / a[-1]

    for i in range(1, n):
        s = c[i] / a[i - 1]
        a[i] = a[i] - s * b[i - 1]
        r[i] = r[i] - s * r[i - 1]
    x[n - 1] = r[n - 1] / a[n - 1]
    for j in range(n - 1):
        i = n - 2 - j
        x[i] = (r[i] - b[i] * x[i + 1]) / a[i]
    return x


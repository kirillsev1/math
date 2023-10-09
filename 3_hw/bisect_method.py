def bisect(fun, inter, eps):
    a, b = inter
    fa = fun(a)
    fb = fun(b)
    if fa * fb > 0.:
        print("Bad interval [%f, %f]" % (a, b))
        print("Bad interval [%f, %f]" % (fa, fb))
        return 0.
    while (b - a) / 2 > eps:
        c = (b + a) / 2
        fc = fun(c)
        if fc == 0.:
            break
        if fa * fc < 0:
            b = c
            fb = fc
        else:
            a = c
            fa = fc
    return (b + a) / 2

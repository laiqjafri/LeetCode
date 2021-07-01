def area_under_the_curve(x1, x2, func, step=0.1):
    if x1 > x2:
        x1, x2 = x2, x1

    area = 0

    while x1 < x2:
        y1 = func(x1)
        y2 = func(x1 + step)
        area += ((step * func(x1)) + (step * ((y2 - y1) / 2)))
        x1 += step

    return area

print(area_under_the_curve(3, 7, lambda x: x * x, 0.001))

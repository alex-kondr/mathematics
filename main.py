month = 0
step = 1/36      # 01.01.2020 - 31.12.2022 -> 36 months
populate = 10    # * 1000


def func(x, y):
    return (3 * x + y) - y**2


def euler_method(x, y, h):
    return y + h * func(x, y)


def euler_start(x, y, h, number_of_iteration):
    for _ in range(number_of_iteration):
        y = euler_method(x, y, h)
        x += h

    return y * 1000


def runge_kutte(x, y, h):
    k1 = func(x, y)
    k2 = func(x+h/2, y+h*k1/2)
    k3 = func(x+h/2, y+h*k2/2)
    k4 = func(x+h, y+h*k3)
    return y + (h/6) * (k1 + 2 * k2 + 2 * k3 + k4)


def runge_kutte_start(x, y, h, number_of_iteration):
    for _ in range(number_of_iteration):
        y = runge_kutte(x, y, h)
        x += h

    return y * 1000


if __name__ == "__main__":
    print(f"Now 01.01.2020, populate={populate*1000}")
    number_of_month = int(input("After how many months to show the future population: "))

    populate_euler = euler_start(month, populate, step, number_of_month)
    print(f"Result by euler method: {populate_euler=}")
    populate_runge_kutte = runge_kutte_start(month, populate, step, number_of_month)
    print(f"Result by euler method: {populate_runge_kutte=}")

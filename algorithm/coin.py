def dimensions(kind):
    if kind == 1:
        return 1
    elif kind == 2:
        return 5
    elif kind == 3:
        return 10
    elif kind == 4:
        return 25
    elif kind == 5:
        return 50


def cc(amount, kinds):
    if amount == 0:
        return 1
    elif amount < 0 or kinds == 0:
        return 0
    else:
        return cc(amount, kinds - 1) + cc(amount - dimensions(kinds), kinds)


def count_change(amount):
    return cc(amount, 5)


print(count_change(10))

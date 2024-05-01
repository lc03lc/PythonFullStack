def login(fn):
    def inner(a, b):
        r = fn(a, b)
        return r

    return inner


@login
def sum_num(a, b):
    result = a + b
    return result


s = sum_num(1, 2)
print(s)

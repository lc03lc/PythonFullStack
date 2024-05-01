def login(fn):
    def inner(*args, **kwargs):
        r = fn(*args, **kwargs)
        return r

    return inner


@login
def sum_num(*args, **kwargs):
    print(args, kwargs)


sum_num(1, 2, 3, age="18")

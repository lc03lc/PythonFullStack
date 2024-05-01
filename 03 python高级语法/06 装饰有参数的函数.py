def login(fn):
    def inner(a, b):
        fn(a, b)
    return inner

@login
def sum_num(a, b):
    result = a + b
    print(result)


sum_num(1, 2)

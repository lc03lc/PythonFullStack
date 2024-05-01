def login(flag):
    def decorator(fn):
        def inner(num1, num2):
            if flag == '+':
                print("加法运算")
            elif flag == "-":
                print("减法运算")
            result = fn(num1, num2)
            return result

        return inner

    return decorator


@login('+')
def add(a, b):
    result = a + b
    return result


result = add(1, 3)
print(result)

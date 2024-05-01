def fb(num):
    a = 0
    b = 1
    for i in range(num):
        result = a
        a, b = b, a + b
        yield result


f = fb(5)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
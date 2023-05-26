def fibonacci(n):
    a, b = 1, 1
    result = []
    for i in range(n):
        result.append(a)
        a, b = b, a + b
    return result


print(fibonacci(10))
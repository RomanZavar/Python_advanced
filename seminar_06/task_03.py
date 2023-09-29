# Создайте функцию генератор чисел Фибоначчи




# def fibonachi(limit: int):
#     fibo = [0, 1]
#     while limit > 0:
#         yield fibo[-1]
#         fibo.append(fibo[-1] + fibo[-2])
#         limit -= 1


# for number in fibonchi(10):
#     print(number)



a = int(input('Give amount: '))
def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b
print(list(fib(a)))

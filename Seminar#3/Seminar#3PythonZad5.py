# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:

# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Задайте число:'))

def list_fib(num_fib):
  
    fib_list = [1] * (2 * num_fib + 1)
    fib_list[num_fib] = 0
    for i in range(num_fib + 2, len(fib_list)):
        fib_list[i] = fib_list[i - 1] + fib_list[i - 2]
        fib_list[len(fib_list) - i - 1] = fib_list[i] * (-1) ** (i + 1)
    print(fib_list)


list_fib(num)
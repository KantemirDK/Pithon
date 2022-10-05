# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

def dec(num):
    num_bin = ''
    if num == 0:
        num_bin = '0'
    while num != 0:
        num_bin = str(num % 2) + num_bin
        num //= 2

    print(num_bin)
    
dec(45)
dec(3)
dec(2)
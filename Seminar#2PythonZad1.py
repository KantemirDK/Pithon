# Напишите программу, которая принимает на вход вещественное число и показывает 
# сумму его цифр. 
# Пример:
# 6782 -> 23
# 0,56 -> 11

def find_sum_dig_of_num():
    num = input('Введите целое или дробное число: ')
    SumDig = 0
    for el in range(len(num)):
        try:
            SumDig += int(num[el])
        except:
            pass
    return num, SumDig


num, sum_dig = find_sum_dig_of_num()
print(f'Сумма цифр в числе {num} = {sum_dig}')
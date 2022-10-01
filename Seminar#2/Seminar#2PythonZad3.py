# Задайте список из n чисел последовательности (1 + 1 / n) ** n и выведите 
# на экран их сумму.

# Пример:

# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

def make_list_subseq(n):
    listNum = []
    sum_el = 0
    for i in range(1, n + 1):
        num = (1 + 1 / i) ** i
        sum_el += num
        listNum.append(round(num, 4))
    return listNum, sum_el


listSubseq, SubseqSum = make_list_subseq(3)
print(f'Сумма элементов последовательности {listSubseq} = {round(SubseqSum, 4)}')
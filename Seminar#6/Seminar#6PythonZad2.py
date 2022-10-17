# 2 – Дана последовательность чисел. 
# Получить список уникальных элементов заданной последовательности, 
# список повторяемых и убрать дубликаты из заданной последовательности.

# Пример:
# [1, 2, 3, 5, 1, 5, 3, 10] => [2, 10] и [1, 3, 5] и [1, 2, 5, 3, 10]

def find_uniq(list):
   
    max_elem = max(list) + 1
    count = [0] * max_elem

    for element in list:
        count[element] += 1

    result = []
    for element in list:
        if count[element] == 1:
            result.append(element)
    return result


list_num = [1, 2, 3, 5, 1, 5, 3, 10]
print(list_num)

list_unq = find_uniq(list_num)
print(list_unq)

list_unq1 = [el for el in list_num if list_num.count(el) == 1]
print(list_unq1)
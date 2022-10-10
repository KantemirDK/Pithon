# Задайте натуральное число N. Напишите программу, которая составит список
# простых множителей числа N.

def find_list(n):

    simpl_num_list(abs(n))
    list_div_n = []
    file = open('simp_num', 'r')
    div_simp = file.read().split()
    file.close()
    for el in div_simp:
        if n % int(el) == 0:
            list_div_n.append(el)

    print(f'Cписок простых множителей числа {n} --> {list_div_n}')


def simpl_num_list(num):
    try:
        file = open('simp_num', 'r')
    except:
        file = open('simp_num', 'w+').write("1 2 3")
        file = open('simp_num', 'r')

    simp_numbers = file.read().split()
    file.close()
    last_el = int(simp_numbers[len(simp_numbers) - 1])
    if num > last_el:
        for i in range(last_el + 1, abs(num) + 1):
            sim_num = find_simpl_num(i)
            if sim_num is not None:
                file = open('simp_num', 'a+')
                file.write(" " + str(sim_num))
                file.close()


def find_simpl_num(num):
    for i in range(2, abs(num)):
        if num % i == 0:
            return
    return num


find_list(1008)



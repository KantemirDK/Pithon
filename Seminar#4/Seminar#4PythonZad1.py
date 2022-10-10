# Вычислить число c заданной точностью d
# Пример:
# - при d = 0.001, π = 3.142,    10^(-1) ≤ d ≤10^(-10)

import math
def find (d):
    pi = 3
    count = 1
    while round(pi, d + 1) != round(math.pi, d + 1):
        pi += (-1)**(count + 1) * 4 / (2 * count * (2 * count + 1) * (2 * count + 2))
        count += 1

    return round(pi,d)
d = 10
pi = find (d)
print(f'Число π c заданной точностью {d} = {pi}')
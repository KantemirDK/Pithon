def inputCoordXandY(coorX = 0, coorY = 0):
    while coorX == 0 or coorY == 0:
        coorX = int(input('Введите координату X (X ≠ 0): '))
        coorY = int(input('Введите координату Y (Y ≠ 0): '))

    return coorX, coorY

def findQuarter(x, y):
    if x > 0 and y > 0:
        numQ = 1
    elif x < 0 and y > 0:
        numQ = 2
    elif x < 0 and y < 0:
        numQ = 3
    else:
        numQ = 4

    print(f"Точка находится в {numQ} - четверти плоскости")

coorX, coorY = inputCoordXandY()

findQuarter(coorX, coorY)
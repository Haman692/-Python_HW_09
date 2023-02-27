from datetime import datetime

def mult(numberA, numberB):
    res = numberA * numberB
    with open('log.txt', 'a', encoding='utf=8')as file:
        file.writelines(str(datetime.now()) + ': ' + str(numberA) + ' * ' + str(numberB) + ' = ' + str(res) + '\n')
    return res
def div(numberA, numberB):
    res = numberA / numberB
    with open('log.txt', 'a', encoding='utf=8')as file:
        file.writelines(str(datetime.now()) + ': ' + str(numberA) + ' / ' + str(numberB) + ' = ' + str(res) + '\n')
    return res
def sum(numberA, numberB):
    res = numberA + numberB
    with open('log.txt', 'a', encoding='utf=8')as file:
        file.writelines(str(datetime.now()) + ': ' + str(numberA) + ' + ' + str(numberB) + ' = ' + str(res) + '\n')
    return res
def diff(numberA, numberB):
    res = numberA - numberB
    with open('log.txt', 'a', encoding='utf=8')as file:
        file.writelines(str(datetime.now()) + ': ' + str(numberA) + ' - ' + str(numberB) + ' = ' + str(res) + '\n')
    return res

while True:
    print('1. Умножение\n2. деление\n3. Сложение\n4. Вычетание')
    flag = int(input('Введиете действие: '))
    if 1 <= flag <= 4:
        break
    else:
        print('Неккоректный ввод, повторите')
if flag == 1:
    numbarA = int(input('Введите первое число: '))
    numberB = int(input('Введите второе число: '))
    print(str(numbarA) + ' * ' + str(numberB) + ' = ' + str(mult(numbarA, numberB)))
if flag == 2:
    numbarA = int(input('Введите первое число: '))
    numberB = int(input('Введите второе число: '))
    print(str(numbarA) + ' / ' + str(numberB) + ' = ' + str(div(numbarA, numberB)))
if flag == 3:
    numbarA = int(input('Введите первое число: '))
    numberB = int(input('Введите второе число: '))
    print(str(numbarA) + ' + ' + str(numberB) + ' = ' + str(sum(numbarA, numberB)))
if flag == 4:
    numbarA = int(input('Введите первое число: '))
    numberB = int(input('Введите второе число: '))
    print(str(numbarA) + ' - ' + str(numberB) + ' = ' + str(diff(numbarA, numberB)))


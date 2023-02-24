def print_matrix(matrix): #Вывод матрицы
    for i in matrix:
        print(''.join(i))

def find_position(number): #Поиск позиции по номеру
    matrix = [[1,2,3],
              [4,5,6],
              [7,8,9]]
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == number:
                return[i, j]

def x_or_y(matrix, position, player): # Ввод в матрицу X или O
    matrix[int(position[0])][int(position[1])] = '[' + player + ']'

def check_to_win(matrix):  #Проверка на победу
    for i in range(len(matrix)):
        if player == 'X':
            if matrix[i][0] == '[X]' and matrix[i][1] == '[X]' and matrix[i][2] == '[X]' :
                return True
            if matrix[0][i] == '[X]' and matrix[1][i] == '[X]' and matrix[2][i] == '[X]':
                return True
        if matrix[0][0] ==  '[X]' and matrix[1][1] == '[X]' and matrix[2][2] == '[X]':
            return True
        if matrix[0][2] == '[X]' and matrix[1][1] == '[X]' and matrix[2][0] == '[X]':
            return True
        if player == 'O':
            if matrix[i][0] == '[O]' and matrix[i][1] == '[O]' and matrix[i][2] == '[O]' :
                return True
            if matrix[0][i] == '[O]' and matrix[1][i] == '[O]' and matrix[2][i] == '[O]':
                return True
        if matrix[0][0] ==  '[O]' and matrix[1][1] == '[O]' and matrix[2][2] == '[O]':
            return True
        if matrix[0][2] == '[O]' and matrix[1][1] == '[O]' and matrix[2][0] == '[O]':
            return True

example_matrix = [['[1]','[2]','[3]'],
                  ['[4]','[5]','[6]'],
                  ['[7]','[8]','[9]']]
tic_tac = [['[ ]','[ ]','[ ]'],
           ['[ ]','[ ]','[ ]'],
           ['[ ]','[ ]','[ ]']]

print('ПРАВИЛА ИГРЫ:')
print('Два игрока поочереди набирают число, как показанно на примере нижуе, что бы поставить на эту позицию X ИЛИ O')
print_matrix(example_matrix)
print('START')
print_matrix(tic_tac)
player = 'X'
for i in range(9):
    if player == 'X':
        while True: # Проверка на верность ввода
            try:  
                cor = int(input('Поставить Х на посицию: '))
                if 1 <= cor <= 9 and tic_tac[find_position(cor)[0]][find_position(cor)[1]] == '[ ]':
                    break
                else:
                    print('Позиция уже занята, введите другую')
            except:
                print("Ошибка - это не число")
        position = find_position(cor)
        x_or_y(tic_tac, position, player)
        print_matrix(tic_tac)
        win = check_to_win(tic_tac)
        if win == True:
            print('X - Победитель')
            break
        player = 'O'
    elif player == 'O':
        while True: # Проверка на верность ввода
            try:  
                cor = int(input('Поставить O на посицию: '))
                if 1 <= cor <= 9 and tic_tac[find_position(cor)[0]][find_position(cor)[1]] == '[ ]':
                    break
                else:
                    print('Позиция уже занята, введите другую')
            except:
                print("Ошибка - это не число")
        position = find_position(cor)
        x_or_y(tic_tac, position, player)
        print_matrix(tic_tac)        
        win = check_to_win(tic_tac)
        if win == True:
            print('O - Победитель')
            break
        player = 'X'
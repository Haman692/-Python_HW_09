while True:
    print('1. Посмторет телефонную книгу\n2. Добавить запись')
    flag = int(input('Введите действие '))
    if 1 <= flag <= 2 :
        break
    else:
        print('Неккоректный ввод\n')
if flag == 1:
    with open('phone_book.txt', 'r', encoding='utf=8') as file:
        text = file.read()
        print(text)
if flag == 2:
    while True:
        print('1. Добавить другую телефонную книгу\n2. Добавить в ручную')
        flag = int(input('Введите действие '))
        if 1 <= flag <= 2 :
            break
        else:
            print('Неккоректный ввод\n')
    if flag == 1:
        path = str(input('Введите путь до файла '))
        open('phone_book.txt','a',encoding='utf=8').write('\n' + open(path,"r").read())
        file.close
    if flag == 2:
        name = str(input('Введиет ФИО'))
        number_tel = str(input('Введите телефон'))
        open('phone_book.txt','a',encoding='utf=8').write('\n' + name + ' - ' + number_tel)
        
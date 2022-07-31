import sys
def initial_phonebook():
    temp = []
    print('Чтобы начать предлагаем сохранить первый контакт\n')
    print('В случае если Вы не собираетесь сейчас ничего вводить, нажмите 0')
    phone_book = []
    rows = 1
    cols = 5
    for i in range(rows):
        print("ПРИМЕЧАНИЕ: * указывает на обязательные поля")
        print("....................................................................")
        
        for j in range(cols):
            if j == 0:
                temp.append(str(input("Введите Ф.И.О*: ")))
                if temp[j] == '' or temp[j] == ' ':
                    with open('HWPS7.csv', 'w') as file:
                        file.write(f'Ф.И.О: {temp.append}')
                    sys.exit("Имя является обязательным полем. Процесс прерывается из-за пустого поля...")
            if j == 1:
                temp.append(str(input("Введите номер*: "))) 
                if temp[j] == '' or temp[j] == ' ': 
                    with open('HWPS7.csv', 'w') as file:
                        file.write(f'Номер: {temp.append}')
                    sys.exit("Номер является обязательным полем. Процесс прерывается из-за пустого поля...") # при int удалить эту строку
            if j == 2:
                temp.append(str(input("Введите адрес электронной почты: ")))
            if j == 3:
                temp.append(str(input("Введите дату рождения (дд/мм/гг): ")))
# При поиске пользователь должен будет вводить запрос точно так же, как и
# он ввел во время ввода, чтобы обеспечить точный поиск
            if j == 4:
                temp.append(str(input("Введите категорию (Семья/Друзья/Работа/Другие): ")))
    phone_book.append(temp)
    print(phone_book)
    with open('HWPS7.csv', 'a', encoding='utf-8') as file:
        file.write(f"\nФ.И.О: {temp[0]}\nНомер: {temp[1]}\nАдрес электронной почты: {temp[2]}\nДата рождения : {temp[3]}\nКатегория: {temp[4]}\n")
    return phone_book

import display_all 
def search_existing(pb):
# Эта функция ищет существующий контакт и отображает результат
    choice = int(input("\nВведите критерии поиска\
    \n1. Имя\n2. Номер\n3. Идентификатор электронной почты\n4. Дата рождения\n5. Категория(Семья/Друзья/Работа/Другое)\
    \nПожалуйста, введите: "))
    temp = []
    check = -1
    if choice == 1:
    # Поиск по имени контакта
        query = str(
            input("Пожалуйста, введите имя контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append(pb[i])
    elif choice == 2:
    # Поиск по номеру контакта
        query = int(
            input("Пожалуйста, введите номер контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][1]:
                check = i
                temp.append(pb[i])
    elif choice == 3:
    # Поиск по адресу электронной почты контакта
        query = str(input("Пожалуйста, введите e-mail ID\
        контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][2]:
                check = i
                temp.append(pb[i])
    elif choice == 4:
    # Поиск по дате рождения контакта
        query = str(input("Пожалуйста, введите дату рождения (ТОЛЬКО в формате дд/мм/гггг)\
            контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][3]:
                check = i
                temp.append(pb[i])
    elif choice == 5:
    # Поиск по категории контакта
        query = str(
            input("\nПожалуйста, введите категорию контакта, который вы хотите найти: "))
        for i in range(len(pb)):
            if query == pb[i][4]:
                check = i
                temp.append(pb[i])
# С помощью этой функции будут показаны все контакты в категории запросов.
    else:
    # Если пользователь введет любой другой вариант, поиск будет неудачным.
        print("Неверные критерии поиска")
        return -1
    # возврат -1 означает, что поиск не увенчался успехом
    if check == -1:
        return -1
    # возвращение -1 указывает, что запрос не существует в каталоге
    else:
        display_all.display_all(temp)
        return check

 

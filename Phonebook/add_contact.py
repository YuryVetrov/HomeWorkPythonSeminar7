# Функция добавления контактов
def add_contact(pb):
# добавим еще один список деталей в уже существующий список
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Введите имя: ")))
        if i == 1:
            dip.append(int(input("Введите номер: ")))
        if i == 2:
            dip.append(str(input("Введите адрес электронной почты: ")))
        if i == 3:
            dip.append(str(input("Введите дату рождения (дд/мм/гг): ")))
        if i == 4:
            dip.append(
                str(input("Введите категорию (Семья/Друзья/Работа/Другие): ")))
    pb.append(dip)
    return pb
 
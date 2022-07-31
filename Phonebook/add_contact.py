# Функция добавления контактов
def add_contact(pb):
# добавим еще один список в уже существующий список
    dip = []
    for i in range(len(pb[0])):
        if i == 0:
            dip.append(str(input("Введите Ф.И.О*: ")))
        if i == 1:
            dip.append(str(input("Введите номер*: "))) 
        if i == 2:
            dip.append(str(input("Введите адрес электронной почты: ")))
        if i == 3:
            dip.append(str(input("Введите дату рождения (дд/мм/гг): ")))
        if i == 4:
            dip.append(str(input("Введите категорию (Семья/Друзья/Работа/Другие): ")))
    pb.append(dip)
    with open('HWPS7.csv', 'a', encoding='utf-8') as file:
        file.write(f"\nФ.И.О: {dip[0]}\nНомер: {dip[1]}\nАдрес электронной почты: {dip[2]}\nДата рождения : {dip[3]}\nКатегория: {dip[4]}\n")
    return pb

 
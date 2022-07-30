import initial_phonebook 
import menu
import add_contact
import remove_existing
import delete_all
import search_existing
import display_all
import thanks
# Код основной функции
print("....................................................................")
print("Привет, дорогой пользователь, добро пожаловать в наш телефонный справочник.")
print("....................................................................")
ch = 1
pb = initial_phonebook.initial_phonebook()
while ch in (1, 2, 3, 4, 5):
    ch = menu.menu()
    if ch == 1:
        pb = add_contact.add_contact(pb)
    elif ch == 2:
        pb = remove_existing.remove_existing(pb)
    elif ch == 3:
        pb = delete_all.delete_all(pb)
    elif ch == 4:
        d = search_existing.search_existing(pb)
        if d == -1:
            print("Контакт не существует. Пожалуйста, попробуйте еще раз")
    elif ch == 5:
        display_all.display_all(pb)
    else:
        thanks.thanks()

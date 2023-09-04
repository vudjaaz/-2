from random import *
import json

phone_book = {}

def save():
    with open("contact.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(phone_book, ensure_ascii=False))
    print("Контакт сохранен")
def load():
    with open("contact.json", "r", encoding="utf-8") as fh:
        phone_book = json.load(fh)
    return phone_book
    
# def delete_contact():
#     name = input('Введите имя или фамилию контакта, которого надо удалить:  ')
#     with open("contact.json", 'r', encoding='UTF-8') as fh:
#         phone_book = json.load(fh)
#         for i in range(0, len(phone_book)):
#             if name == phone_book[i]:
#                 del phone_book[i]
    

while True:
    command = input("Введите команду: ")
    if command == "/add":
        name = input("Введите имя нового контакта: ")
        surname = input("Введите фамилию нового контакта: ")
        number0 = input("Введите 1й номер: ")
        number1 = input("Введите 2й номер: ")
        bith_day = input("Введите ДР: ")
        mail = input("Введите email: ")
        phone_book[name] = {"phone_numbers": [number0, number1], "birth_day": bith_day, "email": mail}
        print("Контакт добавлен")
    elif command == "/all":
        print("Список всех контактов")
        print(phone_book)
    elif command == "/find":
        name = input("Введите имя для поиска: ")
        if name in phone_book:
            print(name, phone_book[name])
    elif command == "/save":
        save()
    elif command == "/load":
        phone_book = load()
        print("Загрузка контактов выполнена успешно")
    # elif command == "del":
    #     phone_book = delete_contact()
        print("Контакт успешно изменена удалён!")
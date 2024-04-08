def handle_command(command):
    argum = command.split()
    if argum[0] == "echo":
        strs = argum[1:]
        sr = ""
        for strv in strs:
            sr += f"{strv} "
        sr = sr[:-1]
        print(sr)
    elif argum[0] == "off" or argum[0] == "exit":
        return True  # Сигнал завершения программы
    elif argum[0] == "help":
        print("echo [Содержание] - вывод информации\noff или exit - выйти из ОС\nhelp - выход\nterms - условия изпользования\ncal (пример) - калькулятор")
    elif argum[0] == "terms":
        print("\n\nЛицензионное соглашение для операционной системы OSoPfPC:\n\n")
        print("Эта версия v.v.v является бета-версией и не предназначена для публичного использования.\n")
        print("МЕСТОИМЕННИЯ:\n")
        print("* Вы, ваши, вам - Пользователь\n")
        print("* Мы, наши, нам - Компания\n")
        print("\n\nУСЛОВИЯ ИЗПОЛЬЗОВАНИЯ:\n\n")
        print("1. Система НЕ ПЕРЕДАЁТ ВАШИ ДАННЫЕ третим лицам\n")
        print("2. Система НЕ ПЕРЕДАЁТ ВАШИ ДАННЫЕ нам\n")
        print("3. Эта система(OSoPfPC) ЯВЛЯЕТСЯ КОНСОЛЬНОЙ ОС\n")
        print("4. МЫ НЕ ПРОСИМ ЧТОТО ПОКУПАТЬ И Т.Д.\n")
        print("5. НАРУШЕНИЕ СОГЛАШЕНИЯ(Продажа товаров через ОС)  ЯВЛЯЕТСЯ УЖАСНЫМ ДЕЙСТВИЕМ\n")
        print("\n\nПОМОЩЬ ДЛЯ ПОЛЬЗОВАТЕЛЯ ПОСЛЕ УСТАНОВКИ:\n\n")
        print("help - все команды\nterms - условия(бета или публичное)\n")
        print("\n\nССЫЛКИ ЧТОБЫ ОБНОВИТСЯ И СКАЧАТЬ УСТАНОВЩИКИ И УСТАНОВИТЬ НОВЫЕ ОС:\n\n")
        print("https://t.me/OSoPfPC - наш телеграмм канал\n")
    elif argum[0] == "cal":
        if len(argum) > 1:
            i = ""
            ii = argum[1:]
            for t in ii:
                i += f"{t} "
            i[:-1]
            print(eval(i))
        else:
            print("Нету примера")
    else:
        print("Не верная команда")
    return False  # Сигнал продолжения работы программы

def main():
    while True:
        command = input("Ввод: ")
        if handle_command(command):
            break  # Завершаем цикл, если возвращено True

if __name__ == "__main__":
    main()

def handle_command(command):
    argum = command.split()
    if argum[0] == "echo":
        strs = argum[1:]
        sr = " ".join(strs)
        print(sr)
    elif argum[0] == "off" or argum[0] == "exit":
        return True  # Сигнал завершения программы
    elif argum[0] == "help":
        print("echo [Содержание] - вывод информации\noff или exit - выйти из ОС\nhelp - выход\nterms - условия изпользования\ncal (пример) - калькулятор\nwmol (1число) (2число)\nsplit (число) - раздел числа на сотни, десяток и единиц")
    elif argum[0] == "terms":
        print("\n\nЛицензионное соглашение для операционной системы OSoPfPC:\n\n")
        print("Эта версия 1.3 является бета-версией и не предназначена для публичного использования.\n")
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
            try:
                result = eval(" ".join(argum[1:]))
                print(result)
            except Exception as e:
                print("Ошибка:", e)
        else:
            print("Нет примера")
    elif argum[0] == "wmol":
        if len(argum) == 3:
            try:
                num1 = int(argum[1])
                num2 = int(argum[2])
                if num1 < num2:
                    print(f"{num1} < {num2}")
                elif num1 > num2:
                    print(f"{num1} > {num2}")
                else:
                    print(f"{num1} = {num2}")
            except ValueError:
                print("Ошибка: Введите целые числа для сравнения")
        else:
            print("Ошибка: Неверное количество аргументов для команды 'wmol'")
    elif argum[0] == "split":
        if len(argum) == 2:
            num = argum[1:]
            nums_str = ""
            for text in num:
                nums_str += text
            nums_str = nums_str[:-1]
            nums = list(nums_str)
            if len(nums) == 2:
                print(f"Сотней: {nums[0]}, Десяток: {nums[1]}, единиц: {nums[2]}")
            elif len(nums) == 1:
                print(f"Десяток: {nums[0]}, единиц: {nums[1]}")
            else:
                print("Ошибка: нужно больше цифр")
        else:
            print("Ошибка: Неверное количество аргументов для команды 'split'")
    else:
        print("Неизвестная команда")
    return False  # Сигнал продолжения работы программы

def main():
    while True:
        command = input("Ввод: ")
        if handle_command(command):
            break  # Завершаем цикл, если возвращено True

if __name__ == "__main__":
    main()

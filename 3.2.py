#                              2
# Создать текстовый файл (не программно). Построчно записать
# названия детских товаров и их стоимость (не менее 10 строк). Вывести на
# экран все товары, стоимость которых ниже 10 рублей. Вывести на экран все
# товары с минимальной стоимостью.
    # Пример файла:
    # Машинка 50
    # Кукла 40
import os

print("\033[3m\033[36m{}{}{}\033[0m".format("\n", " " * 8, "Задание 2\n"))
while True:
    if os.path.exists("File_3_2.txt"):
        toys = {}
        with open("File_3_2.txt", encoding="utf-8") as file_3_2:
            print("Данные из файла:")
            print(file_3_2.read(), '\n')
            file_3_2.seek(0)
            print("Стоимость ниже 10р:")
            for line in file_3_2.readlines():
                # print(line)
                name, amount = line.split(' ')
                # print(name, amount)
                toys[name] = amount.strip()
            # print(toys)
            min_v = int(toys[list(toys.keys())[0]])
            # print(min_v)
            for key, value in toys.items():
                if int(value) < 10:
                    print(key, ' - ', value)
                if int(value) < min_v:
                    min_v = int(value)
            print("\nМинимальная стоимость:", min_v)
            print()
            # print(min_v, type(min_v))
            for key, value in toys.items():
                if int(value) == min_v:
                    print(key, ' - ', value)
        break
    else:
        text = (
"""Машинка 50
Кукла 40
Раскраска 5
Пазл 8
Конструктор 45
Медведь 50
Карандаши 5
Сказки 9
Робот 50
Глобус 25
Поезд 30
Наклейки 5"""
        )
        # print("Нет файла.")
        with open("File_3_2.txt",'w', encoding="utf-8") as file_3_2:
            file_3_2.write(text)
#                              2
# Создать текстовый файл (не программно). Построчно записать
# названия детских товаров и их стоимость (не менее 10 строк). Вывести на
# экран все товары, стоимость которых ниже 10 рублей. Вывести на экран все
# товары с минимальной стоимостью.
    # Пример файла:
    # Машинка 50
    # Кукла 40
print("\033[3m\033[36m{}{}{}\033[0m".format("\n", " " * 8, "Задание 2\n"))
toys = {}
with open("File_3_2.txt", encoding="utf-8") as file_3_2:
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

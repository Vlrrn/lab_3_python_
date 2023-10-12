#                               1
# Создать программный файл F1 в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# будет свидетельствовать пустая строка. Скопировать из файла F1 в файл F2
# строки, начиная с четвертой по порядку. Подсчитать количество символов в
# последнем слове F2
print("\033[3m\033[36m{}{}{}\033[0m".format("\n", " " * 8, "Задание 1\n"))
with open("F1.txt", 'w+') as f1:
    counter = 0
    while True:
        i = 1
        dd = input("Введите данные для %.f строки: " % (counter + 1))
        f1.write(dd + "\n")
        counter += 1
        i += 1
        if dd == '':
            break
print("\033[3m\033[36m{}\033[0m".format(" " * 8, "\nВвод завершён!\n"))
if counter > 4:
    with open("F1.txt", 'r') as f1, open("F2.txt", 'w') as f2:
        l = 4
        count = -1
        for i, line in enumerate(f1, 1):
            if i == l:
                f2.write(line)
                l += 1
                count += 1
    with open("F2.txt", 'r') as f2:
        f2.seek(0)
        for i, line in enumerate(f2, 1):
            if i == count:
                last_line = line
                print("Последняя строка:", last_line)
        list_last_line = last_line.split()
        if list_last_line:
            last_word_in_list = list_last_line[-1]
            print("Последнее слово в строке: {}\nДлина слова = {}".format( last_word_in_list, len(last_word_in_list)))
        else:
            print("В последней строке нет слов")
else:
    print("\033[1m\033[31m{}\033[0m".format("Недостаточно элементов!"))
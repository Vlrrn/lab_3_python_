#                             3
# Сформировать (не программно) текстовый файл. В нём каждая
# строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету. Сюда должно входить и
# количество занятий. Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее
# количество занятий по нему. Вывести его на экран.
# Примеры строк файла:
#      Информатика: 100(л) 50(пр) 20(лаб).
#      Физика: 30(л) 10(лаб)
#      Физкультура: 30(пр)
# Пример словаря: {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
import os

print("\033[3m\033[36m{}{}{}\033[0m".format("\n", " " * 8, "Задание 3\n"))
while True:
    if os.path.exists("File_3_3.txt"):
        with open("File_3_3.txt", encoding="utf-8") as file_3_3:
            print("Данные из файла:")
            print(file_3_3.read())
            file_3_3.seek(0)
            print()
            s = {}
            for line in file_3_3.readlines():
                p, c = line.split(':')
                s[p] = c.strip()
            # print(s)
            print("Общее количество занятий по предметам:")
            for key, value in s.items():
                s1 = value.replace("(л)", '').replace("(пр)", '').replace("(лаб)", '').split()
                s2 = 0
                for el in s1:
                    s2 += int(el)
                s[key] = s2
                print(key, ' - ', s2)
            print("\nСловарь:", s)
        break
    else:
        text = (
"""Информатика: 100(л) 50(пр) 20(лаб)
Физика: 30(л) 10(лаб)
Физкультура: 30(пр)"""
        )
        # print("---")
        with open("File_3_3.txt", 'w', encoding="utf-8") as file_3_3:
            file_3_3.write(text)

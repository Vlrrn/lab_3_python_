#                                4
# Создать вручную и заполнить несколькими строками текстовый файл,
# в котором каждая строка будет содержать данные о фирме: название, форма собственности, выручка, издержки.
#   Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,а также среднюю прибыль.
# Если фирма получила убытки, в расчёт средней прибыли её не включать. Далее реализовать список.
# Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить её в словарь (со значением убытков).
#   Пример списка:  [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
#   Пример json-объекта: [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
import json
import os

print("\033[3m\033[36m{}{}{}\033[0m".format("\n", " " * 8, "Задание 4\n"))
while True:
    if os.path.exists("File_3_4.txt"):
        with open("File_3_4.txt", encoding="utf-8") as file_3_4:
            print(" " * 2, "Данные о фирмах:")
            print(file_3_4.read(), '\n')
            file_3_4.seek(0)
            s = {}
            s2 = {}
            list_ = []
            for line in file_3_4.readlines():
                st = line.split(' ')
                for el in st:
                    i = st.index(el)
                    el = el.replace("\n", '')
                    st[i] = el
                del st[1]
                money = int(st[1]) - int(st[2])
                name = st[0]
                s[name] = money
            # for key, value in s.items():
            #     print(key, ':', value)
            # print(s)
            n = 0
            c = 0
            for value in s.values():
                if int(value) > 0:
                    n += 1
                    c += int(value)
            k = "average_profit"
            v = c / n
            s2[k] = int(v)
            # print(s2)
            list_.append(s)
            list_.append(s2)
            print(" " * 2, "Словарь:")
            for e in list_:
                for key, value in e.items():
                    print(key, ':', value)
            # print(list_)
        print()
        with open("File.json", 'w') as file_json:
            json.dump(list_, file_json)
            print("json-объект:", json.dumps(list_))
        break
    else:
        text = (
"""firm_1 ООО 10000 5000
firm_2 ООО 1000 5000
firm_3 ООО 10000 4000
firm_4 ООО 15000 5000
firm_5 ООО 10000 5000
firm_6 ООО 10000 2000
firm_7 ООО 7000 5000"""
        )
        # print("---")
        with open("File_3_4.txt", 'w', encoding='utf-8') as file_3_4:
            file_3_4.write(text)

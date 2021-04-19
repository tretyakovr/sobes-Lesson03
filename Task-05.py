# Третьяков Роман Викторович
# Факультет Geek University Python-разработки
# Основы языка Python
# Урок 3
# Задание 5:
# Усовершенствовать первую функцию из предыдущего примера. Необходимо во втором списке
# часть строковых значений заменить на значения типа example345 (строка+число). Далее —
# усовершенствовать вторую функцию из предыдущего примера (функцию извлечения данных).
# Дополнительно реализовать поиск определенных подстрок в файле по следующим условиям:
# вывод первого вхождения, вывод всех вхождений. Реализовать замену всех найденных
# подстрок на новое значение и вывод всех подстрок, состоящих из букв и цифр и имеющих
# пробелы только в начале и конце — например, example345.

import os, re


def first_func():
    try:
        file_txt = open('data.txt', 'x')

    except FileExistsError:
        print('Файл уже существует!')

    else:
        simple_str = 'simple_str'
        list1 = [i for i in simple_str]
        list2 = []
        for i in range(len(simple_str)):
            if i % 2 == 0:
                list2.append(simple_str + ' str' + str(i ** 8) + ' ')
            else:
                list2.append(simple_str + ' str' + str(i * 8) + ' ')

        for i in zip(list1, list2):
            file_txt.write(f'{"".join(i)} \n')

        file_txt.close()

        second_func(file_txt)

def second_func(file_name):
    try:
        file_txt = open(os.path.abspath(file_name.name), 'r')

    except:
        print('Ошибка открытия файла!')

    else:
        substr = '7'
        new_substr = ' new_substr '

        for line_str in file_txt:
            line_str = line_str.split('\n')[0]
            print('Исходная строка: "' + line_str + '"')
            match = re.search(substr, line_str)
            if match is None:
                print(f'Нет вхождений подстроки "{substr}" в строку "{line_str}"')
            else:
                print(f'Первое вхождение подстроки "{substr}" в строку "{line_str}": ', match.start())
                print(f'Все вхождения подстроки "{substr}" в строку "{line_str}": ', [m.start() for m in re.finditer(substr, line_str)])

            print('Измененная строка: "' + re.sub(substr, new_substr, line_str) + '"')

            print('Подстроки исходной строки, состоящие из букв и цифр, обрамленные пробелами: ', re.findall(r'\b[a-z]+[0-9]+\b', line_str), '\n')


        file_txt.close()


first_func()
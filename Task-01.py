# Третьяков Роман Викторович
# Факультет Geek University Python-разработки
# Основы языка Python
# Урок 1
# Задание 1:
# Написать программу, которая будет содержать функцию для получения имени файла из
# полного пути до него. При вызове функции в качестве аргумента должно передаваться имя
# файла с расширением. В функции необходимо реализовать поиск полного пути по имени файла,
# а затем «выделение» из этого пути имени файла (без расширения).
import os


def get_parts_of_filename(filename):

    dir_name = os.path.dirname(filename)
    file_with_ext = os.path.basename(filename)
    (filename_only, ext_only) = os.path.splitext(file_with_ext)
    print(f'Полный путь к файлу: {dir_name}')
    print(f'Имя файла с расширением: {file_with_ext}')
    print(f'Имя файла без расширения: {filename_only}')


get_parts_of_filename('/Users/username/dir1/dir2/dir3/Lesson03/Task-01.py')

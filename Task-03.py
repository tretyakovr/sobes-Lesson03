# Третьяков Роман Викторович
# Факультет Geek University Python-разработки
# Основы языка Python
# Урок 3
# Задание 3:
# Создать два списка с различным количеством элементов. В первом должны быть записаны
# ключи, во втором — значения. Необходимо написать функцию, создающую из данных ключей
# и значений словарь. Если ключу не хватает значения, в словаре для него должно
# сохраняться значение None. Значения, которым не хватило ключей, необходимо отбросить.

def fill_dict(list1, list2):

    dict = {}

    for i in range(len(list1)):
        try:
            dict[list1[i]] = list2[i]
        except IndexError:
            dict[list1[i]] = None

    return dict

print(fill_dict([1, 2, 3, 4, 5, 6], ['a', 'b', 'c', 'd', 'e', 'f', 'g']))
print(fill_dict([1, 2, 3, 4, 5, 6], ['a', 'b', 'c', 'd', 'e']))


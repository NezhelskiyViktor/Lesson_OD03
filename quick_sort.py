# Определение функции quick_sort, которая принимает список s
def quick_sort(s):
    # Проверка, если длина списка меньше или равна 1
    if len(s) <= 1:
        return s  # Возврат списка, так как он уже отсортирован

    # Выбор первого элемента списка в качестве опорного
    element = s[0]

    # Создание списка left с элементами, меньшими опорного
    left = list(filter(lambda i: i < element, s))

    # Создание списка center с элементами, равными опорному
    center = [i for i in s if i == element]

    # Создание списка right с элементами, большими опорного
    right = list(filter(lambda i: i > element, s))

    # Рекурсивный вызов quick_sort для списков left и right,
    # объединение результатов
    return quick_sort(left) + center + quick_sort(right)


# Вызов функции quick_sort с заданным списком и вывод результата
print(quick_sort([5, 2, 9, 0, 1, 5, 3]))

# Определение функции insertion_sort, принимающей список arr
def insertion_sort(arr):
    # Внешний цикл, проходящий по всем элементам списка
    for i in range(1, len(arr)):
        # Сохранение текущего элемента в переменной key
        key = arr[i]
        # Инициализация переменной j, указывающей на индекс предыдущего элемента
        j = i - 1

        # Внутренний цикл, проходящий по оставшимся элементам списка
        while j >= 0 and arr[j] > key:
            # Перемещение элемента вправо, если он больше текущего
            arr[j + 1] = arr[j]
            # Уменьшение j для проверки следующего элемента
            j -= 1

        # Вставка текущего элемента key на правильную позицию
        arr[j + 1] = key

    return arr  # Возврат отсортированного списка


# Вызов функции с заданным списком и вывод результата
print(insertion_sort([64, 25, 12, 22, 11]))

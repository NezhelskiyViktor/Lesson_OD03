# Определение функции selection_sort, принимающей список arr
def selection_sort(arr):
    # Внешний цикл, проходящий по всем элементам списка
    for i in range(len(arr)):
        # Предположение, что текущий индекс i является
        # индексом минимального элемента
        min_index = i

        # Внутренний цикл, проходящий по оставшимся элементам списка
        for j in range(i + 1, len(arr)):
            # Проверка, является ли текущий элемент меньшим,
            # чем минимальный найденный
            if arr[j] < arr[min_index]:
                # Обновление индекса минимального элемента
                min_index = j

                # Обмен текущего элемента с найденным минимальным элементом
        arr[i], arr[min_index] = arr[min_index], arr[i]
    # Возврат отсортированного списка arr
    return arr


# Вызов функции с заданным списком и вывод результата
print(selection_sort([64, 25, 12, 22, 11]))

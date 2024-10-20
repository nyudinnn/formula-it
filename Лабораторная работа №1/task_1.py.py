numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Найдем сумму всех чисел, кроме None
valid_numbers = [num for num in numbers if num is not None]
total_sum = sum(valid_numbers)

# Общее количество элементов, включая пропуск
total_count = len(numbers)

# Среднее арифметическое всех элементов, кроме пропущенного
average = total_sum / total_count

# Заменим None на среднее арифметическое
numbers = [average if num is None else num for num in numbers]

# Выводим измененный список
print("Измененный список:", numbers)

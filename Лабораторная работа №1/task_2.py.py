# TODO Найдите количество книг, которое можно разместить на дискете
# Дано
disk_size_mb = 1.44  # размер дискеты в Мб
pages = 100  # количество страниц в книге
lines_per_page = 50  # количество строк на странице
symbols_per_line = 25  # количество символов в строке
bytes_per_symbol = 4  # количество байт на символ

# Конвертируем размер дискеты в байты
disk_size_bytes = disk_size_mb * 1024 * 1024

# Рассчитаем объем одной книги в байтах
book_size_bytes = pages * lines_per_page * symbols_per_line * bytes_per_symbol

# Рассчитаем, сколько книг помещается на дискету
books_on_disk = int(disk_size_bytes // book_size_bytes)

# Вывод результата
print("Количество книг, помещающихся на дискету:", books_on_disk)

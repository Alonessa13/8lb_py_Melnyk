# Основна частина
input1 = input("Введи перший список чисел через пробіл: ")
input2 = input("Введи другий список чисел через пробіл: ")

# Перетворення рядків у списки цілих чисел
list1 = [int(x) for x in input1.split()] if input1 else []
list2 = [int(x) for x in input2.split()] if input2 else []

# Обробка: об'єднати, видалити повтори, відсортувати
combined = list1 + list2
unique = list(set(combined))
sorted_list = sorted(unique)

print("Результуючий список:", sorted_list)

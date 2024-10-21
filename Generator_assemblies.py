first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# 1. В переменную first_result запишите генераторную сборку, которая высчитывает разницу длин строк из
# списков first и second, если их длины не равны. Для перебора строк попарно из двух списков используйте функцию zip.

# Генератор для вычисления разницы длин строк, если длины не равны
first_result = (len(f) - len(s) for f, s in zip(first, second) if len(f) != len(s))

# 2. В переменную second_result запишите генераторную сборку, которая содержит результаты сравнения длин строк в одинаковых
# позициях из списков first и second. Составьте эту сборку НЕ используя функцию zip. Используйте функции range и len.

# Генератор для сравнения длин строк на одинаковых позициях
second_result = (len(first[i]) == len(second[i]) for i in range(min(len(first), len(second))))

# Вывод результатов
print(list(first_result))   #  => [1, 2]
print(list(second_result))  #  => [False, False, True]
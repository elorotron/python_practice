# Настало самое главное событие в детском саду — новогодний утренник.
# Хорошо замаскированная робоняня в роли Деда Мороза решила раздать детям конфеты так, чтобы каждому досталось поровну.

# Напишите программу для робоняни, которая поможет раздать конфеты детям на новогоднем утреннике. Конфеты должны быть разделены поровну между всеми детьми, а оставшиеся конфеты останутся у Деда Мороза.

# Формат ввода
# В первой строке указано натуральное число N — количество детей на утреннике (
# N
# ≥
# 1
# N≥1).
# Во второй строке указано натуральное число M — количество конфет в конфетном отсеке робоняни (
# M
# ≥
# 1
# M≥1).

# Формат вывода
# Выведите два числа, каждое с новой строки:

# Количество конфет, которое получит каждый ребёнок.
# Количество конфет, которые останутся в отсеке.

childrens = int(input())
candies = int(input())

candies_per_child = candies // childrens
left_candies = candies % childrens

print(candies_per_child)
print(left_candies)
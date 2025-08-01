# Операции с числами
# Мы уже научились работать со строками. Теперь давайте разберёмся с числами — ведь в любой программе часто приходится считать: складывать, делить, округлять. Посмотрим, как Python работает с числами и какие операции доступны.

# Целые и вещественные числа
# В программировании, как и в математике, существуют два основных типа чисел:

# Целые числа — это числа без дробной части:
# -3, 0, 42

# Вещественные числа (или числа с плавающей точкой, float) — это числа с дробной частью:
# 3.14, 0.5, -7.25

# В Python для записи вещественных чисел используется точка, а не запятая.

a = 2 # целое число
b = 2.0 # вещественное число

# Создание числовых переменных
# Чтобы создать переменную и присвоить ей числовое значение, достаточно указать имя и знак равенства

n = 10 # целое число
pi = 3.14 # вещественное число

# Преобразование типов

# Для преобразования строк в числа и наоборот используются следующие функции:

# int() — преобразует строку (или вещественное число) в целое число. Дополнительно можно указать, в какой системе счисления было записано исходное число. По умолчанию используется десятичная система. При конвертации вещественного числа в целое отбрасывается дробная часть;
# float() — преобразует строку (или целое число) в вещественное число;
# str() — преобразует значения (в общем случае не только числовые) в строки.

n_1 = "1"
n_2 = "2"
print(n_1 + n_2)
n_1 = int(n_1)
n_2 = int(n_2)
print(n_1 + n_2)

# Первый результат — результат сложения (конкатенации) двух строк. Второй — результат сложения целых чисел, которые были преобразованы из строк функцией int().

x = 3.89
x = int(x)
print(x)

# Здесь программа выведет в консоли результат 3. Дробная часть после десятичного разделителя была отброшена при преобразовании в целое число.

width = "3.7"
height = "2.5"
s = float(width) * float(height)
print(s)
# Программа выведет: 9.25.

# float() — преобразует строку (или целое число) в вещественное число;
# А чтобы вводить целые или вещественные числа с клавиатуры, можно использовать уже знакомую нам функцию input() в сочетании с функциями int() и float():
int_number = int(input())
float_number = float(input())

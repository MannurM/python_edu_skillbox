# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя ни одной из операций деления: ни деления с плавающей точкой /, ни целочисленного деления //
# и взятия остатка %
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

a, b = 179, 37
xxx, yyy = a, b
count = 0
text_box = 'Целочисленное деление ' + str(xxx) + ' на ' + str(yyy) + ' дает'

while a > b:
    a = a - b
    count += 1

print(text_box, count)

# Зачёт!

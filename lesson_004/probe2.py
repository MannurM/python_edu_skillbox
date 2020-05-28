def color_number():
    color_num = int(input('Введите желаемый номер цвета:'))

    if 0 < color_num > 6:
        print('вы ввели некорректный номер, попробуйте еще раз')
        color_number()
    else:
        return

print('Возможные цвета:')
print('0: red')
print('1: orange')
print('2: yellow')
print('3: green')
print('4: cyan')
print('5: blue')
print('6: purple')

color_number()
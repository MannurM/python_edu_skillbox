# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
count = 1
material_assistance = 0
expenses_procent = 0

while count < 11:
    expenses_procent += (expenses + expenses_procent) * .03
    count += 1


material_assistance = round(expenses * 10 + expenses_procent - educational_grant * 10, 2)
print("Студенту надо попросить", material_assistance, "рублей")


# другой логики вычисления  у меня нет - всю голову сломал!!!!
#

educational_grant, expenses = 10000, 12000
count = 1
material_assistance = 0
expenses_procent = 0


while count < 11:
    expenses_procent += expenses * 0.03 + expenses_procent * .03
    print('месяц', count)
    print('проценты нарастающим итогом', expenses_procent)
    count += 1

material_assistance = round(expenses * 10 + expenses_procent - educational_grant * 10, 2)
print("Студенту надо попросить", material_assistance, "рублей")


# -*- coding: utf-8 -*-

# Создать модуль my_burger. В нем определить функции добавления инградиентов:
#  - булочки
#  - котлеты
#  - огурчика
#  - помидорчика
#  - майонеза
#  - сыра
# В каждой функции выводить на консоль что-то вроде "А теперь добавим ..."

# В этом модуле создать рецепт двойного чизбургера (https://goo.gl/zA3goZ)
# с помощью фукций из my_burger и вывести на консоль.

# Создать рецепт своего бургера, по вашему вкусу.
# Если не хватает инградиентов - создать соответствующие функции в модуле my_burger
# mb.mayonnaise()
# mb.cutlet()
# mb.cucumber()
# mb.tomato()
# mb.mayonnaise()
# mb.cheese()
# mb.onion()
# mb.dill()
# mb.mustard()
# mb.salad()

# import my_burger as mb
# # рецепт чизбургера я не знаю, пусть будет такой
# # вполне себе неплохой рецепт) хотя помидоры я бы не стал в самый низ класть, булочка вся промокнет
# # как раз помидоры - то наверху, бутерброды чаще все собираются снизу вверх ))
# # ...Добавим булочку
# # Добавим лист салата
# # Добавим котлету...
# #
# print('Рецепт:')
# mb.bun()
# mb.salad()
# mb.cutlet()
# mb.cheese()
# mb.onion()
# mb.dill()
# mb.cucumber()
# mb.tomato()
# mb.mayonnaise()
# mb.bun()

from my_burger import bun, salad, cutlet, cheese, onion, dill, cucumber, tomato, mayonnaise
print('Рецепт:')
bun(), salad(), cutlet(), cheese(), onion(), dill(), cucumber(), tomato(), mayonnaise(), bun()
#зачет!
# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...


from room_1 import folks as folks_room_1
from room_2 import folks

print('В комнате room_1 живут: ', end='')

print(', '.join(folks_room_1))

print('В комнате room_2 живет: ', end='')
print(folks[0])

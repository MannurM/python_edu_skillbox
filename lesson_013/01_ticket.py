# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru

# import os
# from PIL import Image, ImageDraw, ImageFont, ImageColor
#
#
# def make_ticket(fio, from_, to, date, out_path=None):
#     fio, from_, to, date = fio, from_, to, date
#     font_path = os.path.join('fonts', 'arial.ttf')
#     path_teplate = os.path.normpath(os.getcwd() + '/' + 'images/ticket_template.png')
#
#     image_teplate = Image.open(path_teplate)
#     draw = ImageDraw.Draw(image_teplate)
#     print(path_teplate)
#     font = ImageFont.truetype(font_path, size=18)
#
#     draw.text((45, 120), fio, font=font, fill=ImageColor.colormap['black'])  # ФИО
#     draw.text((45, 190), from_, font=font, fill=ImageColor.colormap['black'])  # откуда
#     draw.text((45, 255), to, font=font, fill=ImageColor.colormap['black'])  # куда
#     font = ImageFont.truetype(font_path, size=14)
#     draw.text((286, 259), date, font=font, fill=ImageColor.colormap['black'])  # время
#
#     image_teplate .show()
#     out_path = out_path if out_path else 'probe_ticket.png'
#     image_teplate.save(out_path)
#     print(f'Post card saved az {out_path}')
#
#
# if __name__ == '__main__':
#     make_ticket(fio='Пирцхилава Ираклий Батькович', from_='Лондон', to='Париж', date='01.01.2021')


import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to, date, out_path=None):
    fio, from_, to, date = fio, from_, to, date
    font_path = os.path.join('fonts', 'arial.ttf')
    path_teplate = os.path.normpath(os.getcwd() + '/' + 'images/ticket_template.png')

    image_teplate = Image.open(path_teplate)
    draw = ImageDraw.Draw(image_teplate)
    print(path_teplate)
    font = ImageFont.truetype(font_path, size=18)

    draw.text((45, 120), fio, font=font, fill=ImageColor.colormap['black'])  # ФИО
    draw.text((45, 190), from_, font=font, fill=ImageColor.colormap['black'])  # откуда
    draw.text((45, 255), to, font=font, fill=ImageColor.colormap['black'])  # куда
    font = ImageFont.truetype(font_path, size=14)
    draw.text((286, 259), date, font=font, fill=ImageColor.colormap['black'])  # время

    image_teplate.show()
    out_path = out_path if out_path else 'probe_ticket.png'
    image_teplate.save(out_path)
    print(f'Post card saved az {out_path}')


def create_parser():
    parser = argparse.ArgumentParser(description='silver wing plane ticket')
    parser.add_argument('--fio', type=str, required=True, help='Name')
    parser.add_argument('--from_', type=str, required=True, help='from')
    parser.add_argument('--to', type=str, required=True, help='to')
    parser.add_argument('--date', type=str, required=True, help='date')
    parser.add_argument('--save_to', type=str, help='ticket')
    return parser


if __name__ == '__main__':
    parser = create_parser()
    args = parser.parse_args()
    make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, out_path=args.save_to)
# TODO не знаю где ошибка.

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

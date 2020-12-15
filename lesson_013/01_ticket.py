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
# def make_ticket(fio, from_, to, date, out_name_file=None):
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
#     out_name_file = out_name_file if out_name_file else 'probe_ticket.png'
#     image_teplate.save(out_name_file)
#     print(f'Post card saved az {out_name_file}')
#
#
# if __name__ == '__main__':
#     make_ticket(fio='Пирцхилава Ираклий Батькович', from_='Лондон', to='Париж', date='01.01.2021')


import argparse
import os
from PIL import Image, ImageDraw, ImageFont, ImageColor


def make_ticket(fio, from_, to, date, out_name_file=None):
    fio, from_, to, date = fio, from_, to, date
    font_path = os.path.join('fonts', 'arial.ttf')
    path_teplate = os.path.normpath(os.path.join(os.getcwd(), 'images/ticket_template.png'))
    image_teplate = Image.open(path_teplate)
    draw = ImageDraw.Draw(image_teplate)

    font = ImageFont.truetype(font_path, size=18)
    draw.text((45, 120), fio, font=font, fill=ImageColor.colormap['black'])  # ФИО
    draw.text((45, 190), from_, font=font, fill=ImageColor.colormap['black'])  # откуда
    draw.text((45, 255), to, font=font, fill=ImageColor.colormap['black'])  # куда
    font = ImageFont.truetype(font_path, size=14)
    draw.text((286, 259), date, font=font, fill=ImageColor.colormap['black'])  # время

    # image_teplate.show()
    ticket_folder = 'Ticket'  # как вариант + '_' + fio, а если ФИО на русском - придется нормализовать к латинице?
    if not os.path.isdir(ticket_folder):
        os.mkdir(ticket_folder)
    os.chdir(ticket_folder)
    out_name_file = out_name_file if out_name_file else (fio + '_ticket.png')
    image_teplate.save(out_name_file)
    print(f'You ticket saved az {out_name_file} in folder {ticket_folder}')


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
    # args = parser.parse_args('--fio KLF --from_ M --to T --date 20-09-2020'.split())
    args = parser.parse_args()
    make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, out_name_file=args.save_to)

# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.
#зачёт!
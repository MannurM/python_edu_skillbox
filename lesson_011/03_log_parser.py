# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# который читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234


class ReaderGenerator:

    def __init__(self):
        self.file = None
        self.file_name = None
        self.group_time = None
        self.event_count = 1
        self.end_segment = 17
        self.old_line = None

    def __str__(self):
        pass

    def get_read(self, file_name):
        self.file_name = file_name
        with open(self.file_name, 'r', encoding='utf8') as self.file:
            for line in self.file:
                if not line:
                    continue
                if not line[-4:-3] == 'N':
                    continue
                else:
                    self.group_time = line[1:self.end_segment]
                    if self.group_time == self.old_line:
                        self.event_count += 1
                    else:
                        if self.old_line is None:
                            self.old_line = self.group_time
                            continue
                        yield self.old_line, self.event_count
                        self.old_line = self.group_time
                        self.event_count = 1
            yield self.old_line, self.event_count


grouped_events = ReaderGenerator()
for group_time, event_count in grouped_events.get_read(file_name='events.txt'):
    print(f'[{group_time}] {event_count}')
#зачёт!
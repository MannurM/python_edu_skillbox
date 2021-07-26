import csv
from multiprocessing import Process, Pipe
from queue import Empty

import prepare


class VolatilityObject(Process):

    def __init__(self, file_path, conn, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.dict_file = {}
        self.file_path = file_path
        self.tiker_price_list = []
        self.secid = None
        self.volatility_rezult = 0
        self.file = None
        self.conn = conn

    def run(self):
        with open(self.file_path, encoding='utf-8') as self.file:
            reader = csv.reader(self.file, delimiter=',')
            count = 0
            for line in reader:
                if count == 0:
                    count = 1
                    continue
                self.secid, tiker_price = line[0], line[2]
                self.tiker_price_list.append(float(tiker_price))

        value_max = max(self.tiker_price_list)
        value_min = min(self.tiker_price_list)
        if value_max == value_min:
            self.volatility_rezult = 0
        else:
            half_sum = (value_max + value_min) / 2
            difference = value_max - value_min
            self.volatility_rezult = (difference / half_sum) * 100
            self.volatility_rezult = round(self.volatility_rezult, 2)
        self.conn.send([self.secid, self.volatility_rezult])
        self.conn.close()  # вот тут () стоило добавить


if __name__ == '__main__':
    folder_name = 'trades'
    parent_conn, child_conn = Pipe()
    volatils = [VolatilityObject(file_path=file_path, conn=child_conn)
                for file_path in prepare.file_to_path(folder_name=folder_name)]
    volatility_dict = {}
    volatility_zero = []
    pipes =[]
    for volatil in volatils:
        volatil.start()
        # print(volatil)
        pipes.append(parent_conn)
    # TODO а так нельзя? запустили все процессы,  передали  и собрали данные по своим трубам,
    # TODO дождались заврешения процессов.
    # print(pipes)
    # for _ in pipes:
    #     data_pipe = parent_conn.recv()
    #     # print(data_pipe)
    #     if data_pipe[1] == 0:
    #         volatility_zero.append(data_pipe[0])
    #     else:
    #         volatility_dict.update({data_pipe[0]: data_pipe[1]})


    count = 1
    while True:
        try:
            data_pipe = parent_conn.recv()
            print('Труба работает', count, flush=True)
            if data_pipe[1] == 0:
                volatility_zero.append(data_pipe[0])
            else:
                volatility_dict.update({data_pipe[0]: data_pipe[1]})
            count += 1
        except Empty:
            print('процессы мертвы', flush=True)
            if not any(parent_conn.is_alive()):
                break
       # TODO а так не работает - исключение не выбрасывает

    # И получение данных стоит тут реализовывать, до join-ов
    # как в этом примере
    # for fisher in self.fishers:
    #     fisher.start()
    # while True:
    #     try:
    #         # Этот метод у очереди - атомарный и блокирующий,
    #         # Поток приостанавливается, пока нет элементов в очереди
    #         fish = self.fish_receiver.get(timeout=1)
    #         print(f'Садок принял {fish}', flush=True)
    #         self.fish_tank[fish] += 1
    #     except Empty:
    #         print('В садке пусто в течении 1 секунды', flush=True)
    #         if not any(fisher.is_alive() for fisher in self.fishers):
    #             break
    # for fisher in self.fishers:
    #     fisher.join()
    # print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)

    for volatil in volatils:
        volatil.join()
        print(volatil)

    prepare.printed_rezult(dict_value=volatility_dict, list_zero=volatility_zero)

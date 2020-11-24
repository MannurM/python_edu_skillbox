import csv



class PrepareObject:  #  Подготовка и обработка одного файла

    def __init__(self, folder_name):
        self.folder_name = folder_name
        self.secid = None
        self.volatility_rezult = 0
        self.volatility_max = []
        self.volatility_min = []
        self.volatility_dict = {}
        self.volatility_zero = []
        self.tiker_price_list = []  # список значений из файла
        self.half_sum = 0  # полусумма
        self.difference = 0  # разность макс и мин
        self.value_max = 0
        self.value_min = 0
        self.dict_file = {}
        self.key = None
        self.dict_file = {}
        self.tiker_price = []
        self.file_path = ''

    def prepare(self, file_path):  # предобработка данных
        self.file_path = file_path
        with open(self.file_path, encoding='utf-8') as file:
            reader = csv.reader(file, delimiter=',')
            count = 0
            for line in reader:
                if count == 0:
                    count = 1
                    continue
                self.secid, self.tiker_price = line[0], line[2]
                self.tiker_price_list.append(self.tiker_price)
            self.dict_file.update({self.secid: self.tiker_price_list})
            print(self.secid)
        return self.dict_file

    def calculation(self, dict_file):
        self.dict_file = dict_file
        self.tiker_price_list = self.dict_file[self.secid]
        self.value_max = float(max(self.tiker_price_list))
        self.value_min = float(min(self.tiker_price_list))
        if self.value_max == self.value_min:
            self.volatility_zero.append(self.secid)
        self.half_sum = (self.value_max + self.value_min) / 2
        self.difference = (self.value_max - self.value_min)
        self.difference = round(self.difference, 4)
        self.volatility_rezult = (self.difference / self.half_sum) * 100
        self.volatility_rezult = round(self.volatility_rezult, 4)
        self.volatility_dict.update({self.secid: self.volatility_rezult})
        print('____________', self.value_max, self.value_min, self.half_sum, self.difference,
              self.volatility_rezult)
        return self.volatility_dict

    def printed_rezult(self):  # сортировка и вывод на консоль
        for i, v in self.volatility_dict.items():
            self.volatility_max.append(v)
        self.volatility_min = self.volatility_max
        #  вывод на консоль
        self.volatility_max.sort(reverse=True)
        print('Максимальная волатильность:')
        for i in range(3):
            self.get_value(dic=self.volatility_dict, value=self.volatility_max[i])
            print(self.key, self.volatility_max[i])

        self.volatility_min.sort()
        print('Минимальная волатильность:')
        for i in range(3):
            self.get_value(dic=self.volatility_dict, value=self.volatility_min[i])
            print(self.key, self.volatility_min[i])

        self.volatility_zero.sort()
        print('Нулевая волатильность:')
        print(self.volatility_zero)

    def get_value(self, dic, value):
        for self.key in dic:
            if dic[self.key] == value:
                return self.key



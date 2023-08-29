import csv
import os


class InstantiateCSVError(Exception):
    def __init__(self, message="Файл item.csv поврежден"):
        self.message = message
        super().__init__(self.message)


@classmethod
def instantiate_from_csv(cls, filename=None):
    """
    Инициализирует экземпляры класса Item данными из CSV файла.
    """
    if filename is None:
        script_location = os.path.abspath(os.path.dirname(__file__))
        filename = os.path.join(script_location, '../src/items.csv')

    try:
        with open(filename, newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if row['name'] == '' or row['price'] == '' or row['quantity'] == '':
                    raise InstantiateCSVError("Файл item.csv поврежден")
                cls(row['name'], row['price'], row['quantity'])
    except FileNotFoundError:
        print(f'FileNotFoundError: Отсутствует файл {filename}')




class Item:
    """
    Класс для представления товара в магазине.
    """
    pay_rate = 1.0
    all = []


    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Создание экземпляра класса item.

        :param name: Название товара.
        :param price: Цена за единицу товара.
        :param quantity: Количество товара в магазине.
        """
        self.__name = name
        self.price = price
        self.quantity = quantity
        Item.all.append(self)

    def __repr__(self):
        return f'{self.__class__.__name__}{self.__name}, {self.price},{self.quantity}'

    @property


    def name(self):
        return self.__name

    @name.setter


    def name(self, name):
        if len(name) > 10:
            name = name[:10]
        else:
            self.__name = name


    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        total_price = self.price * self.quantity
        return total_price


    def apply_discount(self) -> float:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price *= self.pay_rate
        return self.price

    @classmethod
    def instantiate_from_csv(cls):
        """
        Инициализирует экземпляры класса Item данными из CSV файла.
        """
        with open('../src/items.csv', newline='',
            encoding='utf-8-sig') as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(row['name'], row['price'], row['quantity'])
                cls(row['name'], row['price'], row['quantity'])

    @staticmethod


    def string_to_number(string):
        """Преобразует строку в число."""
        return float(string)



    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', {self.price}, {self.quantity})"

    def __str__(self):
        return self.name

    def __add__(self, other):
        if isinstance(other, Item):
            return self.quantity + other.quantity
        else:
            raise TypeError("Ошибка")



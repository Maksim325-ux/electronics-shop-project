import csv


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

    def calculate_total_price(self) -> float:
        """
        Рассчитывает общую стоимость конкретного товара в магазине.

        :return: Общая стоимость товара.
        """
        return self.price * self.quantity


    def apply_discount(self) -> None:
        """
        Применяет установленную скидку для конкретного товара.
        """
        self.price = self.price * Item.pay_rate

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        if len(value) >= 10:
            return 'Длина наименования товара превышает 10 символов.'
        self.__name = value

    @classmethod
    def instantiate_from_csv(cls):
        '''класс-метод, инициализирующий экземпляры класса'''
        with open('items.csv', 'r', encoding='windows-1251') as csvfile:
            data = csv.reader(csvfile)
            for i in data:
                cls.all.append(i)

    @staticmethod
    def string_to_number(number):
        '''статический метод, возвращающий число из числа-строки'''
        return int(number.split('.')[0])






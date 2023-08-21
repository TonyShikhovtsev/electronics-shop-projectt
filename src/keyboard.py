from src.item import Item


class MixinLog():
    language = 'EN'

    def change_lang(self):
        if self.language == 'EN':
            self.language = 'RU'
        else:
            self.language = "EN"
        return self


class Keyboard(Item, MixinLog):
    """
    Класс представления товара
    """

    pay_rate = 1.0

    def __init__(self, name: str, price: float, quantity: int) -> None:
        """
        Функция создания класса Keyboard
        """
        super().__init__(name, price, quantity)

    def __str__(self):
        return f'{self.name}'


keyboard = Keyboard('AOS', 5000, 2)
print(Keyboard.__mro__)
print(keyboard.__dict__)
print(keyboard.name)
print(keyboard.price)
print(keyboard.language)
keyboard.change_lang().change_lang()
print(keyboard.language)

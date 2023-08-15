from item import Item

class Phone(Item):
    def __init__(self, name, price,quantity, sim_slots):
        super().__init__(name, price,quantity)
        self.sim_slots = sim_slots

    def __add__(self, other):
        if isinstance(other,(Phone, Item)):
            return self.quantity + other.quantity
        else:
            raise ValueError("Ошибка")


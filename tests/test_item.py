"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item


def test_name_getter_setter(self):
    item = Item("Product", 10.0, 5)
    self.assertEqual(item.name, "Product")

    item.name = "LongProductName"
    self.assertEqual(item.name, "LongProdu")
def test_calculate_total_price():
    item = Item("Тестовый товар", 10.0, 3)
    expected_total_price = 30.0
    result = item.calculate_total_price()
    assert result == expected_total_price

def test_apply_discount():
    item = Item("Тестовый товар", 100.0, 1)
    item.apply_discount()
    expected_price = 50.0
    result = item.price
    assert result == expected_price

def test_string_to_number(self):
    number_str = "15.75"
    converted_number = Item.string_to_number(number_str)
    self.assertEqual(converted_number, 15.75)

def test_instantiate_from_csv(self):
    Item.instantiate_from_csv()
    assert len(Item.all) == 3
    assert Item.all[0].name == "Product1"
    assert Item.all[0].price == "10.0"
    assert Item.all[0].quantity == "5"


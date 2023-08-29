"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv
from src.item import Item, instantiate_from_csv, InstantiateCSVError
from src.phone import Phone




def test_calculate_total_price():
    item = Item("Тестовый товар", 10.0, 3)
    expected_total_price = 30.0
    result = item.calculate_total_price()
    assert result == expected_total_price


def test_apply_discount():
    item = Item("Тестовый товар", 50.0, 1)
    item.apply_discount()
    expected_price = 50.0
    result = item.price
    assert result == expected_price


def test_string_to_number():
    number_str = "15.75"
    converted_number = Item.string_to_number(number_str)
    assert converted_number == 15.75


def test_name_getter_and_setter():
    item = Item("Test Item", 10.0, 5)
    assert item.name == "Test Item"


def test_repr():
    item = Item("Смартфон", 10000, 20)
    assert repr(item) == "Item('Смартфон', 10000, 20)"

def test_str():
    item = Item("Смартфон", 10000, 20)
    assert str(item) == "Смартфон"


def test_phone_creation():
    phone = Phone("Phone Model", 1000, 10, 2)
    assert phone.name == "Phone Model"
    assert phone.price == 1000
    assert phone.quantity == 10
    assert phone.sim_slots == 2


def test_phone_addition_with_item():
    phone = Phone("Phone Model", 1000, 10, 2)
    item = Item("Item Model", 500, 5)
    result = phone + item
    assert result == 15


def test_phone_addition_with_phone():
    phone1 = Phone("Phone Model 1", 1000, 10, 2)
    phone2 = Phone("Phone Model 2", 1200, 8, 1)
    result = phone1 + phone2
    assert result == 18


def test_item_instantiate_from_csv():
    Item.instantiate_from_csv()
    assert len(Item.all) == 5
    item_data = Item.all[0]
    assert item_data.name == 'Компьютер'
    assert int(item_data.price) == 100
    assert int(item_data.quantity) == 1





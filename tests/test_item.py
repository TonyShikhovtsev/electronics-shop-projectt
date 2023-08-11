"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
import csv
from src.item import Item


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

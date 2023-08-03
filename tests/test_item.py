"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest
from src.item import Item

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


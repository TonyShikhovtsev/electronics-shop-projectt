import pytest
from src.item import Item
from src.phone import Phone

def test_phone_addition_with_item():
    phone = Phone("Phone Model", 1000, 10, 2)
    item = Item("Item Model", 500, 5)
    result = phone + item
    assert result == 15


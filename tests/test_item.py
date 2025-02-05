"""Здесь надо написать тесты с использованием pytest для модуля item."""
import pytest

from src.item import Item

@pytest.fixture
def item1():
    return Item("Смартфон", 10000, 20)
def test_init(item1):
    assert item1.name == 'Смартфон'
    assert item1.price == 10000
    assert item1.quantity == 20


def test_calculate_total_price(item1):
    assert 200000
"""Здесь надо написать тесты с использованием pytest для модуля item."""

import pytest
from src.item import Item


@pytest.fixture
def item():
    """Тест Класса"""
    return Item("Смартфон", 10000, 20)


def test_item(item) :
    """Тест атрибутов"""
    assert item.name == "Смартфон"
    assert item.price == 10000
    assert item.quantity == 20


def test_calculate_total_price(item):
    """Тест метода общей стоимости товара"""
    assert item.calculate_total_price() == 200000


def test_apply_discount(item):
    """ Тест метода применения скидки"""
    item.pay_rate = 0.8
    item.apply_discount()
    assert item.price == 8000.0


# Se comprueba la el comportamiento de un objeto
from datetime import date

from models.product import Product

import pytest

def test_product_creation():
    product = Product(
        1,
        "Mac",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    assert product.id == 1
    assert product.name == "Mac"
    assert product.price == 1200
    assert product.quantity == 10
    assert product.expiration_date == date(2026, 12, 31)
    
def test_product_rejects_invalid_name():
    with pytest.raises(ValueError):
        Product(
            1,
            "",
            1200,
            10,
            date(2026, 12, 31),
        )
        
def test_product_rejects_invalid_price():
    with pytest.raises(ValueError):
        Product(
            1,
            "Mac",
            0,
            10,
            date(2026, 12, 31),
        )
        
def test_product_rejects_invalid_quantity():
    with pytest.raises(ValueError):
        Product(
            1,
            "Mac",
            1200,
            -1,
            date(2026, 12, 31),
        )
        
def test_product_add_stock():
    product = Product(
        1,
        "Mac",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    product.add_stock(5)

    assert product.quantity == 15
    
def test_product_add_stock_rejects_zero():
    product = Product(
        1,
        "Mac",
        2300,
        20,
        date(2026, 12, 31),
    )
    
    with pytest.raises(ValueError):
        product.add_stock(0)
        
def test_product_rejects__negative_amount():
    product = Product(
        1,
        "Mac",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    with pytest.raises(ValueError):
        product.add_stock(-5)
    
def test_product_remove_stock():
    product = Product(
        1,
        "Mac",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    product.remove_stock(4)
    assert product.quantity == 6
    
def test_product_remove_stock_rejects_zero():
    product = Product(
        1,
        "Mac",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    with pytest.raises(ValueError):
        product.remove_stock(0)
        
def test_product_remove_stock_rejects_negative_amount():
    product = Product(
        1,
        "Mac",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    with pytest.raises(ValueError):
        product.remove_stock(-5)
        
def test_product_remove_stock_rejects_amount_greater_than_stock():
    product = Product(
        1,
        "Mac",
        1200,
        3,
        date(2026, 12, 31),
    )
    
    with pytest.raises(ValueError):
        product.remove_stock(4)
        
def test_product_id_is_read_only():
    product = Product(
        1,
        "Mac",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    with pytest.raises(AttributeError):
        product.id = 2
        
def test_product_string_representation():
    product = Product(
        1,
        "Mac",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    result = str(product)
    
    assert "ID: 1" in result
    assert "Name: Mac" in result
    assert "Price: $1200" in result
    assert "Quantity: 10" in result
    assert "Expiration Date: 2026-12-31" in result
    
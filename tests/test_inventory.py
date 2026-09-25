from models.inventory import Inventory
from datetime import date
from models.product import Product
from utils.exceptions import InvalidProductIdError
import pytest

def test_inventory_starts_empty():
    inventory = Inventory()
    
    assert inventory.total_products() == 0
    assert inventory.is_empty() is True
    
def test_inventory_add_product():
    inventory = Inventory()
    
    product = Product(
        1,
        "Mac",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    inventory.add_product(product)
    
    assert inventory.total_products() == 1
    assert inventory.get_products() == [product]
    
def test_inventory_add_multiple_products():
    inventory = Inventory()
    
    product_1 = Product(
        1,
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )

    product_2 = Product(
        2,
        "Mouse",
        150,
        50,
        date(2028, 12, 31),
    )

    inventory.add_product(product_1)
    inventory.add_product(product_2)
    
    assert inventory.total_products() ==2
    assert inventory.get_products() == [product_1, product_2]
    
def test_inventory_find_product_by_id():
    inventory = Inventory()

    product = Product(
        1,
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )

    inventory.add_product(product)

    result = inventory.find_product_by_id(1)

    assert result is product
    
def test_inventory_find_product_by_returns_none_when_not_found():
    inventory = Inventory()
    
    product = Product(
        1,
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    inventory.add_product(product)
    
    result = inventory.find_product_by_id(99)
    
    assert result is None
    
def test_inventory_find_product_by_id_rejects_zero():
    inventory = Inventory()
    
    with pytest.raises(InvalidProductIdError):
        inventory.find_product_by_id(0)
        
def test_find_product_by_id_reajects_negative_id():
    inventory = Inventory()
    
    with pytest.raises(InvalidProductIdError):
        inventory.find_product_by_id(-5)
        
def test_inventory_remove_product():
    inventory = Inventory()
    
    product = Product(
        1,
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    inventory.add_product(product)
    inventory.remove_product(1)
    
    assert inventory.total_products() == 0
    assert inventory.find_product_by_id(1) is None

def test_inventory_remove_product_when_not_found():
    inventory = Inventory()
    
    product = Product(
        1,
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    inventory.add_product(product)
    inventory.remove_product(99)
    
    assert inventory.total_products() == 1
    assert inventory.find_product_by_id(1) is product
    
def test_inventory_update_prodcut_price():
    inventory = Inventory()
    
    product = Product(
        1,
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    inventory.add_product(product)
    inventory.update_product(1, price=1500)
    
    assert product.price == 1500
    assert product.quantity == 10
    assert product.expiration_date == date(2026, 12, 31)
    
def test_inventory_update_product_quantity():
    inventory = Inventory()

    product = Product(
        1,
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )

    inventory.add_product(product)

    inventory.update_product(1, quantity=25)

    assert product.quantity == 25
    assert product.price == 1200
    assert product.expiration_date == date(2026, 12, 31)
    
def test_inventory_update_product_expiration_date():
    inventory = Inventory()
    
    product = Product(
        1,
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    inventory.add_product(product)
    
    inventory.update_product(
        1, 
        expiration_date = date(2027, 12, 31)
        )
    
    assert product.expiration_date == date(2027, 12, 31)
    assert product.price == 1200
    assert product.quantity == 10
    
def test_inventory_update_product_multiple_fields():
    inventory = Inventory()

    product = Product(
        1,
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )

    inventory.add_product(product)

    inventory.update_product(
        1,
        price=1500,
        quantity=25,
        expiration_date=date(2027, 12, 31),
    )

    assert product.price == 1500
    assert product.quantity == 25
    assert product.expiration_date == date(2027, 12, 31)
    
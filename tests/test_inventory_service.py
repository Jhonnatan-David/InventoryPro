from datetime import date

from models.inventory import Inventory
from services.inventory_service import InventoryService

def test_inventory_services_uses_existing_inventory():
    inventory = Inventory()
    
    service = InventoryService(inventory)
    
    assert service.inventory is inventory
    
def test_inventory_service_create_product():
    inventory = Inventory() #Se crea el inventario con sus parametros
    service = InventoryService(inventory)#Crea el objeto con los servicios
    
    service.create_product(
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    products = inventory.get_products()
    
    assert len(products) == 1
    assert products[0].id == 1
    assert products[0].name == "Laptop"
    assert products[0].price == 1200
    assert products[0].quantity == 10
    assert products[0].expiration_date == date(2026, 12, 31)
    
def test_inventory_services_genrates_sequential_ids():
    inventory = Inventory() #Se crea el inventario con sus parametros
    service = InventoryService(inventory)
    
    service.create_product(
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    service.create_product(
        "Mouse",
        1500,
        50,
        date(2028, 12, 31),
    )
    
    products =inventory.get_products()
    
    assert len(products) == 2
    assert products[0].id == 1
    assert products[1].id == 2
    
def test_inventory_service_get_product():
    inventory = Inventory()
    service = InventoryService(inventory)
    
    service.create_product(
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    result = service.get_product(1)
    
    assert result is inventory.get_products()[0]
    
def test_inventory_service_get_product_returns_none_when_not_found():
    inventory = Inventory()
    service = InventoryService(inventory)

    service.create_product(
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )

    result = service.get_product(99)

    assert result is None
    
def test_inventory_service_get_all_products():
    inventory = Inventory()
    service = InventoryService(inventory)

    service.create_product(
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )

    service.create_product(
        "Mouse",
        150,
        50,
        date(2028, 12, 31),
    )
    
    result = service.get_all_products()
    
    assert result is inventory.get_products()
    assert len(result) == 2
    assert result[0].name == "Laptop"
    assert result[1].name == "Mouse"
    
def test_inventory_services_delete_product():
    inventory = Inventory()
    service = InventoryService(inventory)
    
    service.create_product(
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )
    
    service.delete_product(1)
    
    assert service.get_product(1) is None
    assert service.get_all_products() == []
    
def test_inventory_service_update_product():
    inventory = Inventory()
    service = InventoryService(inventory)

    service.create_product(
        "Laptop",
        1200,
        10,
        date(2026, 12, 31),
    )

    service.update_product(
        1,
        price=1500,
        quantity=20,
    )

    product = service.get_product(1)

    assert product.price == 1500
    assert product.quantity == 20
    assert product.expiration_date == date(2026, 12, 31)
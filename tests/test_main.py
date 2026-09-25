from main import (
    get_validated_input, 
    get_validated_integer, 
    add_product,
    search_product,
    update_product,
    delete_product,
    show_products,
    main,
    )
from datetime import date
from main import search_product


def test_get_validated_input_returns_validate_value(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "Laptop"
    )
    
    result = get_validated_input(
        "Name: ",
        lambda value: value.strip()
    )
    
    assert result == "Laptop"
    
def test_get_validated_input_retries_after_invalid_input(monkeypatch, capsys):
    inputs = iter(["", "Laptop"]) #iter: Nos permite simular 2 entradas consecutivas
    
    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )
    
    def validate_name(value):
        if not value.strip():
            raise ValueError("Product name cannot be empy.")
        
        return value
    
    result = get_validated_input(
        "Name: ",
        validate_name
    )
    
    captured = capsys.readouterr() #capsys, captura lo de main.py imprime con print()
    
    assert result == "Laptop"
    assert "Product name cannot be empy." in captured.out
    

    
def test_validate_integer_returns_validated_value(monkeypatch):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1200"
    )
    
    result = get_validated_integer(
        "Price: ",
        lambda value: value
    )
    
    assert result == 1200
    
def test_get_validated_integer_retries_after_non_numeric_input(monkeypatch, capsys):
    
    inputs = iter(["abc", "1200"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    result = get_validated_integer(
        "Price: $",
        lambda value: value
    )

    captured = capsys.readouterr()

    assert result == 1200
    assert "Invalid Input. Please enter a whole number." in captured.out
    
def test_get_validated_integer_retries_after_validation_error(
    monkeypatch,
    capsys,
):
    inputs = iter(["-50", "1200"])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    def validate_price(value):
        if value <= 0:
            raise ValueError("Price must be greater than zero.")

        return value

    result = get_validated_integer(
        "Price: $",
        validate_price
    )

    captured = capsys.readouterr()

    assert result == 1200
    assert "Price must be greater than zero." in captured.out
    
def test_add_product_creates_product_with_valid_input(
    monkeypatch,
    capsys,
):
    inputs = iter([
        "Laptop",
        "1200",
        "10",
        "2026-12-31",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    created_product = {}

    class FakeInventoryService:
        def create_product(
            self,
            name,
            price,
            quantity,
            expiration_date,
        ):
            created_product["name"] = name
            created_product["price"] = price
            created_product["quantity"] = quantity
            created_product["expiration_date"] = expiration_date

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    add_product()

    captured = capsys.readouterr()

    assert created_product == {
        "name": "Laptop",
        "price": 1200,
        "quantity": 10,
        "expiration_date": date(2026, 12, 31),
    }

    assert "Product created Successfully" in captured.out
    
def test_add_product_retries_invalid_price_before_creating_product(
    monkeypatch,
    capsys,
):
    inputs = iter([
        "Laptop",
        "-100",
        "1200",
        "10",
        "2026-12-31",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    created_product = {}

    class FakeInventoryService:
        def create_product(
            self,
            name,
            price,
            quantity,
            expiration_date,
        ):
            created_product["name"] = name
            created_product["price"] = price
            created_product["quantity"] = quantity
            created_product["expiration_date"] = expiration_date

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    add_product()

    captured = capsys.readouterr()

    assert created_product == {
        "name": "Laptop",
        "price": 1200,
        "quantity": 10,
        "expiration_date": date(2026, 12, 31),
    }

    assert "Price must be greater than zero." in captured.out
    assert "Product created Successfully" in captured.out
    
def test_search_product_displays_existing_product(
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1"
    )

    class FakeProduct:
        def __str__(self):
            return "Laptop - $1200"

    class FakeInventoryService:
        def get_product(self, product_id):
            assert product_id == 1
            return FakeProduct()

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    search_product()

    captured = capsys.readouterr()

    assert "Product found." in captured.out
    assert "Laptop - $1200" in captured.out
    
def test_search_product_displays_not_found_message(
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99"
    )

    class FakeInventoryService:
        def get_product(self, product_id):
            assert product_id == 99
            return None

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    search_product()

    captured = capsys.readouterr()

    assert "Product not found." in captured.out

def test_update_product_updates_price(
    monkeypatch,
):
    inputs = iter([
        "1",
        "1",
        "250",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    class FakeProduct:
        pass

    product = FakeProduct()

    class FakeInventoryService:
        def get_product(self, product_id):
            assert product_id == 1
            return product

        def update_product(self, product_id, price=None):
            assert product_id == 1
            assert price == 250

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )
    
    update_product()
    
def test_update_product_displays_not_found_message(
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99"
    )

    class FakeInventoryService:
        def get_product(self, product_id):
            assert product_id == 99
            return None

        def update_product(self, product_id, price=None):
            raise AssertionError(
                "update_product should not be called"
            )

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    update_product()

    captured = capsys.readouterr()

    assert "Product not found" in captured.out
    
def test_update_product_updates_quantity(
    monkeypatch,
):
    inputs = iter([
        "1",
        "2",
        "25",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    class FakeProduct:
        pass

    product = FakeProduct()

    class FakeInventoryService:
        def get_product(self, product_id):
            assert product_id == 1
            return product

        def update_product(self, product_id, quantity=None):
            assert product_id == 1
            assert quantity == 25

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    update_product()

def test_update_product_updates_expiration_date(
    monkeypatch,
):
    inputs = iter([
        "1",
        "3",
        "2027-12-31",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    class FakeProduct:
        pass

    product = FakeProduct()

    class FakeInventoryService:
        def get_product(self, product_id):
            assert product_id == 1
            return product

        def update_product(
            self,
            product_id,
            expiration_date=None,
        ):
            assert product_id == 1
            assert expiration_date == date(2027, 12, 31)

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    update_product()
    
def test_delete_product_deletes_existing_product(
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "1"
    )

    class FakeProduct:
        pass

    product = FakeProduct()

    class FakeInventoryService:
        def get_product(self, product_id):
            assert product_id == 1
            return product

        def delete_product(self, product_id):
            assert product_id == 1

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    delete_product()

    captured = capsys.readouterr()

    assert "Product deleted successfully." in captured.out
    
def test_delete_product_displays_not_found_message(
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "99"
    )

    class FakeInventoryService:
        def get_product(self, product_id):
            assert product_id == 99
            return None

        def delete_product(self, product_id):
            raise AssertionError(
                "delete_product should not be called"
            )

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    delete_product()

    captured = capsys.readouterr()

    assert "Product not found." in captured.out
    
def test_show_products_displays_products(
    monkeypatch,
    capsys,
):
    class FakeProduct:
        def __str__(self):
            return "Product 1"

    products = [
        FakeProduct(),
    ]

    class FakeInventoryService:
        def get_all_products(self):
            return products

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    show_products()

    captured = capsys.readouterr()

    assert "Product 1" in captured.out
    
def test_show_products_displays_not_found_when_empty(
    monkeypatch,
    capsys,
):
    class FakeInventoryService:
        def get_all_products(self):
            return []

    monkeypatch.setattr(
        "main.services",
        FakeInventoryService()
    )

    show_products()

    captured = capsys.readouterr()

    assert "No product found." in captured.out
    
def test_main_exits_when_user_selects_exit(
    monkeypatch,
    capsys,
):
    monkeypatch.setattr(
        "builtins.input",
        lambda _: "6"
    )

    main()

    captured = capsys.readouterr()

    assert "Exiting InventoryPro..." in captured.out
    assert "InventoryPro Closed" in captured.out
    
def test_main_handles_non_numeric_menu_input(
    monkeypatch,
    capsys,
):
    inputs = iter([
        "abc",
        "6",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    main()

    captured = capsys.readouterr()

    assert "Invalid option. Please enter a number from 1 to 6." in captured.out
    assert "Exiting InventoryPro..." in captured.out
    
def test_main_handles_invalid_menu_option(
    monkeypatch,
    capsys,
):
    inputs = iter([
        "9",
        "6",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs)
    )

    main()

    captured = capsys.readouterr()

    assert (
        "Invalid option. Please select a number from 1 to 6."
        in captured.out
    )
    assert "Exiting InventoryPro..." in captured.out
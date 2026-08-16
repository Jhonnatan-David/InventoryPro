

Architecture

main.py

Entry point of the application.

Responsibilities:
- Display menu
- Receive user input
- Call InventoryService

----------------------------

models/

Contains business entities.

Product

Inventory


Product
│
├── _id 🔒
├── _name
├── _price
├── _quantity
└── _expiration_date
│
├── id (solo lectura)
├── name (controlado)
├── price (validación)
├── quantity (validación)
└── expiration_date (validación)


Inventory
│
├── add_product()
├── remove_product()
├── find_product()
└── list_products()

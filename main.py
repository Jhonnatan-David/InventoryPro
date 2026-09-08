'''
Su responsabilidad es muy simple:
Crear los objetos principales.
Mostrar el menú.
Leer lo que escribe el usuario.
Llamar a los métodos adecuados.
Nada más.

===== InventoryPro =====

1. Add Product

2. List Products

3. Exit

'''
from models.inventory import Inventory
from services.inventory_service import InventoryService
from utils.validators import (
    validate_product_name,
    validate_price, 
    validate_quantity, 
    validate_product_id,
    validate_update_option,
    validate_expiration_date,
    )

inventory = Inventory()
services = InventoryService(inventory)


def get_validated_input(prompt, validator):
    while True:
        value = input(prompt)
        try:
            return validator(value)
        except ValueError as error:
            print(error)

def get_validated_integer(prompt, validator):
    while True:
        try: 
            value = int(input(prompt))
        except ValueError:
            print("Invalid Input. Please enter a whole number.")
            continue

        try:
            return validator(value)
        except ValueError as error:
            print(error)    
    
def add_product():
    print("\n======> Add Product <======\n")
    
    name = get_validated_input(
        "Name: ",
        validate_product_name
        )
    
    price = get_validated_integer(
        "Price: $",
        validate_price 
    )

    quantity = get_validated_integer(
        "Quantity: ",
        validate_quantity
    )
            
    
    expiration_date = get_validated_input(
        "Expiration Date (YYYY-MM-DD): ",
        validate_expiration_date
    )
    services.create_product(
        name, 
        price, 
        quantity, 
        expiration_date
        )
     
    print("\nProduct created Successfully")
            
def show_products():
    print("\n======> Show Products <======\n")          
                
    products = services.get_all_products()
    
    if products:
        for product in products:
            print(product)
    else:
        print("No product found.")
                    
def search_product():                        
    print("======>   Search Product    <======\n")
        
    product_id = get_validated_integer(
        "Enter Product ID: ",
        validate_product_id
    )
    
    product = services.get_product(product_id)

    if product:
        print("\n Product found.")
        print(product)

    else:
        print("Product not found.")    
            
def update_product():            
    print("\n======> Update Product <======\n")
    
    product_id = get_validated_integer(
        "Enter product ID: ",
        validate_product_id
    )

    product = services.get_product(product_id)
        
    if not product:
        print("Product not found")
        return
            
    print("\n======> Select Update Product <======\n")
    print("1. Price \n")
    print("2. Quantity \n")
    print("3. Expiration Date")

    update_option = get_validated_integer(
        "\nSelect an option: ",
        validate_update_option
    )
    
    if update_option == 1:
        price = get_validated_integer(
            "New Price: $",
            validate_price
        )
        
        services.update_product(product_id, price = price)
        print("\nPrice updated successfully.\n")
                
    elif update_option == 2:
        quantity = get_validated_integer(
            "New Quantity: ",
            validate_quantity
        )
        
        services.update_product(product_id, quantity = quantity)
        print("\nQuantity updated successfully.\n")
                        
    elif update_option == 3:
        expiration_date = get_validated_input(
            "New Expiration Date (YYYY-MM-DD): ",
            validate_expiration_date
        )
        services.update_product(product_id, expiration_date = expiration_date)
        print("\nExpiration Date updated successfully.\n")
    
    print(services.get_product(product_id))
            
def delete_product():   
    print("\n======> Delete Product <======\n")         
            
    product_id = get_validated_integer(
        "Enter product ID: ",
        validate_product_id
    )
    product = services.get_product(product_id)

    if not product:
        print("\nProduct not found.") 
        return
    
    services.delete_product(product_id)
    print("\nProduct deleted successfully.\n")
            
            
def main():
    print("\n======>   Welcome to InventoryPro    <======\n")
    
    running = True
    
    while running:
        print("\n======>   InventoryPro Menu    <======\n")
        print("1. Add Product")
        print("2. Show Products")
        print("3. Search Product")
        print("4. Update product")
        print("5. Delete Product")
        print("6. Exit")
    
        try:
            option = int(input("\nSelect an option: "))
        
            if option == 1:
                add_product()
                
            elif option == 2:
                show_products()
                
            elif option == 3:
                search_product()
                
            elif option == 4:
                update_product()
                
            elif option == 5:
                delete_product()
                
            elif option == 6:
                print("\nExiting InventoryPro...\n")
                running = False
                
            else:
                print("Invalid option. Please select a number from 1 to 6.\n")

        except ValueError:
            print("\nInvalid option. Please enter a number from 1 to 6.")
            
    print("\n======>   InventoryPro Closed    <======\n")    
        
if __name__ == "__main__":
    main()
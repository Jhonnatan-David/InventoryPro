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
from models.product import Product

product = Product

inventory = Inventory()
services = InventoryService(inventory)
print(" ")
print("\n======>   Welcome to InventoryPro.    <======\n")
print("1. Add Product")
print("2. Show Products")
print("3. Search Product")
print("4. Update product")
print("5. Delete Product")
print("6. Exit")

option = int(input("\nSelect an option: ")) #Input siempre vevuelde un str

if option == 1:
    print("\nPlease enter the product information.\n")
    
    valid = False
    while not valid:
        try:
            name = input("Name: ")
            
            try:
                price = int(input("Price: "))
            except ValueError:
                print("Invalid price. Please enter a numeric value.")
                continue
            try:     
                quantity = int(input("Quantity: "))
            except ValueError:
                print("Invalid quantity, Please enter a numeric value.")
                continue
            
            expiration_date = input("Expiration Date: ")
            
            services.create_product(name, price, quantity, expiration_date)
            
            valid = True
            
        except ValueError as error:
            print(f"Invalid product: {error}")
    

    print("\nProduct created Successfully")
    
elif option == 2:
        print("\n======>   Show Products    <======\n")
        
        products = services.get_all_products()
        
        if products:
            for product in products:
                print(product)
        else:
            print("No product found.")
            
elif option == 3:
    print("======>   Search Product    <======\n")
    
    valid = False
    
    while not valid:
        try:
            product_id = int(input("Enter ID the Product you wish to search for: \n "))
        
            product = services.get_product(product_id)
        
            if product:
                print("\n Product found.")
                print(product)
                valid = True
            else:
                print("Product not found.")
                valid = True
        
        except ValueError:
            print("Invalid product ID. Please enter a valid integer.")
    
elif option == 4:
     #Temporal
    product1 = product(
        1,
        "Mac",
        1200,
        10,
        "1/01/2026",
    )
    inventory.add_product(product1) #Temporal
    print("\n======> Select Update Product <======\n")
    
    valid = False
    
    while not valid:
        try:
            product_id = int(input("\nEnter product ID: "))
            product = services.get_product(product_id)
            
            if not product:
                print("Product not found")
                valid = True
                
            else:
                print("\n======> Select Update Product <======\n")
                print("1. Price \n")
                print("2. Quantity \n")
                print("3. Expitarion Date \n")

                update_option = int(input("Selectan option: "))
            
                if update_option == 1:
                    price = int(input("New Price: "))
                    services.update_product(product_id, price = price)
                    print("\nPrice update successfully.\n")
                    print(services.get_product(product_id))
                    valid = True
                    
                elif update_option == 2:
                    quantity = int(input("New Quantity: "))
                    services.update_product(product_id, quantity = quantity)
                    print("\nQuantity update successfully.\n")
                    print(services.get_product(product_id))
                    valid = True
                    
                elif update_option == 3:
                    expiration_date = input("New Expiration Date: ")
                    services.update_product(product_id, expiration_date = expiration_date)
                    print("\nExpiration Date update successfully.\n")
                    print(services.get_product(product_id))
                    valid = True
                    
                else:
                    print("invalid update option.")
                    valid = True
                    
        except ValueError:
            print("Invalid input. Pleas enter a valid value.")
    
elif option == 5:
    
    #Temporal
    product1 = product(
        1,
        "Mac",
        1200,
        10,
        "1/01/2026",
    )
    inventory.add_product(product1) #Temporal
    
    print("\n======> Delete Product <======\n")
    
    try:
        product_id = int(input("Enter product ID: "))
    
        if product:
            services.delete_product(product_id)
            print(f"Product deleted successfully.\n")
        else:
            print("Product not found.") 
        
    except ValueError:
        print("Invalid product ID. Pleas enter a valid integer.")        
    
elif option == 6:
    print("Exit\n")
else:
    print("Invalid option.\n")
    



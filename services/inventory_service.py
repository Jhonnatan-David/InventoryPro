from models.product import Product


class InventoryService:
    def __init__(self,inventory):
         self.inventory = inventory
         self.next_id = 1
         
    def create_product(
        self,
        name,
        price,
        quantity,
        expiration_date,
        ):
        
        new_product = Product(
            self.next_id,
            name,
            price,
            quantity,
            expiration_date,
        )        

        self.inventory.add_product(new_product)
        self.next_id += 1
        
    def get_product(self,product_id):
        return self.inventory.find_product_by_id(product_id)
    
    def delete_product(self, product_id):
        return self.inventory.remove_product(product_id)
    
    def update_product(
        self, 
        product_id,
        price = None,
        quantity = None,
        expiration_date = None,
        ):
        return self.inventory.update_product(
            product_id,
            price = price,
            quantity = quantity,
            expiration_date = expiration_date,
            )
        
    def get_all_products(self):
        return self.inventory.get_product()
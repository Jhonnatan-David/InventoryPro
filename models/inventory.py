
class Inventory:
    def __init__(self):
        self.products = [] #Lista
        
    def add_product(self, product):
        self.products.append(product)
        
    def show_products(self):
        for product in self.products:
            print(product)
            
    def get_product(self):
        return self.products
            
    def total_products(self):
        return len(self.products)
    
    def is_empty(self):
        if self.total_products() <= 0:
            return True
        return False
    
    def find_product_by_id(self, product_id):
        for product in self.products:
            if product_id == product.id:
                return product

    def remove_product(self, product_id):
        delete_product= self.find_product_by_id (product_id)
  
        if delete_product:
            self.products.remove(delete_product)
            
    def update_product (
        self, 
        product_id,
        price = None,
        quantity = None,
        expiration_date = None,
        ):
        found_product = self.find_product_by_id(product_id)
        
        if found_product:
            if price is not None:
                found_product.price= price
                
            if quantity is not None:
                found_product.quantity = quantity

            if expiration_date is not None:
                found_product.expiration_date = expiration_date
                
        else:
            print(f"Product with ID {product_id} does not exist")



class Product:
    
    def __init__(
        self, 
        product_id, 
        name, 
        price, 
        quantity, 
        expiration_date,
        ):
        
        self._id = product_id
        self._name = name
        self.price = price
        self.quantity = quantity
        self.expiration_date = expiration_date
        
    def __str__(self):
            return (
                f"=======  Product Information  =======\n"
                f"----------------------------------------\n"
                f"ID: {self._id}\n"
                f"Name: {self._name}\n"
                f"Price: {self._price}\n"
                f"Quantity: {self._quantity}\n"
                f"Expiration Date: {self._expiration_date}\n"
            )
    
    @property
    def id(self):
        return self._id
            
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, texto):
        
        self._name=texto
            
    @property
    def price(self):
        return self._price
        
    @price.setter
    def price(self, value):
        if value <= 0:
            raise ValueError("Price must be greater than zero")
            
        self._price = value
            
    @property
    def quantity(self):
        return self._quantity
    
    @quantity.setter
    def quantity(self, value):
        if value < 0:
            raise ValueError("Quantity cannot be negative and less than zero")
        self._quantity = value
        
    @property
    def expiration_date(self):
        return self._expiration_date

    @expiration_date.setter
    def expiration_date(self, value):
        self._expiration_date = value
    

    def add_stock(self, amount):
        if amount <=0:
            raise ValueError("Stock amount must be greater than zero")
        
        self.quantity += amount
        
    def remove_stock(self, amount):
        if amount <= 0:
            raise ValueError("Quantity cannot be zero or negative")
        
        if amount > self.quantity:
            raise ValueError("Quantity cannot be more than current stock")
        
        self.quantity -= amount
        
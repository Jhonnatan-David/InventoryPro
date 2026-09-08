from datetime import date, datetime

def validate_product_name(name):
    if not name.strip():
        raise ValueError("Product name cannot be empty. ")
    
    return name

def validate_price(price):
    if price <=0:
        raise ValueError ("Price must be greater than zero.")
    
    return price

def validate_quantity(quantity):
    if quantity <0:
        raise ValueError ("Quantity cannot be negative.")
    
    return quantity

def validate_product_id(product_id):
    if product_id <= 0:
        raise ValueError("Product ID must be greater than zero.")
    
    return product_id

def validate_update_option(option):
    if option not in (1,2,3):
        raise ValueError("Invalid update option. Please select 1, 2, or 3. ")
    
    return option

def validate_expiration_date(value):
    if isinstance(value, datetime):
        return value.date()
    if isinstance(value, date):
        return value
    try:
        return datetime.strptime(value, "%Y-%m-%d").date()
    except ValueError:
        raise ValueError(
            "Invalid expiration date. use the format YYYY-MM-DD."
        )
from datetime import date, datetime

from utils.validators import (
    validate_product_name, 
    validate_price,
    validate_quantity,
    validate_product_id,
    validate_update_option,
    validate_expiration_date
    )
import pytest

#Resultados esperados
def test_validate_product_name_accepts_valid_name():
    result = validate_product_name("Laptop")
    
    assert result == "Laptop"
    

#Errores esperados
def test_validate_product_name_accepts_rejects_valid_name():
    with pytest.raises(ValueError):
        validate_product_name("")
        
        
def test_validate_product_name_accepts_valid_price():
    result = validate_price(100)
    
    assert result == 100
    
def test_validate_price_rejects_zero():
    with pytest.raises(ValueError):
        validate_price(0)
        
def test_validate_price_rejects_negative_price():
    with pytest.raises(ValueError):
        validate_price(-50)
        
def test_validate_product_name_accepts_positive_quantity():
    result = validate_quantity(10)
    assert result == 10
    
def test_validate_quantity_accepts_zero_quantity():
    result = validate_quantity(0)
    
    assert result == 0
    
def test_valicate_quantity_rejects_negative_quantity():
    with pytest.raises(ValueError):
        validate_quantity(-5)
        
def test_validate_product_id_accepts_valid_id():
    result = validate_product_id(1)
    
    assert result == 1
    
def test_validate_rejects_zero():
    with pytest.raises(ValueError):
        validate_product_id(0)
        
def test_validate_product_id_rejects_negative_id():
    with pytest.raises(ValueError):
        validate_product_id(-3)
        
def test_validate_upgrade_option_accepts_valid_option(): 
    result = validate_update_option(1)
    
    assert result == validate_update_option(1)

def test_validate_update_optionaccepts_second_valid_option():
    result = validate_update_option(2)
    
    assert result == 2
    
def test_validate_update_option_accepts_third_valid_option():
    result = validate_update_option(3)
    
    assert result == 3
    
@pytest.mark.parametrize("option", [0,4,-1])
def test_validate_update_option_rejects_invalid_options(option):
    with pytest.raises(ValueError):
        validate_update_option(option)
        
def test_validate_expiration_date_accepts_valid_string():
    result = validate_expiration_date("2026-12-31")
    
    assert result == date(2026, 12, 31)
    
def test_validate_expiration_date_rejects_invalid_format():
    with pytest.raises(ValueError):
        validate_expiration_date("12/31/2026")
        
def test_validate_expiration_date_rejects_invalid_date():
    with pytest.raises(ValueError):
        validate_expiration_date("2026-02-30")
        
def test_validate_expiration_date_accepts_date():
    expiration_date = date(2026, 12, 31)
    
    result = validate_expiration_date(expiration_date)
    
    assert result == expiration_date
    
def test_validate_expiration_date_converts_datetime_to_date():
    expiration_datetime = datetime(2026, 12, 31, 15, 30)
    
    result = validate_expiration_date(expiration_datetime)
    
    assert result == date(2026, 12, 31)
    

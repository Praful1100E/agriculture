# utils/validators.py - Input validation utilities
import re

def validate_phone(phone):
    """Validate Indian phone number"""
    if not phone:
        return False, "Phone number is required"

    # Remove any spaces or special characters
    phone = re.sub(r'[^0-9]', '', phone)

    # Check length and pattern
    if len(phone) == 10 and phone[0] in '6789':
        return True, ""
    elif len(phone) == 13 and phone.startswith('91') and phone[2] in '6789':
        return True, ""
    else:
        return False, "Please enter a valid 10-digit phone number"

def validate_email(email):
    """Validate email address"""
    if not email:
        return False, "Email is required"

    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(pattern, email):
        return True, ""
    else:
        return False, "Please enter a valid email address"

def validate_password(password):
    """Validate password strength"""
    if not password:
        return False, "Password is required"

    if len(password) < 6:
        return False, "Password must be at least 6 characters long"

    return True, ""

def validate_price(price_text):
    """Validate price input"""
    if not price_text:
        return False, "Price is required"

    try:
        price = float(price_text)
        if price <= 0:
            return False, "Price must be greater than 0"
        return True, ""
    except ValueError:
        return False, "Please enter a valid price"

def validate_quantity(quantity_text):
    """Validate quantity input"""
    if not quantity_text:
        return False, "Quantity is required"

    try:
        quantity = float(quantity_text)
        if quantity <= 0:
            return False, "Quantity must be greater than 0"
        return True, ""
    except ValueError:
        return False, "Please enter a valid quantity"

def validate_required_field(value, field_name):
    """Validate required field"""
    if not value or not value.strip():
        return False, f"{field_name} is required"
    return True, ""
#!/usr/bin/env python3
"""
Test script to verify login functionality and seller product display
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_login():
    """Test login with existing users"""
    db = DatabaseManager()

    # Test users from database
    test_cases = [
        ("8544757931", "23022007"),  # seller
        ("8598658456", "Praful@1234"),  # seller
        ("6230329271", "ggggggghjhd"),  # seller
        ("6548962462", "fdfyuhdsr"),  # buyer
    ]

    print("Testing login functionality:")
    for phone, password in test_cases:
        result = db.authenticate_user(phone, password)
        if result:
            name, role, location = result
            print(f"✅ Login successful: {phone} -> {name} ({role})")
        else:
            print(f"❌ Login failed: {phone}")

def test_seller_products():
    """Test seller product retrieval"""
    db = DatabaseManager()

    seller_phones = ["8544757931", "8598658456", "6230329271"]

    print("\nTesting seller product retrieval:")
    for phone in seller_phones:
        products = db.get_user_products(phone)
        print(f"Seller {phone}: {len(products)} products")
        for product in products:
            print(f"  - {product[2]} ({product[3]}): {product[7]} {product[5]} @ ₹{product[6]}")

if __name__ == "__main__":
    test_login()
    test_seller_products()

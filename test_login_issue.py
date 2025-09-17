#!/usr/bin/env python3
"""
Test script to debug login and product display issues
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_login():
    """Test login functionality"""
    db = DatabaseManager()

    print("=== Testing Login Functionality ===")

    # Test with existing users
    test_users = [
        ("8544757931", "23022007"),  # jatin dadwal - seller
        ("8598658456", "Praful@1234"),  # Lo - seller
        ("6230329271", "ggggggghjhd"),  # Reemma - seller
        ("6548962462", "fdfyuhdsr"),  # neha - buyer
    ]

    for phone, password in test_users:
        result = db.authenticate_user(phone, password)
        if result:
            name, role, location = result
            print(f"✅ Login successful: {name} ({role}) - Phone: {phone}")
        else:
            print(f"❌ Login failed: Phone {phone}")

def test_products():
    """Test product retrieval"""
    db = DatabaseManager()

    print("\n=== Testing Product Display ===")

    # Test with seller phones
    seller_phones = ["8544757931", "8598658456", "6230329271"]

    for phone in seller_phones:
        products = db.get_user_products(phone)
        print(f"Seller {phone}: {len(products)} products")
        for product in products:
            print(f"  - {product[2]} ({product[3]}) - ₹{product[6]}/{product[5]} - Stock: {product[7]}")

def test_marketplace():
    """Test marketplace products"""
    db = DatabaseManager()

    print("\n=== Testing Marketplace Products ===")

    products = db.get_all_products()
    print(f"Total marketplace products: {len(products)}")
    for product in products:
        print(f"  - {product[2]} ({product[3]}) - ₹{product[6]}/{product[5]} - Seller: {product[1]}")

if __name__ == "__main__":
    test_login()
    test_products()
    test_marketplace()

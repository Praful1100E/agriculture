#!/usr/bin/env python3
"""
Test script to check login functionality and seller products
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_login():
    db = DatabaseManager()

    # Test login with existing users
    test_users = [
        ("8544757931", "23022007"),  # jatin dadwal - seller
        ("8598658456", "Praful@1234"),  # Lo - seller
        ("6230329271", "ggggggghjhd"),  # Reem ma - seller
        ("6548962462", "fdfyuhdsr"),  # neha - buyer
    ]

    print("Testing login functionality:")
    for phone, password in test_users:
        result = db.authenticate_user(phone, password)
        if result:
            name, role, location = result
            print(f"✅ Login successful: {phone} -> {name} ({role})")
        else:
            print(f"❌ Login failed: {phone}")

    print("\nTesting seller products:")
    seller_phones = ["8544757931", "8598658456", "6230329271"]
    for phone in seller_phones:
        products = db.get_user_products(phone)
        print(f"Seller {phone} has {len(products)} products:")
        for product in products:
            print(f"  - {product[2]} ({product[3]}) - ₹{product[6]}/{product[5]} - Stock: {product[7]}")

if __name__ == "__main__":
    test_login()

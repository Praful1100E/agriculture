#!/usr/bin/env python3
"""
Test script to verify seller product display functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_product_display():
    """Test product display logic"""
    db = DatabaseManager()

    # Test with a seller who has products
    phone = "8598658456"  # Lo - has Wheat
    products = db.get_user_products(phone)

    print(f"Testing product display for seller {phone}:")
    print(f"Found {len(products)} products")

    for i, product in enumerate(products):
        print(f"\nProduct {i+1}:")
        print(f"  ID: {product[0]}")
        print(f"  Seller Phone: {product[1]}")
        print(f"  Name: {product[2]}")
        print(f"  Category: {product[3]}")
        print(f"  Variety: {product[4]}")
        print(f"  Unit: {product[5]}")
        print(f"  Price: {product[6]}")
        print(f"  Quantity: {product[7]}")
        print(f"  Description: {product[8]}")
        print(f"  Status: {product[10]}")

        # Simulate the display logic
        name = product[2]
        category = product[3]
        price = product[6]
        unit = product[5]
        quantity = product[7]
        status = product[10] or 'Active'

        print("
Display simulation:")
        print(f"  Product: {name}")
        print(f"  Category: {category}")
        print(f"  Price: ₹{price:.2f}/{unit}")
        print(f"  Stock: {quantity} {unit}")
        print(f"  Status: {status}")

if __name__ == "__main__":
    test_product_display()

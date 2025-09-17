#!/usr/bin/env python3
"""
Comprehensive test script for AgriConnect functionality
Tests login, product display, and marketplace features
"""

import sys
import os
import time
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_user_registration():
    """Test user registration functionality"""
    print("\n=== Testing User Registration ===")
    db = DatabaseManager()

    # Test data
    test_users = [
        {
            "name": "Test Seller",
            "phone": "9999999999",
            "email": "test@example.com",
            "password": "TestPass123",
            "role": "seller",
            "location": "Test City"
        },
        {
            "name": "Test Buyer",
            "phone": "8888888888",
            "email": "buyer@example.com",
            "password": "BuyerPass123",
            "role": "buyer",
            "location": "Test City"
        }
    ]

    for user in test_users:
        try:
            success = db.create_user(
                user["name"], user["phone"], user["email"],
                user["password"], user["role"], user["location"]
            )
            if success:
                print(f"✅ Registration successful: {user['name']} ({user['role']})")
            else:
                print(f"❌ Registration failed: {user['name']} - Phone already exists")
        except Exception as e:
            print(f"❌ Registration error for {user['name']}: {e}")

def test_login_scenarios():
    """Test various login scenarios"""
    print("\n=== Testing Login Scenarios ===")
    db = DatabaseManager()

    # Test cases
    test_cases = [
        ("8544757931", "23022007", "Existing seller"),
        ("8598658456", "Praful@1234", "Existing seller with products"),
        ("6230329271", "ggggggghjhd", "Existing seller with products"),
        ("6548962462", "fdfyuhdsr", "Existing buyer"),
        ("9999999999", "TestPass123", "Newly registered seller"),
        ("8888888888", "BuyerPass123", "Newly registered buyer"),
        ("1234567890", "wrongpass", "Invalid credentials"),
        ("", "", "Empty credentials"),
    ]

    for phone, password, description in test_cases:
        try:
            result = db.authenticate_user(phone, password)
            if result:
                name, role, location = result
                print(f"✅ {description}: {name} ({role}) - Login successful")
            else:
                print(f"❌ {description}: Login failed")
        except Exception as e:
            print(f"❌ {description}: Error - {e}")

def test_product_management():
    """Test product management functionality"""
    print("\n=== Testing Product Management ===")
    db = DatabaseManager()

    # Test adding products
    test_products = [
        {
            "seller_phone": "9999999999",
            "name": "Test Rice",
            "category": "Grains",
            "variety": "Basmati",
            "unit": "kg",
            "price": 50.0,
            "quantity": 100.0,
            "description": "Premium quality basmati rice"
        },
        {
            "seller_phone": "9999999999",
            "name": "Test Tomatoes",
            "category": "Vegetables",
            "variety": "Organic",
            "unit": "kg",
            "price": 30.0,
            "quantity": 50.0,
            "description": "Fresh organic tomatoes"
        }
    ]

    for product in test_products:
        try:
            product_id = db.add_product(
                product["seller_phone"], product["name"], product["category"],
                product["variety"], product["unit"], product["price"],
                product["quantity"], product["description"]
            )
            if product_id:
                print(f"✅ Product added: {product['name']} (ID: {product_id})")
            else:
                print(f"❌ Failed to add: {product['name']}")
        except Exception as e:
            print(f"❌ Error adding {product['name']}: {e}")

def test_product_retrieval():
    """Test product retrieval for different users"""
    print("\n=== Testing Product Retrieval ===")
    db = DatabaseManager()

    test_phones = ["9999999999", "8598658456", "6230329271", "8544757931"]

    for phone in test_phones:
        try:
            products = db.get_user_products(phone)
            print(f"📦 Seller {phone}: {len(products)} products")
            for product in products:
                print(f"   - {product[2]} ({product[3]}) - ₹{product[6]}/{product[5]} - Stock: {product[7]}")
        except Exception as e:
            print(f"❌ Error retrieving products for {phone}: {e}")

def test_marketplace():
    """Test marketplace functionality"""
    print("\n=== Testing Marketplace ===")
    db = DatabaseManager()

    try:
        products = db.get_all_products()
        print(f"🛒 Marketplace: {len(products)} total products")

        categories = {}
        for product in products:
            category = product[3]  # category
            if category not in categories:
                categories[category] = []
            categories[category].append(product[2])  # name

        print("📊 Products by category:")
        for category, product_names in categories.items():
            print(f"   {category}: {len(product_names)} products - {', '.join(product_names[:3])}{'...' if len(product_names) > 3 else ''}")

    except Exception as e:
        print(f"❌ Error loading marketplace: {e}")

def test_cart_functionality():
    """Test cart functionality"""
    print("\n=== Testing Cart Functionality ===")
    db = DatabaseManager()

    buyer_phone = "8888888888"  # Test buyer
    product_ids = []

    # Get some product IDs
    try:
        products = db.get_all_products()
        if products:
            product_ids = [p[0] for p in products[:2]]  # First 2 products
    except Exception as e:
        print(f"❌ Error getting product IDs: {e}")
        return

    # Test adding to cart
    for product_id in product_ids:
        try:
            success = db.add_to_cart(buyer_phone, product_id, 1)
            if success:
                print(f"✅ Added product {product_id} to cart")
            else:
                print(f"❌ Failed to add product {product_id} to cart")
        except Exception as e:
            print(f"❌ Error adding to cart: {e}")

    # Test getting cart
    try:
        cart_items = db.get_cart_items(buyer_phone)
        print(f"🛒 Cart for {buyer_phone}: {len(cart_items)} items")
        for item in cart_items:
            print(f"   - Product ID: {item[1]}, Quantity: {item[2]}")
    except Exception as e:
        print(f"❌ Error getting cart: {e}")

def run_all_tests():
    """Run all tests"""
    print("🚀 Starting AgriConnect Functionality Tests")
    print("=" * 50)

    try:
        test_user_registration()
        test_login_scenarios()
        test_product_management()
        test_product_retrieval()
        test_marketplace()
        test_cart_functionality()

        print("\n" + "=" * 50)
        print("✅ All tests completed!")

    except Exception as e:
        print(f"\n❌ Test suite failed: {e}")

if __name__ == "__main__":
    run_all_tests()

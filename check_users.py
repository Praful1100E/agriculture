#!/usr/bin/env python3
"""
Check existing users and test login with real credentials
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def check_existing_users():
    """Check existing users in database"""
    print("👥 Existing Users in Database:")
    print("=" * 50)

    db = DatabaseManager()
    conn = db.get_connection()
    c = conn.cursor()

    try:
        c.execute("SELECT name, phone, role, location FROM users")
        users = c.fetchall()

        if users:
            for i, user in enumerate(users, 1):
                name, phone, role, location = user
                print(f"{i}. {name} ({phone}) - {role.upper()}")
                if location:
                    print(f"   Location: {location}")
                print()
        else:
            print("No users found in database")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def test_real_login():
    """Test login with existing users"""
    print("🔐 Testing Login with Existing Users:")
    print("=" * 50)

    db = DatabaseManager()
    conn = db.get_connection()
    c = conn.cursor()

    try:
        c.execute("SELECT name, phone, password, role FROM users LIMIT 3")
        users = c.fetchall()

        for user in users:
            name, phone, password, role = user
            print(f"\nTesting login for: {name} ({phone})")

            # Test authentication
            result = db.authenticate_user(phone, password)
            if result:
                auth_name, auth_role, auth_location = result
                print(f"✅ Login successful: {auth_name} ({auth_role})")
            else:
                print("❌ Login failed")

    except Exception as e:
        print(f"Error: {e}")
    finally:
        conn.close()

def check_products():
    """Check existing products"""
    print("\n📦 Existing Products in Database:")
    print("=" * 50)

    db = DatabaseManager()
    products = db.get_available_products()

    if products:
        for i, product in enumerate(products, 1):
            product_id, seller_phone, name, category, variety, unit, price, stock_qty, description, image_path, status, created_at, updated_at, seller_name, seller_location = product
            print(f"{i}. {name} ({category})")
            print(f"   Seller: {seller_name} ({seller_phone})")
            print(f"   Price: ₹{price}/{unit}")
            print(f"   Stock: {stock_qty}")
            if description:
                print(f"   Description: {description}")
            print()
    else:
        print("No products found")

if __name__ == "__main__":
    check_existing_users()
    test_real_login()
    check_products()

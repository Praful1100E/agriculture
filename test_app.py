#!/usr/bin/env python3
"""
Test script for AgriConnect app
Tests database functionality and user flows
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_database():
    """Test database operations"""
    print("🧪 Testing Database Operations...")

    db = DatabaseManager()

    # Test 1: Check if database tables exist
    print("\n1. Checking database schema...")
    conn = db.get_connection()
    c = conn.cursor()

    try:
        c.execute("SELECT name FROM sqlite_master WHERE type='table'")
        tables = c.fetchall()
        table_names = [table[0] for table in tables]
        expected_tables = ['users', 'products', 'orders', 'cart', 'govt_schemes', 'price_history', 'addresses', 'notifications']

        print(f"Found tables: {table_names}")
        for table in expected_tables:
            if table in table_names:
                print(f"✅ {table} table exists")
            else:
                print(f"❌ {table} table missing")

    except Exception as e:
        print(f"❌ Error checking schema: {e}")
    finally:
        conn.close()

    # Test 2: Check existing users
    print("\n2. Checking existing users...")
    conn = db.get_connection()
    c = conn.cursor()

    try:
        c.execute("SELECT COUNT(*) FROM users")
        user_count = c.fetchone()[0]
        print(f"Total users: {user_count}")

        if user_count > 0:
            c.execute("SELECT name, phone, role, location FROM users")
            users = c.fetchall()
            for user in users:
                print(f"  - {user[0]} ({user[1]}) - {user[2]} - {user[3]}")
        else:
            print("No users found. Creating test users...")

            # Create test users
            test_users = [
                ("Rajesh Kumar", "9876543210", "rajesh@example.com", "password123", "seller", "Hamirpur"),
                ("Priya Sharma", "9876543211", "priya@example.com", "password123", "buyer", "Bilaspur"),
                ("Amit Singh", "9876543212", "amit@example.com", "password123", "seller", "Kangra")
            ]

            for user in test_users:
                success = db.create_user(*user)
                if success:
                    print(f"✅ Created user: {user[0]}")
                else:
                    print(f"❌ Failed to create user: {user[0]}")

    except Exception as e:
        print(f"❌ Error checking users: {e}")
    finally:
        conn.close()

    # Test 3: Check existing products
    print("\n3. Checking existing products...")
    conn = db.get_connection()
    c = conn.cursor()

    try:
        c.execute("SELECT COUNT(*) FROM products")
        product_count = c.fetchone()[0]
        print(f"Total products: {product_count}")

        if product_count > 0:
            c.execute("SELECT name, category, price, stock_qty, unit FROM products LIMIT 5")
            products = c.fetchall()
            for product in products:
                print(f"  - {product[0]} ({product[1]}) - ₹{product[2]}/{product[4]} - Stock: {product[3]}")
        else:
            print("No products found. Creating test products...")

            # Create test products for sellers
            test_products = [
                ("9876543210", "Tomatoes", "Vegetables", "Hybrid", "kg", 25.0, 100.0, "Fresh red tomatoes"),
                ("9876543210", "Wheat", "Grains", "Organic", "quintal", 1800.0, 50.0, "Premium quality wheat"),
                ("9876543212", "Rice", "Grains", "Basmati", "kg", 80.0, 200.0, "Long grain basmati rice"),
                ("9876543212", "Potatoes", "Vegetables", "Desi", "kg", 15.0, 150.0, "Fresh potatoes")
            ]

            for product in test_products:
                product_id = db.add_product(*product)
                if product_id:
                    print(f"✅ Created product: {product[1]}")
                else:
                    print(f"❌ Failed to create product: {product[1]}")

    except Exception as e:
        print(f"❌ Error checking products: {e}")
    finally:
        conn.close()

    # Test 4: Test authentication
    print("\n4. Testing authentication...")
    test_credentials = [
        ("9876543210", "password123"),  # Rajesh (seller)
        ("9876543211", "password123"),  # Priya (buyer)
        ("9999999999", "password123"),  # Non-existent user
        ("9876543210", "wrongpass")     # Wrong password
    ]

    for phone, password in test_credentials:
        result = db.authenticate_user(phone, password)
        if result:
            name, role, location = result
            print(f"✅ Login successful: {name} ({role}) - {location}")
        else:
            print(f"❌ Login failed: {phone}")

    # Test 5: Test product retrieval
    print("\n5. Testing product retrieval...")
    products = db.get_user_products("9876543210")  # Rajesh's products
    if products:
        print(f"✅ Found {len(products)} products for Rajesh:")
        for product in products:
            print(f"  - ID: {product[0]}, Name: {product[2]}, Price: ₹{product[6]}/{product[5]}, Stock: {product[7]}")
    else:
        print("❌ No products found for Rajesh")

    # Test 6: Test available products
    print("\n6. Testing available products...")
    available_products = db.get_available_products(10)
    if available_products:
        print(f"✅ Found {len(available_products)} available products:")
        for product in available_products:
            print(f"  - {product[2]} by {product[11]} - ₹{product[6]}/{product[5]}")
    else:
        print("❌ No available products found")

    print("\n🎉 Database testing completed!")

def test_session_management():
    """Test session management"""
    print("\n🔐 Testing Session Management...")

    try:
        from kivy.storage.jsonstore import JsonStore
        store = JsonStore('data/user_session.json')

        # Clear any existing session
        if store.exists("session"):
            store.delete("session")
            print("✅ Cleared existing session")

        # Test storing session
        test_session = {
            "phone": "9876543210",
            "name": "Rajesh Kumar",
            "role": "seller",
            "location": "Hamirpur"
        }

        store.put("session", **test_session)
        print("✅ Session stored successfully")

        # Test retrieving session
        if store.exists("session"):
            session_data = store.get("session")
            print(f"✅ Session retrieved: {session_data}")

            # Verify data integrity
            if all(session_data.get(key) == value for key, value in test_session.items()):
                print("✅ Session data integrity verified")
            else:
                print("❌ Session data integrity check failed")
        else:
            print("❌ Session not found after storing")

        # Test session deletion
        store.delete("session")
        if not store.exists("session"):
            print("✅ Session deleted successfully")
        else:
            print("❌ Session deletion failed")

    except Exception as e:
        print(f"❌ Session management test failed: {e}")

if __name__ == "__main__":
    print("🚀 AgriConnect App Testing Suite")
    print("=" * 50)

    test_database()
    test_session_management()

    print("\n" + "=" * 50)
    print("✅ All tests completed!")
    print("\n📱 You can now run the app with: python main.py")
    print("🔑 Test login credentials:")
    print("   Seller: 9876543210 / password123")
    print("   Buyer:  9876543211 / password123")

#!/usr/bin/env python3
"""
Test script to reproduce the profile issue when seller clicks on seller information
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_profile_loading():
    """Test profile loading for sellers"""
    print("=== Testing Profile Loading ===")

    # Test with existing sellers
    test_sellers = [
        ("8544757931", "23022007", "jatin dadwal"),
        ("8598658456", "Praful@1234", "Lo"),
        ("6230329271", "ggggggghjhd", "Reema"),
        ("9999999999", "TestPass123", "Test Seller")
    ]

    db = DatabaseManager()

    for phone, password, expected_name in test_sellers:
        print(f"\n--- Testing seller: {expected_name} ({phone}) ---")

        # Simulate login
        result = db.authenticate_user(phone, password)
        if not result:
            print(f"❌ Login failed for {phone}")
            continue

        name, role, location = result
        print(f"✅ Login successful: {name} ({role})")

        # Simulate profile loading
        try:
            # Get user info (simulating ProfileScreen.load_profile)
            conn = db.get_connection()
            c = conn.cursor()
            c.execute("SELECT name, email, location FROM users WHERE phone = ?", (phone,))
            user_data = c.fetchone()
            conn.close()

            if user_data:
                name, email, location = user_data
                print(f"📋 Profile data: Name={name}, Email={email}, Location={location}")
            else:
                print("❌ User data not found")

            # Test statistics loading (simulating ProfileScreen.load_statistics)
            print(f"📊 Loading statistics for {role} - phone: {phone}")

            if role == "seller":
                # Count products
                products = db.get_user_products(phone)
                print(f"📦 Found {len(products)} products for seller")

                # Count orders (seller orders)
                orders = db.get_user_orders(phone, role)
                print(f"📋 Found {len(orders)} orders for seller")

                # Show product details
                if products:
                    print("   Products:")
                    for product in products[:3]:  # Show first 3
                        print(f"   - {product[2]} ({product[3]}) - ₹{product[6]}/{product[5]} - Stock: {product[7]}")

                # Show order details
                if orders:
                    print("   Recent orders:")
                    for order in orders[:2]:  # Show first 2
                        order_id, order_number, buyer_phone, seller_phone, product_id, quantity, unit_price, total_amount, status, delivery_address, payment_method, notes, created_at, delivered_at, product_name, buyer_name = order
                        print(f"   - Order #{order_number}: {product_name} x{quantity} = ₹{total_amount} ({status})")

        except Exception as e:
            print(f"❌ Error during profile loading: {e}")
            import traceback
            traceback.print_exc()

def test_orders_query():
    """Test the orders query specifically"""
    print("\n=== Testing Orders Query ===")

    db = DatabaseManager()
    test_sellers = ["8544757931", "8598658456", "6230329271", "9999999999"]

    for phone in test_sellers:
        print(f"\n--- Testing orders for seller: {phone} ---")

        try:
            # Test the exact query used in get_user_orders
            conn = db.get_connection()
            c = conn.cursor()
            c.execute("""SELECT o.*, p.name as product_name, u.name as buyer_name
                        FROM orders o
                        JOIN products p ON o.product_id = p.id
                        JOIN users u ON o.buyer_phone = u.phone
                        WHERE o.seller_phone = ?
                        ORDER BY o.created_at DESC""", (phone,))
            orders = c.fetchall()
            conn.close()

            print(f"📋 Found {len(orders)} orders via direct query")

            if orders:
                for order in orders[:2]:
                    print(f"   Order data: {order}")

        except Exception as e:
            print(f"❌ Error in orders query: {e}")
            import traceback
            traceback.print_exc()

def test_database_tables():
    """Check what tables exist and their content"""
    print("\n=== Testing Database Tables ===")

    db = DatabaseManager()
    conn = db.get_connection()
    c = conn.cursor()

    try:
        # Check what tables exist
        c.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = c.fetchall()
        print("📊 Database tables:")
        for table in tables:
            print(f"   - {table[0]}")

        # Check orders table specifically
        c.execute("SELECT COUNT(*) FROM orders")
        order_count = c.fetchone()[0]
        print(f"📋 Total orders in database: {order_count}")

        if order_count > 0:
            c.execute("SELECT * FROM orders LIMIT 3")
            sample_orders = c.fetchall()
            print("   Sample orders:")
            for order in sample_orders:
                print(f"   - {order}")

        # Check products table
        c.execute("SELECT COUNT(*) FROM products")
        product_count = c.fetchone()[0]
        print(f"📦 Total products in database: {product_count}")

    except Exception as e:
        print(f"❌ Error checking database: {e}")
        import traceback
        traceback.print_exc()
    finally:
        conn.close()

if __name__ == "__main__":
    test_database_tables()
    test_orders_query()
    test_profile_loading()

#!/usr/bin/env python3
"""
Test script to verify the contact seller functionality
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_contact_seller_functionality():
    """Test the contact seller functionality"""
    print("=== Testing Contact Seller Functionality ===")

    db = DatabaseManager()

    # Test with existing sellers
    test_sellers = [
        ("8544757931", "jatin dadwal"),
        ("8598658456", "Lo"),
        ("6230329271", "Reema"),
        ("9999999999", "Test Seller")
    ]

    for phone, expected_name in test_sellers:
        print(f"\n--- Testing seller: {expected_name} ({phone}) ---")

        # Test get_seller_info method (simulating MarketplaceScreen.get_seller_info)
        try:
            conn = db.get_connection()
            c = conn.cursor()
            c.execute("SELECT name, email, location FROM users WHERE phone = ?", (phone,))
            result = c.fetchone()
            conn.close()

            if result:
                name, email, location = result
                seller_info = {
                    'name': name or "Unknown Seller",
                    'email': email,
                    'location': location
                }

                print(f"✅ Seller info retrieved:")
                print(f"   Name: {seller_info['name']}")
                print(f"   Phone: {phone}")
                print(f"   Email: {seller_info['email'] or 'Not provided'}")
                print(f"   Location: {seller_info['location'] or 'Not specified'}")

                # Simulate what the dialog would show
                print("   Dialog content preview:")
                print(f"   👤 {seller_info['name']}")
                print(f"   📞 {phone}")
                if seller_info['email']:
                    print(f"   ✉️ {seller_info['email']}")
                if seller_info['location']:
                    print(f"   📍 {seller_info['location']}")

            else:
                print("❌ Seller not found")

        except Exception as e:
            print(f"❌ Error getting seller info: {e}")
            import traceback
            traceback.print_exc()

def test_marketplace_products():
    """Test that products are available for contact seller testing"""
    print("\n=== Testing Marketplace Products ===")

    db = DatabaseManager()

    try:
        # Get all active products
        products = db.get_all_products()
        print(f"📦 Found {len(products)} products in marketplace")

        if products:
            print("   Sample products:")
            for i, product in enumerate(products[:3]):  # Show first 3
                product_id, seller_phone, name, category, variety, unit, price, quantity, description, image_path, status, created_at, updated_at = product
                print(f"   {i+1}. {name} - ₹{price}/{unit} (Seller: {seller_phone})")

                # Test seller info for this product
                try:
                    conn = db.get_connection()
                    c = conn.cursor()
                    c.execute("SELECT name FROM users WHERE phone = ?", (seller_phone,))
                    seller_result = c.fetchone()
                    conn.close()

                    seller_name = seller_result[0] if seller_result else "Unknown"
                    print(f"      Seller: {seller_name}")

                except Exception as e:
                    print(f"      Error getting seller name: {e}")

        else:
            print("❌ No products found in marketplace")

    except Exception as e:
        print(f"❌ Error getting products: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    test_marketplace_products()
    test_contact_seller_functionality()

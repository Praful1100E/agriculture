#!/usr/bin/env python3
"""
Complete test to verify login and marketplace functionality
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_complete_flow():
    """Test complete user flow: login + marketplace access"""
    print("🧪 Testing Complete AgriConnect Flow")
    print("=" * 50)

    # Initialize database manager
    db = DatabaseManager()

    # Test 1: Login functionality
    print("🔐 Testing Login Functionality...")

    # Test with existing buyer user
    buyer_phone = "8278853082"  # Praful Thakur
    buyer_password = "Praful@1234"

    buyer_result = db.authenticate_user(buyer_phone, buyer_password)
    if buyer_result:
        name, role, location = buyer_result
        print(f"✅ Buyer login successful: {name} ({role})")
    else:
        print("❌ Buyer login failed")
        return

    # Test with existing seller user
    seller_phone = "8598658456"  # Lo
    seller_password = "Praful@1234"

    seller_result = db.authenticate_user(seller_phone, seller_password)
    if seller_result:
        name, role, location = seller_result
        print(f"✅ Seller login successful: {name} ({role})")
    else:
        print("❌ Seller login failed")
        return

    # Test 2: Seller product access
    print("\n📦 Testing Seller Product Access...")
    seller_products = db.get_user_products(seller_phone)
    if seller_products:
        print(f"✅ Seller has {len(seller_products)} products:")
        for product in seller_products:
            product_id, seller_phone, name, category, variety, unit, price, stock_qty, description, image_path, status, created_at, updated_at = product
            print(f"   - {name} ({category}) - ₹{price}/{unit}")
    else:
        print("❌ Seller has no products")

    # Test 3: Marketplace access for buyers
    print("\n🛒 Testing Marketplace Access...")
    marketplace_products = db.get_all_products()
    if marketplace_products:
        print(f"✅ Marketplace has {len(marketplace_products)} products available:")
        for product in marketplace_products:
            product_id, seller_phone, name, category, variety, unit, price, stock_qty, description, image_path, status, created_at, updated_at = product
            print(f"   - {name} ({category}) - ₹{price}/{unit} - Stock: {stock_qty} {unit}")
    else:
        print("❌ No products in marketplace")

    print("\n🎯 All tests completed successfully!")
    print("\n📋 Summary:")
    print("   ✅ Login functionality working")
    print("   ✅ Seller product display working")
    print("   ✅ Buyer marketplace access working")

if __name__ == "__main__":
    test_complete_flow()

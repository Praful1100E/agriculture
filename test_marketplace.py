#!/usr/bin/env python3
"""
Test script to verify marketplace functionality
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager

def test_marketplace():
    """Test marketplace product loading"""
    print("🧪 Testing Marketplace Functionality")
    print("=" * 50)

    # Initialize database manager
    db = DatabaseManager()

    # Test getting all products
    print("📦 Testing get_all_products()...")
    products = db.get_all_products()

    if products:
        print(f"✅ Found {len(products)} products:")
        for product in products:
            product_id, seller_phone, name, category, variety, unit, price, stock_qty, description, image_path, status, created_at, updated_at = product
            print(f"   - {name} ({category}) - ₹{price}/{unit} - Stock: {stock_qty} {unit}")
    else:
        print("❌ No products found")

    print("\n📊 Testing get_available_products()...")
    available_products = db.get_available_products()

    if available_products:
        print(f"✅ Found {len(available_products)} available products")
    else:
        print("❌ No available products found")

    print("\n🎯 Marketplace test completed!")

if __name__ == "__main__":
    test_marketplace()

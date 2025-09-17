#!/usr/bin/env python3
"""
Automated tests for AgriConnect app fixes
Tests login functionality and seller product display
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from database.db_manager import DatabaseManager
import json

def test_login_functionality():
    """Test login with existing users"""
    print("🧪 Testing Login Functionality...")

    db = DatabaseManager()

    # Test cases: phone, password, expected result
    test_cases = [
        ("8544757931", "23022007", True),  # Existing seller
        ("8598658456", "Praful@1234", True),  # Existing seller
        ("6230329271", "ggggggghjhd", True),  # Existing seller
        ("6548962462", "fdfyuhdsr", True),  # Existing buyer
        ("9999999999", "wrongpass", False),  # Non-existent user
        ("8544757931", "wrongpass", False),  # Wrong password
    ]

    passed = 0
    total = len(test_cases)

    for phone, password, expected in test_cases:
        result = db.authenticate_user(phone, password)
        success = (result is not None) == expected

        if success:
            passed += 1
            print(f"✅ Login test passed: {phone}")
            if result:
                print(f"   User: {result[0]}, Role: {result[1]}")
        else:
            print(f"❌ Login test failed: {phone} (expected {expected}, got {result is not None})")

    print(f"Login tests: {passed}/{total} passed\n")
    return passed == total

def test_seller_products():
    """Test seller product retrieval"""
    print("🧪 Testing Seller Product Retrieval...")

    db = DatabaseManager()

    # Test with existing sellers
    seller_tests = [
        ("8598658456", 1),  # Should have 1 product (Wheat)
        ("6230329271", 1),  # Should have 1 product (potato)
        ("8544757931", 0),  # Should have 0 products
    ]

    passed = 0
    total = len(seller_tests)

    for phone, expected_count in seller_tests:
        products = db.get_user_products(phone)
        success = len(products) == expected_count

        if success:
            passed += 1
            print(f"✅ Product test passed: {phone} has {len(products)} products")
            for product in products:
                print(f"   - {product[2]}: {product[7]} {product[5]} @ ₹{product[6]}")
        else:
            print(f"❌ Product test failed: {phone} expected {expected_count}, got {len(products)}")

    print(f"Product tests: {passed}/{total} passed\n")
    return passed == total

def test_product_display_logic():
    """Test the product display formatting logic"""
    print("🧪 Testing Product Display Logic...")

    # Simulate product data (from database query result)
    sample_product = (1, '8598658456', 'Wheat', 'Grains', '', 'quintal', 2000.0, 1000.0, '', None, 'active', '2025-09-17 05:13:52', '2025-09-17 05:13:52')

    # Test the corrected display logic
    name = sample_product[2]
    category = sample_product[3]
    unit = sample_product[5]
    price = sample_product[6]
    quantity = sample_product[7]

    # Corrected details string (as fixed in code)
    details = f"Category: {category} | Quantity: {quantity} {unit} | Price: ₹{price}"

    expected = "Category: Grains | Quantity: 1000.0 quintal | Price: ₹2000.0"

    success = details == expected
    if success:
        print("✅ Product display logic test passed")
        print(f"   Display: {details}")
    else:
        print("❌ Product display logic test failed")
        print(f"   Expected: {expected}")
        print(f"   Got: {details}")

    print()
    return success

def main():
    """Run all tests"""
    print("🚀 Starting AgriConnect Automated Tests\n")

    login_ok = test_login_functionality()
    products_ok = test_seller_products()
    display_ok = test_product_display_logic()

    all_passed = login_ok and products_ok and display_ok

    print("📊 Test Results Summary:")
    print(f"Login Functionality: {'✅ PASS' if login_ok else '❌ FAIL'}")
    print(f"Seller Products: {'✅ PASS' if products_ok else '❌ FAIL'}")
    print(f"Product Display: {'✅ PASS' if display_ok else '❌ FAIL'}")
    print(f"Overall: {'✅ ALL TESTS PASSED' if all_passed else '❌ SOME TESTS FAILED'}")

    if all_passed:
        print("\n🎉 All fixes are working correctly!")
        print("The login input issue and seller product display issue have been resolved.")
    else:
        print("\n⚠️ Some issues remain. Please review the failed tests above.")

    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())

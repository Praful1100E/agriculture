# screens/screen_manager_debug_fixed.py - Debug version with fixed buyer screens
from kivy.uix.screenmanager import ScreenManager, NoTransition

from screens.auth_screens_debug import LoginScreen, RegisterScreen
from screens.seller_screens_debug import ProductListScreen
from screens.seller_screens import SellerDashboard, AddProductScreen, BulkUpdateScreen
from screens.buyer_screens_fixed import BuyerDashboard, CartScreen, CheckoutScreen
from screens.common_screens import SchemesScreen, ProfileScreen, MarketPricesScreen, OrdersScreen
from screens.address_screens import AddressScreen, PaymentMethodScreen

def create_screen_manager(app):
    """Create and configure screen manager with all screens"""
    sm = ScreenManager(transition=NoTransition())

    # Add all screens
    sm.add_widget(LoginScreen(name="login", app=app))
    sm.add_widget(RegisterScreen(name="register", app=app))
    sm.add_widget(SellerDashboard(name="seller_dashboard", app=app))
    sm.add_widget(BuyerDashboard(name="buyer_dashboard", app=app))
    sm.add_widget(ProductListScreen(name="product_list", app=app))
    sm.add_widget(AddProductScreen(name="add_product", app=app))
    sm.add_widget(BulkUpdateScreen(name="bulk_update", app=app))
    sm.add_widget(CartScreen(name="cart", app=app))
    sm.add_widget(CheckoutScreen(name="checkout", app=app))
    sm.add_widget(SchemesScreen(name="schemes", app=app))
    sm.add_widget(ProfileScreen(name="profile", app=app))
    sm.add_widget(MarketPricesScreen(name="market_prices", app=app))
    sm.add_widget(OrdersScreen(name="orders", app=app))
    sm.add_widget(AddressScreen(name="address", app=app))
    sm.add_widget(PaymentMethodScreen(name="payment_method", app=app))

    return sm

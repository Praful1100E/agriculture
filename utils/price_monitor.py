# utils/price_monitor.py - Price monitoring and alert system
import random
import threading
from datetime import datetime
from kivymd.uix.snackbar import Snackbar

# Sample market data for price simulation
MARKET_DATA = {
    "Tomatoes": {"base_price": 25, "volatility": 0.15},
    "Onions": {"base_price": 30, "volatility": 0.12},
    "Wheat": {"base_price": 22, "volatility": 0.08},
    "Rice": {"base_price": 45, "volatility": 0.10},
    "Potatoes": {"base_price": 18, "volatility": 0.20},
    "Apples": {"base_price": 80, "volatility": 0.05},
    "Bananas": {"base_price": 35, "volatility": 0.18},
}

class PriceMonitor:
    def __init__(self, app):
        self.app = app
        self.last_prices = {}

    def check_price_updates(self, dt):
        """Check for price updates and send alerts (called periodically)"""
        if not self.app.store.exists("session"):
            return

        session = self.app.store.get("session")
        if session.get("role") != "seller":
            return

        # Run price check in background thread
        threading.Thread(target=self._background_price_check, daemon=True).start()

    def _background_price_check(self):
        """Background task to check price updates"""
        try:
            phone = self.app.store.get("session")["phone"]
            products = self.app.db_manager.get_user_products(phone)

            for product in products:
                product_name = product[2]  # name column
                current_seller_price = product[6]  # price column

                # Simulate market price check
                if product_name in MARKET_DATA:
                    market_data = MARKET_DATA[product_name]
                    base_price = market_data["base_price"]
                    volatility = market_data["volatility"]

                    # Simulate market price with volatility
                    current_market_price = base_price * (1 + random.uniform(-volatility, volatility))

                    # Check if price increased significantly (>5%)
                    last_price = self.last_prices.get(product_name, current_market_price)
                    price_increase_percent = (current_market_price - last_price) / last_price * 100

                    if price_increase_percent > 5.0:
                        self._send_price_alert(product_name, current_market_price, price_increase_percent)

                    # Update last known price
                    self.last_prices[product_name] = current_market_price

        except Exception as e:
            print(f"Error in price monitoring: {e}")

    def _send_price_alert(self, product_name, new_price, increase_percent):
        """Send price increase alert"""
        try:
            message = f"🚀 {product_name} price rising! Market: ₹{new_price:.2f} (+{increase_percent:.1f}%). Update your listing!"

            # Schedule snackbar on main thread
            from kivy.clock import Clock
            Clock.schedule_once(lambda dt: Snackbar(text=message, duration=5).open(), 0)

            # Try system notification if available
            try:
                from plyer import notification
                notification.notify(
                    title="Price Alert 📈",
                    message=f"{product_name} price increased by {increase_percent:.1f}%",
                    timeout=10
                )
            except:
                pass  # Notification not available

        except Exception as e:
            print(f"Error sending price alert: {e}")

    def get_ai_price_suggestion(self, product_name):
        """Get AI-powered price suggestion"""
        if product_name in MARKET_DATA:
            market_data = MARKET_DATA[product_name]
            base_price = market_data["base_price"]
            volatility = market_data["volatility"]

            # Simulate current market conditions
            suggested_price = base_price * (1 + random.uniform(-volatility/2, volatility))
            return round(suggested_price, 2)
        else:
            # Generic suggestion for unknown products
            return round(random.uniform(20, 100), 2)
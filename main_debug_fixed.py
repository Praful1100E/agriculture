# main_debug_fixed.py - Debug version with fixed screen manager
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.storage.jsonstore import JsonStore
import os

# FORCE MOBILE PHONE DIMENSIONS
Window.size = (360, 640)  # Standard mobile phone dimensions (9:16 ratio)
Window.minimum_width = 300
Window.minimum_height = 500

# Import your modules
from database.db_manager import DatabaseManager
from screens.screen_manager_debug_fixed import create_screen_manager

class AgriConnectApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.title = "AgriConnect - Smart Farming Platform"
        self.theme_cls.primary_palette = "Green"
        self.theme_cls.theme_style = "Light"

        # Database setup
        self.db_manager = DatabaseManager()
        self.db_manager.init_database()

        # Storage for session management
        self.store = JsonStore('data/user_session.json')

    def build(self):
        # Create and return screen manager
        sm = create_screen_manager(self)
        return sm

    def load_dashboard_data(self, role):
        """Load data for dashboard based on user role"""
        print(f"DEBUG: load_dashboard_data called with role: {role}")  # Debug print
        if role == "seller":
            # Load seller-specific data
            print("DEBUG: Loading seller data")  # Debug print
            pass
        else:
            # Load buyer-specific data
            print("DEBUG: Loading buyer data")  # Debug print
            pass

    def logout(self):
        """Handle user logout"""
        if self.store.exists("session"):
            self.store.delete("session")
        self.root.current = "login"

    def go_back_to_dashboard(self):
        """Navigate back to appropriate dashboard"""
        if self.store.exists("session"):
            role = self.store.get("session")["role"]
            next_screen = "seller_dashboard" if role == "seller" else "buyer_dashboard"
            self.root.current = next_screen
        else:
            self.root.current = "login"

if __name__ == "__main__":
    AgriConnectApp().run()

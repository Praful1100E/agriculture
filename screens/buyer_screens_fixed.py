# screens/buyer_screens.py - Buyer Screens (FIXED)
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

# Use the newer MDSnackbar instead of deprecated Snackbar
try:
    from kivymd.uix.snackbar import MDSnackbar
    from kivymd.uix.label import MDLabel
    use_md_snackbar = True
except ImportError:
    from kivymd.uix.snackbar import Snackbar
    use_md_snackbar = False

def show_message(message):
    """Universal message function for all KivyMD versions"""
    try:
        if use_md_snackbar:
            snackbar = MDSnackbar(
                MDLabel(
                    text=message,
                    theme_text_color="Custom",
                    text_color=(1, 1, 1, 1)
                ),
                y="24dp",
                pos_hint={"center_x": 0.5},
                size_hint_x=0.9,
                duration=3
            )
            snackbar.open()
        else:
            snackbar = Snackbar()
            snackbar.text = message
            snackbar.duration = 3
            snackbar.open()
    except Exception as e:
        print(f"MESSAGE: {message}")

Builder.load_string("""
<BuyerDashboard>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "🛒 Buyer Dashboard"
            right_action_items: [["cart", lambda x: root.go_to_cart()], ["account-circle", lambda x: root.go_to_profile()], ["logout", lambda x: root.logout()]]
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "15dp"
                padding: "20dp"
                size_hint_y: None
                height: self.minimum_height

                MDCard:
                    size_hint_y: None
                    height: "120dp"
                    elevation: 5
                    radius: [10]
                    padding: "20dp"
                    MDLabel:
                        text: "Welcome to Agrimart Marketplace!\\n\\nDiscover fresh products directly from farmers."
                        halign: "center"
                        font_style: "Subtitle1"
                        theme_text_color: "Primary"

                MDTextField:
                    hint_text: "Search products..."
                    icon_right: "magnify"
                    size_hint_y: None
                    height: "60dp"

                MDLabel:
                    text: "Quick Actions"
                    font_style: "H6"
                    size_hint_y: None
                    height: "40dp"
                    theme_text_color: "Primary"

                MDBoxLayout:
                    size_hint_y: None
                    height: "80dp"
                    spacing: "10dp"
                    MDRaisedButton:
                        text: "🛒 Browse Products"
                        on_release: root.browse_products()
                    MDRaisedButton:
                        text: "📋 My Orders"
                        on_release: root.go_to_orders()

                MDRaisedButton:
                    text: "🏛️ Government Schemes"
                    size_hint_y: None
                    height: "60dp"
                    on_release: root.go_to_schemes()

<CartScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "🛒 Shopping Cart"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDLabel:
            text: "Your cart items will appear here.\\n\\nAdd products to see them in your cart."
            halign: "center"
            font_style: "Subtitle1"

<CheckoutScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "💳 Checkout"
            left_action_items: [["arrow-left", lambda x: root.go_to_cart()]]
        MDLabel:
            text: "Checkout process coming soon!"
            halign: "center"
            font_style: "Subtitle1"
""")

class BuyerDashboard(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def load_products(self):
        pass

    def go_to_cart(self):
        self.app.root.current = "cart"

    def go_to_profile(self):
        self.app.root.current = "profile"

    def logout(self):
        self.app.logout()

    def browse_products(self):
        show_message("Product browsing coming soon!")

    def go_to_orders(self):
        self.app.root.current = "orders"

    def go_to_schemes(self):
        self.app.root.current = "schemes"

class CartScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def go_back(self):
        self.app.go_back_to_dashboard()

class CheckoutScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def go_to_cart(self):
        self.app.root.current = "cart"

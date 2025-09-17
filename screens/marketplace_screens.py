# screens/marketplace_screens.py - Marketplace for buyers to browse products
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.label import MDLabel
from kivymd.uix.card import MDCard
from kivymd.uix.boxlayout import MDBoxLayout

def show_snackbar(message):
    """Helper function for KivyMD 1.2.0 compatibility"""
    try:
        snackbar = Snackbar()
        snackbar.text = message
        snackbar.duration = 3
        snackbar.open()
    except Exception as e:
        print(f"Message: {message}")

Builder.load_string("""
<MarketplaceScreen>:
    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "🛒 Marketplace"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            right_action_items: [["cart", lambda x: root.go_to_cart()]]

        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "10dp"
                padding: "15dp"
                size_hint_y: None
                height: self.minimum_height
                id: products_container
""")

class MarketplaceScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def on_enter(self):
        """Load products when entering the screen"""
        self.load_products()

    def load_products(self):
        """Load all available products from all sellers"""
        container = self.ids.products_container
        container.clear_widgets()

        if not self.app.store.exists("session"):
            show_snackbar("Please login first")
            return

        try:
            # Get all active products
            products = self.app.db_manager.get_all_products()

            if not products:
                # No products available
                no_products_card = MDCard(
                    size_hint_y=None,
                    height="200dp",
                    elevation=5,
                    radius=[10],
                    padding="20dp"
                )

                no_products_layout = MDBoxLayout(
                    orientation="vertical",
                    spacing="10dp"
                )

                no_products_label = MDLabel(
                    text="No products available at the moment.\\n\\nCheck back later!",
                    halign="center",
                    font_style="Subtitle1",
                    theme_text_color="Secondary"
                )

                no_products_layout.add_widget(no_products_label)
                no_products_card.add_widget(no_products_layout)
                container.add_widget(no_products_card)
                return

            # Display products
            for product in products:
                product_card = self.create_product_card(product)
                container.add_widget(product_card)

        except Exception as e:
            show_snackbar("Error loading products")
            print(f"Error loading products: {e}")

    def create_product_card(self, product):
        """Create a card for each product"""
        # Unpack product data
        product_id, seller_phone, name, category, variety, unit, price, quantity, description, image_path, status, created_at, updated_at = product

        card = MDCard(
            size_hint_y=None,
            height="180dp",
            elevation=5,
            radius=[10],
            padding="15dp"
        )

        layout = MDBoxLayout(
            orientation="vertical",
            spacing="5dp"
        )

        # Product name and category
        title_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="30dp"
        )

        product_name = MDLabel(
            text=f"{name}",
            font_style="H6",
            theme_text_color="Primary",
            size_hint_x=0.7
        )

        category_label = MDLabel(
            text=f"{category}",
            font_style="Caption",
            theme_text_color="Secondary",
            halign="right",
            size_hint_x=0.3
        )

        title_layout.add_widget(product_name)
        title_layout.add_widget(category_label)

        # Variety if available
        variety_text = f" ({variety})" if variety else ""
        variety_label = MDLabel(
            text=f"Variety:{variety_text}",
            font_style="Body2",
            theme_text_color="Secondary",
            size_hint_y=None,
            height="20dp"
        )

        # Price and quantity
        price_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="30dp"
        )

        price_label = MDLabel(
            text=f"₹{price:.2f} per {unit}",
            font_style="H6",
            theme_text_color="Primary",
            size_hint_x=0.5
        )

        quantity_label = MDLabel(
            text=f"Available: {quantity} {unit}",
            font_style="Body2",
            theme_text_color="Secondary",
            halign="right",
            size_hint_x=0.5
        )

        price_layout.add_widget(price_label)
        price_layout.add_widget(quantity_label)

        # Description (truncated)
        desc_text = description[:50] + "..." if description and len(description) > 50 else description or ""
        description_label = MDLabel(
            text=desc_text,
            font_style="Body2",
            theme_text_color="Secondary",
            size_hint_y=None,
            height="30dp"
        )

        # Add to cart button
        button_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="40dp",
            spacing="10dp"
        )

        add_to_cart_btn = MDRaisedButton(
            text="Add to Cart",
            size_hint_x=0.6,
            on_release=lambda x, p=product: self.add_to_cart(p)
        )

        contact_btn = MDRaisedButton(
            text="Contact Seller",
            size_hint_x=0.4,
            md_bg_color=[0.2, 0.7, 0.2, 1],  # Green
            on_release=lambda x, p=product: self.contact_seller(p)
        )

        button_layout.add_widget(add_to_cart_btn)
        button_layout.add_widget(contact_btn)

        # Add all elements to layout
        layout.add_widget(title_layout)
        if variety:
            layout.add_widget(variety_label)
        layout.add_widget(price_layout)
        if desc_text:
            layout.add_widget(description_label)
        layout.add_widget(button_layout)

        card.add_widget(layout)
        return card

    def add_to_cart(self, product):
        """Add product to cart"""
        if not self.app.store.exists("session"):
            show_snackbar("Please login first")
            return

        buyer_phone = self.app.store.get("session")["phone"]
        product_id = product[0]
        product_name = product[2]

        # Add to cart with quantity 1 (can be modified later)
        success = self.app.db_manager.add_to_cart(buyer_phone, product_id, 1)

        if success:
            show_snackbar(f"✅ Added {product_name} to cart!")
        else:
            show_snackbar("❌ Failed to add to cart")

    def contact_seller(self, product):
        """Contact seller functionality"""
        seller_phone = product[1]
        seller_info = self.get_seller_info(seller_phone)

        # Instead of snackbar, show a popup with detailed contact information
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton, MDRaisedButton
        from kivymd.uix.boxlayout import MDBoxLayout
        from kivymd.uix.label import MDLabel

        # Create custom content layout
        content_layout = MDBoxLayout(
            orientation="vertical",
            spacing="10dp",
            padding="10dp",
            size_hint_y=None,
            height="120dp"
        )

        # Seller name
        name_label = MDLabel(
            text=f"👤 {seller_info['name']}",
            font_style="H6",
            halign="center",
            theme_text_color="Primary"
        )

        # Phone number
        phone_label = MDLabel(
            text=f"📞 {seller_phone}",
            font_style="Subtitle1",
            halign="center",
            theme_text_color="Secondary"
        )

        # Email if available
        email_text = f"✉️ {seller_info['email']}" if seller_info['email'] else ""
        email_label = MDLabel(
            text=email_text,
            font_style="Body2",
            halign="center",
            theme_text_color="Secondary"
        )

        # Location if available
        location_text = f"📍 {seller_info['location']}" if seller_info['location'] else ""
        location_label = MDLabel(
            text=location_text,
            font_style="Body2",
            halign="center",
            theme_text_color="Secondary"
        )

        content_layout.add_widget(name_label)
        content_layout.add_widget(phone_label)
        if seller_info['email']:
            content_layout.add_widget(email_label)
        if seller_info['location']:
            content_layout.add_widget(location_label)

        def close_dialog(obj):
            dialog.dismiss()

        def call_seller(obj):
            # In a real app, this would initiate a phone call
            show_snackbar(f"📞 Calling {seller_info['name']}...")
            dialog.dismiss()

        dialog = MDDialog(
            title="Contact Seller",
            type="custom",
            content_cls=content_layout,
            size_hint=(0.9, None),
            height="300dp",
            buttons=[
                MDRaisedButton(text="📞 Call", on_release=call_seller, md_bg_color=[0.2, 0.7, 0.2, 1]),
                MDFlatButton(text="Close", on_release=close_dialog)
            ],
        )
        dialog.open()

    def get_seller_name(self, seller_phone):
        """Get seller name from phone number"""
        try:
            conn = self.app.db_manager.get_connection()
            c = conn.cursor()
            c.execute("SELECT name FROM users WHERE phone = ?", (seller_phone,))
            result = c.fetchone()
            conn.close()
            return result[0] if result else "Seller"
        except Exception as e:
            print(f"Error getting seller name: {e}")
            return "Seller"

    def get_seller_info(self, seller_phone):
        """Get detailed seller information"""
        try:
            conn = self.app.db_manager.get_connection()
            c = conn.cursor()
            c.execute("SELECT name, email, location FROM users WHERE phone = ?", (seller_phone,))
            result = c.fetchone()
            conn.close()

            if result:
                name, email, location = result
                return {
                    'name': name or "Unknown Seller",
                    'email': email,
                    'location': location
                }
            else:
                return {
                    'name': "Unknown Seller",
                    'email': None,
                    'location': None
                }
        except Exception as e:
            print(f"Error getting seller info: {e}")
            return {
                'name': "Unknown Seller",
                'email': None,
                'location': None
            }

    def go_back(self):
        """Go back to buyer dashboard"""
        self.app.go_back_to_dashboard()

    def go_to_cart(self):
        """Go to cart screen"""
        self.manager.current = "cart"

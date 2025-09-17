# screens/seller_screens.py - DEBUG VERSION
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.metrics import dp
from kivymd.uix.snackbar import Snackbar
from kivymd.uix.menu import MDDropdownMenu

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
<ProductListScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "📦 My Products"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            right_action_items: [["refresh", lambda x: root.load_products()]]
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "10dp"
                padding: "15dp"
                size_hint_y: None
                height: self.minimum_height
                id: products_container
""")

class ProductListScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def on_enter(self):
        print("DEBUG: ProductListScreen.on_enter called")  # Debug print
        self.load_products()

    def load_products(self):
        """Load and display user's products"""
        print("DEBUG: load_products called")  # Debug print

        if not self.app.store.exists("session"):
            print("DEBUG: No session found")  # Debug print
            show_snackbar("Please login first")
            return

        phone = self.app.store.get("session")["phone"]
        role = self.app.store.get("session")["role"]
        print(f"DEBUG: Loading products for phone: {phone}, role: {role}")  # Debug print

        products = self.app.db_manager.get_user_products(phone)
        print(f"DEBUG: Retrieved {len(products)} products from database")  # Debug print

        # Clear existing products
        self.ids.products_container.clear_widgets()

        if not products:
            print("DEBUG: No products found, showing empty state")  # Debug print
            # Show empty state
            from kivymd.uix.label import MDLabel
            empty_label = MDLabel(
                text="No products found.\\n\\nAdd products to see them here.",
                halign="center",
                font_style="Subtitle1",
                theme_text_color="Secondary"
            )
            self.ids.products_container.add_widget(empty_label)
            return

        print("DEBUG: Displaying products")  # Debug print
        # Display products
        for product in products:
            print(f"DEBUG: Adding product card for: {product[2]}")  # Debug print
            self.add_product_card(product)

    def add_product_card(self, product):
        """Add a product card to the container"""
        from kivymd.uix.card import MDCard
        from kivymd.uix.boxlayout import MDBoxLayout
        from kivymd.uix.label import MDLabel
        from kivymd.uix.button import MDRaisedButton

        # Product card
        card = MDCard(
            size_hint_y=None,
            height="150dp",
            elevation=3,
            radius=[8],
            padding="12dp"
        )

        # Main layout
        main_layout = MDBoxLayout(
            orientation="vertical",
            spacing="8dp"
        )

        # Product name and category
        title_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="30dp"
        )

        name_label = MDLabel(
            text=f"{product[2]}",  # name
            font_style="H6",
            bold=True,
            size_hint_x=0.7
        )

        category_label = MDLabel(
            text=f"{product[3]}",  # category
            font_style="Caption",
            halign="right",
            theme_text_color="Secondary",
            size_hint_x=0.3
        )

        title_layout.add_widget(name_label)
        title_layout.add_widget(category_label)

        # Details layout
        details_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="40dp",
            spacing="10dp"
        )

        # Price
        price_label = MDLabel(
            text=f"₹{product[6]:.2f}/{product[5]}",  # price/unit
            font_style="Subtitle1",
            theme_text_color="Primary",
            size_hint_x=0.3
        )

        # Stock
        stock_label = MDLabel(
            text=f"Stock: {product[7]} {product[5]}",  # stock_qty unit
            font_style="Body2",
            size_hint_x=0.4
        )

        # Status
        status_label = MDLabel(
            text=f"Status: {product[10] or 'Active'}",  # status
            font_style="Body2",
            halign="right",
            size_hint_x=0.3
        )

        details_layout.add_widget(price_label)
        details_layout.add_widget(stock_label)
        details_layout.add_widget(status_label)

        # Description (if exists)
        if product[8]:  # description
            desc_label = MDLabel(
                text=product[8][:100] + "..." if len(product[8]) > 100 else product[8],
                font_style="Body2",
                theme_text_color="Secondary",
                size_hint_y=None,
                height="30dp"
            )
            main_layout.add_widget(desc_label)

        # Action buttons
        buttons_layout = MDBoxLayout(
            orientation="horizontal",
            size_hint_y=None,
            height="40dp",
            spacing="10dp"
        )

        edit_btn = MDRaisedButton(
            text="Edit",
            size_hint_x=0.5,
            on_release=lambda x, p=product: self.edit_product(p)
        )

        delete_btn = MDRaisedButton(
            text="Delete",
            size_hint_x=0.5,
            md_bg_color=(0.8, 0.2, 0.2, 1),
            on_release=lambda x, p=product: self.delete_product(p)
        )

        buttons_layout.add_widget(edit_btn)
        buttons_layout.add_widget(delete_btn)

        # Add all to main layout
        main_layout.add_widget(title_layout)
        main_layout.add_widget(details_layout)
        main_layout.add_widget(buttons_layout)

        card.add_widget(main_layout)
        self.ids.products_container.add_widget(card)

    def edit_product(self, product):
        """Navigate to edit product screen (placeholder)"""
        show_snackbar("Edit functionality coming soon!")

    def delete_product(self, product):
        """Delete a product"""
        from kivymd.uix.dialog import MDDialog
        from kivymd.uix.button import MDFlatButton

        def delete_callback(instance):
            try:
                # Note: Need to add delete_product method to db_manager
                # For now, just show message
                show_snackbar(f"Delete functionality for {product[2]} coming soon!")
                dialog.dismiss()
            except Exception as e:
                show_snackbar("Error deleting product")

        def cancel_callback(instance):
            dialog.dismiss()

        dialog = MDDialog(
            title="Delete Product",
            text=f"Are you sure you want to delete '{product[2]}'?",
            buttons=[
                MDFlatButton(text="Cancel", on_release=cancel_callback),
                MDFlatButton(text="Delete", on_release=delete_callback)
            ]
        )
        dialog.open()

    def go_back(self):
        self.app.go_back_to_dashboard()

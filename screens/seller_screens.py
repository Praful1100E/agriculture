# screens/seller_screens.py - KivyMD 1.2.0 Compatible
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
<SellerDashboard>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "🌾 Farmer Dashboard"
            right_action_items: [["account-circle", lambda x: root.go_to_profile()], ["logout", lambda x: root.logout()]]
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
                        text: "Welcome to your Farmer Dashboard!\\n\\nManage products, track orders, and access government schemes."
                        halign: "center"
                        font_style: "Subtitle1"
                        theme_text_color: "Primary"
                
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
                        text: "➕ Add Product"
                        on_release: root.go_to_add_product()
                    MDRaisedButton:
                        text: "📦 My Products"
                        on_release: root.go_to_product_list()
                
                MDBoxLayout:
                    size_hint_y: None
                    height: "80dp" 
                    spacing: "10dp"
                    MDRaisedButton:
                        text: "📋 Orders"
                        on_release: root.go_to_orders()
                    MDRaisedButton:
                        text: "💰 Market Prices"
                        on_release: root.go_to_market_prices()
                
                MDRaisedButton:
                    text: "🏛️ Government Schemes"
                    size_hint_y: None
                    height: "60dp"
                    on_release: root.go_to_schemes()

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

<AddProductScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "➕ Add Product"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "15dp"
                padding: "20dp"
                size_hint_y: None
                height: "800dp"
                
                MDCard:
                    size_hint_y: None
                    height: "100dp"
                    elevation: 3
                    padding: "15dp"
                    MDLabel:
                        text: "Add New Product to Your Inventory"
                        halign: "center"
                        font_style: "H6"
                        theme_text_color: "Primary"
                
                MDTextField:
                    id: product_name
                    hint_text: "Product Name"
                    helper_text: "e.g., Tomatoes, Wheat, Rice"
                    helper_text_mode: "on_focus"
                    size_hint_y: None
                    height: "70dp"
                
                MDDropDownItem:
                    id: category_dropdown
                    text: "Select Category"
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "56dp"
                    on_release: root.open_category_menu()

                MDTextField:
                    id: variety
                    hint_text: "Variety (Optional)"
                    helper_text: "e.g., Hybrid, Organic"
                    helper_text_mode: "on_focus"
                    size_hint_y: None
                    height: "70dp"

                MDTextField:
                    id: quantity
                    hint_text: "Quantity Available"
                    helper_text: "Enter quantity in numbers"
                    helper_text_mode: "on_focus"
                    size_hint_y: None
                    height: "70dp"

                MDDropDownItem:
                    id: unit_dropdown
                    text: "Select Unit"
                    pos_hint: {"center_x": 0.5}
                    size_hint_y: None
                    height: "56dp"
                    on_release: root.open_unit_menu()
                
                MDTextField:
                    id: price
                    hint_text: "Price per unit (₹)"
                    helper_text: "Price in rupees"
                    helper_text_mode: "on_focus"
                    size_hint_y: None
                    height: "70dp"
                
                MDTextField:
                    id: description
                    hint_text: "Description (Optional)"
                    helper_text: "Quality, farming method, etc."
                    helper_text_mode: "on_focus"
                    multiline: True
                    size_hint_y: None
                    height: "100dp"
                
                MDRaisedButton:
                    text: "✅ Add Product"
                    size_hint_y: None
                    height: "50dp"
                    on_release: root.add_product()

<BulkUpdateScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "📊 Bulk Update"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDLabel:
            text: "Bulk update functionality coming soon!\\n\\nUpdate multiple products at once."
            halign: "center"
            font_style: "Subtitle1"
""")

class SellerDashboard(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
    
    def update_stats(self, products):
        pass
    
    def go_to_profile(self):
        self.app.root.current = "profile"
    
    def logout(self):
        self.app.logout()
    
    def go_to_add_product(self):
        self.app.root.current = "add_product"
    
    def go_to_product_list(self):
        self.app.root.current = "product_list"
    
    def go_to_orders(self):
        self.app.root.current = "orders"
    
    def go_to_market_prices(self):
        self.app.root.current = "market_prices"
    
    def go_to_schemes(self):
        self.app.root.current = "schemes"

class ProductListScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def on_enter(self):
        self.load_products()

    def load_products(self):
        """Load and display user's products"""
        print("DEBUG: load_products called")
        if not self.app.store.exists("session"):
            show_snackbar("Please login first")
            print("DEBUG: No session found")
            return

        phone = self.app.store.get("session")["phone"]
        role = self.app.store.get("session")["role"]
        print(f"DEBUG: Loading products for {role} - phone: {phone}")

        products = self.app.db_manager.get_user_products(phone)
        print(f"DEBUG: Found {len(products)} products")

        # Clear existing products
        self.ids.products_container.clear_widgets()

        if not products:
            # Show empty state
            from kivymd.uix.label import MDLabel
            empty_label = MDLabel(
                text="No products found.\\n\\nAdd products to see them here.",
                halign="center",
                font_style="Subtitle1",
                theme_text_color="Secondary"
            )
            self.ids.products_container.add_widget(empty_label)
            print("DEBUG: Showing empty state")
            return

        # Display products
        for i, product in enumerate(products):
            print(f"DEBUG: Adding product {i+1}: {product[2]}")
            self.add_product_card(product)
        print("DEBUG: Finished loading products")

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

class AddProductScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.category_menu = None
        self.unit_menu = None

    def on_enter(self):
        self.setup_dropdowns()

    def setup_dropdowns(self):
        # Category dropdown
        categories = ["Vegetables", "Fruits", "Grains", "Pulses", "Spices", "Dairy", "Other"]
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": category,
                "height": dp(56),
                "on_release": lambda x=category: self.set_category(x),
            } for category in categories
        ]
        self.category_menu = MDDropdownMenu(
            caller=self.ids.category_dropdown,
            items=menu_items,
            position="center",
            width_mult=4,
        )

        # Unit dropdown
        units = ["kg", "quintal", "ton", "litre", "dozen", "piece", "bundle"]
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": unit,
                "height": dp(56),
                "on_release": lambda x=unit: self.set_unit(x),
            } for unit in units
        ]
        self.unit_menu = MDDropdownMenu(
            caller=self.ids.unit_dropdown,
            items=menu_items,
            position="center",
            width_mult=4,
        )

    def open_category_menu(self):
        if self.category_menu:
            self.category_menu.open()

    def open_unit_menu(self):
        if self.unit_menu:
            self.unit_menu.open()

    def set_category(self, category):
        self.ids.category_dropdown.text = category
        self.category_menu.dismiss()

    def set_unit(self, unit):
        self.ids.unit_dropdown.text = unit
        self.unit_menu.dismiss()

    def go_back(self):
        self.app.go_back_to_dashboard()

    def add_product(self):
        if not self.app.store.exists("session"):
            show_snackbar("Please login first")
            return

        phone = self.app.store.get("session")["phone"]

        try:
            name = self.ids.product_name.text.strip()
            category = self.ids.category_dropdown.text
            variety = self.ids.variety.text.strip()
            quantity = self.ids.quantity.text.strip()
            unit = self.ids.unit_dropdown.text
            price = self.ids.price.text.strip()
            description = self.ids.description.text.strip()

            if category == "Select Category":
                category = ""
            if unit == "Select Unit":
                unit = ""

            if not all([name, category, quantity, unit, price]):
                show_snackbar("Please fill all required fields")
                return

            try:
                quantity = float(quantity)
                price = float(price)
            except ValueError:
                show_snackbar("Quantity and price must be valid numbers")
                return

            if quantity <= 0 or price <= 0:
                show_snackbar("Quantity and price must be positive")
                return

            product_id = self.app.db_manager.add_product(
                phone, name, category, variety, unit, price, quantity, description
            )

            if product_id:
                self.ids.product_name.text = ""
                self.ids.category_dropdown.text = "Select Category"
                self.ids.variety.text = ""
                self.ids.quantity.text = ""
                self.ids.unit_dropdown.text = "Select Unit"
                self.ids.price.text = ""
                self.ids.description.text = ""

                show_snackbar(f"✅ {name} added successfully!")

                # Navigate back to product list and refresh
                self.app.root.current = "product_list"
            else:
                show_snackbar("Failed to add product")

        except Exception as e:
            show_snackbar("Error adding product")

class BulkUpdateScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
    
    def go_back(self):
        self.app.go_back_to_dashboard()

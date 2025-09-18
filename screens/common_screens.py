# screens/common_screens.py - Common Screens (FIXED)
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivymd.uix.list import ThreeLineListItem

Builder.load_string("""
<SchemesScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "🏛️ Government Schemes"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "10dp"
                padding: "15dp"
                size_hint_y: None
                height: self.minimum_height
                
                MDCard:
                    size_hint_y: None
                    height: "80dp"
                    elevation: 3
                    padding: "15dp"
                    radius: [10]
                    MDLabel:
                        text: "🌾 Agricultural Schemes for Farmers"
                        halign: "center"
                        font_style: "H6"
                        theme_text_color: "Primary"
                
                MDList:
                    id: schemes_list

<ProfileScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "👤 Profile"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
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
                    radius: [15]
                    padding: "20dp"
                    md_bg_color: (0.2, 0.7, 0.2, 1)
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "5dp"
                        MDLabel:
                            id: profile_name
                            text: "Loading..."
                            halign: "center"
                            font_style: "H5"
                            bold: True
                            theme_text_color: "Custom"
                            text_color: (1, 1, 1, 1)
                        MDLabel:
                            id: profile_role
                            text: ""
                            halign: "center"
                            font_style: "Subtitle1"
                            theme_text_color: "Custom"
                            text_color: (1, 1, 1, 0.9)

                MDCard:
                    size_hint_y: None
                    height: "200dp"
                    elevation: 3
                    radius: [10]
                    padding: "15dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "10dp"
                        MDLabel:
                            text: "📞 Contact Information"
                            font_style: "H6"
                            theme_text_color: "Primary"
                        
                        MDBoxLayout:
                            orientation: "horizontal"
                            size_hint_y: None
                            height: "40dp"
                            MDLabel:
                                text: "Phone:"
                                font_style: "Body1"
                                bold: True
                                size_hint_x: 0.3
                            MDLabel:
                                id: profile_phone
                                text: ""
                                font_style: "Body1"
                                size_hint_x: 0.7

                        MDBoxLayout:
                            orientation: "horizontal"
                            size_hint_y: None
                            height: "40dp"
                            MDLabel:
                                text: "Name:"
                                font_style: "Body1"
                                bold: True
                                size_hint_x: 0.3
                            MDLabel:
                                id: profile_name_value
                                text: ""
                                font_style: "Body1"
                                size_hint_x: 0.7
                                opacity: 1
                            MDTextField:
                                id: profile_name_input
                                hint_text: "Enter your name"
                                font_style: "Body1"
                                size_hint_x: 0.7
                                opacity: 0

                        MDBoxLayout:
                            orientation: "horizontal"
                            size_hint_y: None
                            height: "40dp"
                            MDLabel:
                                text: "Email:"
                                font_style: "Body1"
                                bold: True
                                size_hint_x: 0.3
                            MDLabel:
                                id: profile_email
                                text: ""
                                font_style: "Body1"
                                size_hint_x: 0.7
                                opacity: 1
                            MDTextField:
                                id: profile_email_input
                                hint_text: "Enter your email"
                                font_style: "Body1"
                                size_hint_x: 0.7
                                opacity: 0

                        MDBoxLayout:
                            orientation: "horizontal"
                            size_hint_y: None
                            height: "40dp"
                            MDLabel:
                                text: "Location:"
                                font_style: "Body1"
                                bold: True
                                size_hint_x: 0.3
                            MDLabel:
                                id: profile_location
                                text: ""
                                font_style: "Body1"
                                size_hint_x: 0.7
                                opacity: 1
                            MDTextField:
                                id: profile_location_input
                                hint_text: "Enter your location"
                                font_style: "Body1"
                                size_hint_x: 0.7
                                opacity: 0

                MDCard:
                    size_hint_y: None
                    height: "150dp"
                    elevation: 3
                    radius: [10]
                    padding: "15dp"
                    MDBoxLayout:
                        orientation: "vertical"
                        spacing: "10dp"
                        MDLabel:
                            text: "📊 Account Statistics"
                            font_style: "H6"
                            theme_text_color: "Primary"
                        
                        MDBoxLayout:
                            orientation: "horizontal"
                            spacing: "20dp"
                            MDBoxLayout:
                                orientation: "vertical"
                                size_hint_x: 0.5
                                MDLabel:
                                    id: products_count
                                    text: "0"
                                    halign: "center"
                                    font_style: "H5"
                                    bold: True
                                    theme_text_color: "Primary"
                                MDLabel:
                                    text: "Products Listed"
                                    halign: "center"
                                    font_style: "Caption"
                                    theme_text_color: "Secondary"
                            
                            MDBoxLayout:
                                orientation: "vertical"
                                size_hint_x: 0.5
                                MDLabel:
                                    id: orders_count
                                    text: "0"
                                    halign: "center"
                                    font_style: "H5"
                                    bold: True
                                    theme_text_color: "Primary"
                                MDLabel:
                                    text: "Total Orders"
                                    halign: "center"
                                    font_style: "Caption"
                                    theme_text_color: "Secondary"

                MDRaisedButton:
                    id: edit_button
                    text: "✏️ Edit Profile"
                    size_hint_y: None
                    height: "50dp"
                    on_release: root.edit_profile()
                    pos_hint: {"center_x": 0.5}

<MarketPricesScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "💰 Live Market Prices"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
            right_action_items: [["refresh", lambda x: root.refresh_prices()]]
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "10dp"
                padding: "15dp"
                size_hint_y: None
                height: self.minimum_height

                MDCard:
                    size_hint_y: None
                    height: "80dp"
                    elevation: 3
                    padding: "15dp"
                    radius: [10]
                    MDLabel:
                        text: "📊 Current Market Prices\\n\\nReal-time agricultural commodity prices"
                        halign: "center"
                        font_style: "H6"
                        theme_text_color: "Primary"

                MDBoxLayout:
                    orientation: "vertical"
                    spacing: "8dp"
                    size_hint_y: None
                    height: "600dp"
                    id: prices_container

<OrdersScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "📋 Orders"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDScrollView:
            MDBoxLayout:
                orientation: "vertical"
                spacing: "10dp"
                padding: "15dp"
                size_hint_y: None
                height: self.minimum_height
                id: orders_container
""")

class SchemesScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def go_back(self):
        self.app.go_back_to_dashboard()

    def on_enter(self):
        self.load_schemes()

    def load_schemes(self):
        try:
            schemes = self.app.db_manager.get_govt_schemes()
            schemes_list = self.ids.schemes_list
            schemes_list.clear_widgets()
            
            for scheme in schemes:
                item = ThreeLineListItem(
                    text=f"🏛️ {scheme[1]}",
                    secondary_text=scheme[2][:80] + "..." if len(scheme[2]) > 80 else scheme[2],
                    tertiary_text=f"Benefits: {scheme[3]} | Contact: {scheme[8]}",
                )
                schemes_list.add_widget(item)
        except Exception as e:
            print(f"Error loading schemes: {e}")

class ProfileScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
        self.edit_mode = False

    def on_enter(self):
        self.load_profile()

    def load_profile(self):
        """Load and display user profile information"""
        if not self.app.store.exists("session"):
            self.ids.profile_name.text = "Not logged in"
            return

        session = self.app.store.get("session")
        phone = session["phone"]
        role = session["role"]

        # Get user details from database
        try:
            # Get user info
            conn = self.app.db_manager.get_connection()
            c = conn.cursor()
            c.execute("SELECT name, email, location FROM users WHERE phone = ?", (phone,))
            user_data = c.fetchone()
            conn.close()

            if user_data:
                name, email, location = user_data
                if self.edit_mode:
                    # In edit mode, populate text fields
                    self.ids.profile_name_input.text = name or ""
                    self.ids.profile_email_input.text = email or ""
                    self.ids.profile_location_input.text = location or ""
                else:
                    # In view mode, show labels
                    self.ids.profile_name.text = name or "Unknown"
                    self.ids.profile_role.text = f"🌾 {role.title()}" if role == "seller" else f"🛒 {role.title()}"
                    self.ids.profile_phone.text = phone
                    self.ids.profile_name_value.text = name or "Unknown"
                    self.ids.profile_email.text = self.mask_email(email) if email else "Not provided"
                    self.ids.profile_location.text = location or "Not specified"
            else:
                self.ids.profile_name.text = "User not found"

            # Load statistics
            self.load_statistics(phone, role)

        except Exception as e:
            print(f"Error loading profile: {e}")
            self.ids.profile_name.text = "Error loading profile"

    def mask_email(self, email):
        """Mask email to show only first few characters"""
        if not email or '@' not in email:
            return email
        username, domain = email.split('@', 1)
        if len(username) <= 3:
            return f"{username}@{domain}"
        return f"{username[:3]}***@{domain}"

    def load_statistics(self, phone, role):
        """Load user statistics"""
        print(f"DEBUG: Loading statistics for {role} - phone: {phone}")
        try:
            if role == "seller":
                # Count products
                products = self.app.db_manager.get_user_products(phone)
                print(f"DEBUG: Found {len(products)} products for seller")
                self.ids.products_count.text = str(len(products))

                # Count orders (seller orders)
                orders = self.app.db_manager.get_user_orders(phone, role)
                print(f"DEBUG: Found {len(orders)} orders for seller")
                self.ids.orders_count.text = str(len(orders))
            else:
                # For buyers, show different stats
                self.ids.products_count.text = "N/A"
                orders = self.app.db_manager.get_user_orders(phone, role)
                print(f"DEBUG: Found {len(orders)} orders for buyer")
                self.ids.orders_count.text = str(len(orders))

        except Exception as e:
            print(f"ERROR: Error loading statistics: {e}")
            import traceback
            traceback.print_exc()
            self.ids.products_count.text = "0"
            self.ids.orders_count.text = "0"

    def edit_profile(self):
        """Toggle edit mode for profile"""
        if not self.edit_mode:
            self.edit_mode = True
            self.show_edit_mode()
        else:
            # Save changes
            self.save_profile_changes()

    def show_edit_mode(self):
        """Switch UI to edit mode"""
        # Hide contact labels and show text inputs
        self.ids.profile_phone.opacity = 0
        self.ids.profile_name_value.opacity = 0
        self.ids.profile_email.opacity = 0
        self.ids.profile_location.opacity = 0

        self.ids.profile_name_input.opacity = 1
        self.ids.profile_email_input.opacity = 1
        self.ids.profile_location_input.opacity = 1

        # Change button text to Save
        self.ids.edit_button.text = "💾 Save Profile"

    def hide_edit_mode(self):
        """Switch UI back to view mode"""
        self.ids.profile_phone.opacity = 1
        self.ids.profile_name_value.opacity = 1
        self.ids.profile_email.opacity = 1
        self.ids.profile_location.opacity = 1

        self.ids.profile_name_input.opacity = 0
        self.ids.profile_email_input.opacity = 0
        self.ids.profile_location_input.opacity = 0

        # Change button text back to Edit
        self.ids.edit_button.text = "✏️ Edit Profile"

    def save_profile_changes(self):
        """Save profile changes to database"""
        session = self.app.store.get("session")
        phone = session["phone"]

        new_name = self.ids.profile_name_input.text.strip()
        new_email = self.ids.profile_email_input.text.strip()
        new_location = self.ids.profile_location_input.text.strip()

        success = self.app.db_manager.update_user(phone, name=new_name, email=new_email, location=new_location)
        from kivymd.uix.snackbar import Snackbar
        if success:
            Snackbar(text="Profile updated successfully!").open()
            self.edit_mode = False
            self.hide_edit_mode()
            self.load_profile()
        else:
            Snackbar(text="Failed to update profile. Please try again.").open()

    def go_back(self):
        self.app.go_back_to_dashboard()

class MarketPricesScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def go_back(self):
        self.app.go_back_to_dashboard()

    def on_enter(self):
        self.refresh_prices()

    def refresh_prices(self):
        """Load and display current market prices"""
        try:
            # Clear existing prices
            prices_container = self.ids.prices_container
            prices_container.clear_widgets()

            # Sample market data - in real app, this would come from API
            market_data = {
                "Tomatoes": {"price": 25.50, "change": "+2.5%", "trend": "up"},
                "Onions": {"price": 32.00, "change": "-1.2%", "trend": "down"},
                "Wheat": {"price": 22.80, "change": "+0.8%", "trend": "up"},
                "Rice": {"price": 48.90, "change": "+1.5%", "trend": "up"},
                "Potatoes": {"price": 18.75, "change": "-0.5%", "trend": "down"},
                "Apples": {"price": 85.00, "change": "+3.2%", "trend": "up"},
                "Bananas": {"price": 38.50, "change": "+1.8%", "trend": "up"},
                "Sugarcane": {"price": 295.00, "change": "+0.3%", "trend": "up"},
                "Cotton": {"price": 4250.00, "change": "-2.1%", "trend": "down"},
                "Soybean": {"price": 42.30, "change": "+1.1%", "trend": "up"}
            }

            for commodity, data in market_data.items():
                # Create price card programmatically
                from kivymd.uix.card import MDCard
                from kivymd.uix.boxlayout import MDBoxLayout
                from kivymd.uix.label import MDLabel

                card = MDCard(
                    size_hint_y=None,
                    height="70dp",
                    elevation=2,
                    radius=[8],
                    padding="12dp"
                )

                box = MDBoxLayout(
                    orientation="horizontal",
                    spacing="10dp"
                )

                # Commodity name
                name_label = MDLabel(
                    text=commodity,
                    font_style="Subtitle1",
                    bold=True,
                    size_hint_x=0.4
                )

                # Price
                price_label = MDLabel(
                    text=f"₹{data['price']:.2f}/kg",
                    font_style="Subtitle1",
                    halign="right",
                    size_hint_x=0.3
                )

                # Change percentage
                change_label = MDLabel(
                    text=data['change'],
                    font_style="Caption",
                    halign="right",
                    theme_text_color="Custom",
                    text_color=(0, 0.8, 0, 1) if data['trend'] == "up" else (0.8, 0, 0, 1),
                    size_hint_x=0.3
                )

                box.add_widget(name_label)
                box.add_widget(price_label)
                box.add_widget(change_label)
                card.add_widget(box)

                prices_container.add_widget(card)

        except Exception as e:
            print(f"Error loading market prices: {e}")
            # Fallback message
            from kivymd.uix.label import MDLabel
            error_label = MDLabel(
                text="Unable to load market prices. Please try again.",
                halign="center",
                font_style="Subtitle1"
            )
            self.ids.prices_container.add_widget(error_label)

class OrdersScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def on_enter(self):
        self.load_orders()

    def load_orders(self):
        """Load and display user orders"""
        container = self.ids.orders_container
        container.clear_widgets()

        if not self.app.store.exists("session"):
            from kivymd.uix.label import MDLabel
            no_session_label = MDLabel(
                text="Please login to view your orders.",
                halign="center",
                font_style="Subtitle1",
                theme_text_color="Secondary"
            )
            container.add_widget(no_session_label)
            return

        session = self.app.store.get("session")
        phone = session["phone"]
        role = session["role"]

        try:
            orders = self.app.db_manager.get_user_orders(phone, role)

            if not orders:
                from kivymd.uix.label import MDLabel
                no_orders_label = MDLabel(
                    text="No orders found.\\n\\nYour order history will appear here once you place orders.",
                    halign="center",
                    font_style="Subtitle1",
                    theme_text_color="Secondary"
                )
                container.add_widget(no_orders_label)
                return

            from kivymd.uix.card import MDCard
            from kivymd.uix.boxlayout import MDBoxLayout
            from kivymd.uix.label import MDLabel

            for order in orders:
                # Unpack order data based on role
                if role == "seller":
                    order_id, order_number, buyer_phone, seller_phone, product_id, quantity, unit_price, total_amount, status, delivery_address, payment_method, notes, created_at, delivered_at, product_name, buyer_name = order
                    other_party = buyer_name
                    other_party_label = "Buyer"
                else:
                    order_id, order_number, buyer_phone, seller_phone, product_id, quantity, unit_price, total_amount, status, delivery_address, payment_method, notes, created_at, delivered_at, product_name, seller_name = order
                    other_party = seller_name
                    other_party_label = "Seller"

                card = MDCard(
                    size_hint_y=None,
                    height="150dp",
                    elevation=5,
                    radius=[10],
                    padding="15dp"
                )

                layout = MDBoxLayout(orientation="vertical", spacing="5dp")

                # Order number and status
                header_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="30dp")
                order_label = MDLabel(
                    text=f"Order #{order_number}",
                    font_style="H6",
                    theme_text_color="Primary",
                    size_hint_x=0.6
                )

                status_label = MDLabel(
                    text=status.title(),
                    font_style="Body2",
                    theme_text_color="Custom",
                    text_color=self.get_status_color(status),
                    halign="right",
                    size_hint_x=0.4
                )

                header_layout.add_widget(order_label)
                header_layout.add_widget(status_label)

                # Product and quantity
                product_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="30dp")
                product_name_label = MDLabel(
                    text=f"{product_name}",
                    font_style="Subtitle1",
                    theme_text_color="Secondary",
                    size_hint_x=0.6
                )

                quantity_label = MDLabel(
                    text=f"Qty: {quantity}",
                    font_style="Body2",
                    theme_text_color="Secondary",
                    halign="right",
                    size_hint_x=0.4
                )

                product_layout.add_widget(product_name_label)
                product_layout.add_widget(quantity_label)

                # Amount and date
                details_layout = MDBoxLayout(orientation="horizontal", size_hint_y=None, height="30dp")
                amount_label = MDLabel(
                    text=f"₹{total_amount:.2f}",
                    font_style="H6",
                    theme_text_color="Primary",
                    size_hint_x=0.5
                )

                date_label = MDLabel(
                    text=created_at.split(' ')[0],  # Show only date
                    font_style="Body2",
                    theme_text_color="Secondary",
                    halign="right",
                    size_hint_x=0.5
                )

                details_layout.add_widget(amount_label)
                details_layout.add_widget(date_label)

                # Other party info
                party_label = MDLabel(
                    text=f"{other_party_label}: {other_party}",
                    font_style="Caption",
                    theme_text_color="Secondary",
                    size_hint_y=None,
                    height="20dp"
                )

                layout.add_widget(header_layout)
                layout.add_widget(product_layout)
                layout.add_widget(details_layout)
                layout.add_widget(party_label)

                card.add_widget(layout)
                container.add_widget(card)

        except Exception as e:
            print(f"Error loading orders: {e}")
            from kivymd.uix.label import MDLabel
            error_label = MDLabel(
                text="Error loading orders. Please try again.",
                halign="center",
                font_style="Subtitle1",
                theme_text_color="Error"
            )
            container.add_widget(error_label)

    def get_status_color(self, status):
        """Get color for order status"""
        status_colors = {
            "pending": (1, 0.5, 0, 1),    # Orange
            "confirmed": (0, 0.5, 1, 1),  # Blue
            "shipped": (0.5, 0, 1, 1),    # Purple
            "delivered": (0, 0.8, 0, 1),  # Green
            "cancelled": (0.8, 0, 0, 1)   # Red
        }
        return status_colors.get(status.lower(), (0.5, 0.5, 0.5, 1))  # Gray default

    def go_back(self):
        self.app.go_back_to_dashboard()

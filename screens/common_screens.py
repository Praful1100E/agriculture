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
        MDLabel:
            text: "Profile management coming soon!"
            halign: "center"
            font_style: "Subtitle1"

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
        MDLabel:
            text: "Your order history will appear here."
            halign: "center"
            font_style: "Subtitle1"
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
    
    def go_back(self):
        self.app.go_back_to_dashboard()

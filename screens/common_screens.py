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
            title: "💰 Market Prices"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDLabel:
            text: "Live market prices will be displayed here."
            halign: "center"
            font_style: "Subtitle1"

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

class OrdersScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
    
    def go_back(self):
        self.app.go_back_to_dashboard()

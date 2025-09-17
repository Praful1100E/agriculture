# screens/address_screens.py - Address Management (FIXED)
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder

Builder.load_string("""
<AddressScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "📍 Addresses"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDLabel:
            text: "Address management coming soon!"
            halign: "center"

<PaymentMethodScreen>:
    MDBoxLayout:
        orientation: "vertical"
        MDTopAppBar:
            title: "💳 Payment Methods"
            left_action_items: [["arrow-left", lambda x: root.go_back()]]
        MDLabel:
            text: "Payment methods coming soon!"
            halign: "center"
""")

class AddressScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
    
    def go_back(self):
        self.app.go_back_to_dashboard()

class PaymentMethodScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app
    
    def go_back(self):
        self.app.go_back_to_dashboard()

# screens/auth_screens.py - COMPLETE AgriConnect with Circular Logo
import re
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.properties import StringProperty, BooleanProperty
from kivy.metrics import dp

# Use the newer MDSnackbar instead of deprecated Snackbar
try:
    from kivymd.uix.snackbar import MDSnackbar
    from kivymd.uix.label import MDLabel
    use_md_snackbar = True
except ImportError:
    from kivymd.uix.snackbar import Snackbar
    use_md_snackbar = False

# COMPLETE AGRICONNECT DESIGN with Circular Logo
Builder.load_string("""
<LoginScreen>:
    MDFloatLayout:
        md_bg_color: 0.94, 0.98, 0.94, 1  # Very light green background
        
        # Mobile-optimized LOGIN card
        MDCard:
            size_hint: 0.92, None
            height: "650dp"  # Increased height for logo
            pos_hint: {"center_x": 0.5, "center_y": 0.5}
            elevation: 12
            md_bg_color: 1, 1, 1, 1  # Pure white
            
            MDBoxLayout:
                orientation: "vertical"
                spacing: 0
                padding: 0
                
                # Logo and Branding Section
                MDBoxLayout:
                    size_hint_y: None
                    height: "120dp"
                    orientation: "vertical"
                    md_bg_color: 1, 1, 1, 1
                    spacing: "8dp"
                    padding: "0dp", "20dp", "0dp", "8dp"
                    
                    # Circular Logo Container - PERFECT CIRCULAR CLIPPING
                    MDBoxLayout:
                        size_hint_y: None
                        height: "70dp"
                        
                        Widget:  # Left spacer
                        
                        # Simple Logo
                        AsyncImage:
                            id: logo_main
                            source: "images/logo.png"
                            size_hint: None, None
                            size: "60dp", "60dp"
                            pos_hint: {"center_x": 0.5}
                            keep_ratio: True
                            allow_stretch: True
                        
                        Widget:  # Right spacer
                    
                    # App Name
                    MDLabel:
                        text: "AgriConnect"
                        font_style: "H6"
                        font_size: "20sp"
                        bold: True
                        halign: "center"
                        theme_text_color: "Custom"
                        text_color: 0, 0, 0, 1  # Black
                        size_hint_y: None
                        height: "24dp"
                                    
                # LOGIN Header
                MDBoxLayout:
                    size_hint_y: None
                    height: "50dp"
                    md_bg_color: 1, 1, 1, 1
                    
                    MDLabel:
                        text: "LOGIN"
                        font_style: "H5"
                        font_size: "24sp"
                        bold: True
                        halign: "center"
                        valign: "center"
                        theme_text_color: "Custom"
                        text_color: 0.15, 0.7, 0.15, 1  # Green
                
                # Tab section - Mobile style
                MDBoxLayout:
                    size_hint_y: None
                    height: "45dp"
                    orientation: "horizontal"
                    md_bg_color: 0.96, 0.96, 0.96, 1
                    
                    # User Login Tab (Active) 
                    MDBoxLayout:
                        size_hint: 0.5, 1
                        md_bg_color: 1, 1, 1, 1
                        
                        MDLabel:
                            text: "User Login"
                            font_style: "Subtitle1"
                            font_size: "16sp"
                            halign: "center"
                            valign: "center"
                            theme_text_color: "Custom"
                            text_color: 0.15, 0.7, 0.15, 1
                    
                    # Admin Login Tab (Inactive)
                    MDBoxLayout:
                        size_hint: 0.5, 1
                        
                        MDLabel:
                            text: "Admin Login"
                            font_style: "Subtitle1"
                            font_size: "16sp"
                            halign: "center"
                            valign: "center"
                            theme_text_color: "Custom"
                            text_color: 0.5, 0.5, 0.5, 1
                
                # Form content - Mobile spacing
                MDBoxLayout:
                    orientation: "vertical"
                    padding: "24dp", "20dp", "24dp", "16dp"
                    spacing: "18dp"
                    md_bg_color: 1, 1, 1, 1
                    
                    # User ID field
                    MDBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: "60dp"
                        spacing: "6dp"
                        
                        MDLabel:
                            text: "Phone Number"
                            font_style: "Subtitle2"
                            font_size: "14sp"
                            size_hint_y: None
                            height: "18dp"
                            theme_text_color: "Custom"
                            text_color: 0.3, 0.3, 0.3, 1

                        MDTextField:
                            id: phone
                            hint_text: "Enter your phone number"
                            helper_text: "10-digit mobile number"
                            helper_text_mode: "persistent"
                            size_hint_y: None
                            height: "60dp"
                            font_size: "16sp"
                            multiline: False
                            max_text_length: 10
                            input_filter: "int"
                            line_color_normal: 0.8, 0.8, 0.8, 1
                            line_color_focus: 0.15, 0.7, 0.15, 1
                            line_width: 1.5
                    
                    # Password field
                    MDBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: "60dp"
                        spacing: "6dp"
                        
                        MDLabel:
                            text: "Password"
                            font_style: "Subtitle2"
                            font_size: "14sp"
                            size_hint_y: None
                            height: "18dp"
                            theme_text_color: "Custom"
                            text_color: 0.3, 0.3, 0.3, 1
                        
                        MDTextField:
                            id: password
                            password: True
                            size_hint_y: None
                            height: "48dp"
                            font_size: "16sp"
                            multiline: False
                            line_color_normal: 0.8, 0.8, 0.8, 1
                            line_color_focus: 0.15, 0.7, 0.15, 1
                            line_width: 1.5
                    
                    # Show Password and Forget Password
                    MDBoxLayout:
                        orientation: "horizontal"
                        size_hint_y: None
                        height: "28dp"
                        spacing: "10dp"
                        
                        MDCheckbox:
                            id: show_password_check
                            size_hint: None, None
                            size: "22dp", "22dp"
                            theme_icon_color: "Custom"
                            icon_color: 0.15, 0.7, 0.15, 1
                            on_active: root.toggle_password_visibility()
                        
                        MDLabel:
                            text: "Show Password"
                            font_style: "Caption"
                            font_size: "12sp"
                            theme_text_color: "Custom"
                            text_color: 0.4, 0.4, 0.4, 1
                            size_hint_y: None
                            height: "22dp"
                            valign: "center"
                        
                        Widget:  # Flexible spacer
                        
                        MDTextButton:
                            text: "Forget Password"
                            theme_text_color: "Custom"
                            text_color: 0.15, 0.7, 0.15, 1
                            font_style: "Caption"
                            font_size: "12sp"
                            size_hint: None, None
                            size: "100dp", "22dp"
                            on_release: root.forgot_password()
                    
                    Widget:
                        size_hint_y: None
                        height: "12dp"
                    
                    # LOGIN Button
                    MDRaisedButton:
                        text: "LOGIN"
                        size_hint: None, None
                        size: "200dp", "46dp"
                        pos_hint: {"center_x": 0.5}
                        md_bg_color: 0.15, 0.7, 0.15, 1
                        elevation: 3
                        font_style: "Button"
                        font_size: "16sp"
                        on_release: root.handle_login()
                    
                    Widget:
                        size_hint_y: None
                        height: "20dp"
                    
                    # New to AgriConnect section
                    MDBoxLayout:
                        orientation: "vertical"
                        size_hint_y: None
                        height: "55dp"
                        spacing: "6dp"
                        
                        MDLabel:
                            text: "New to AgriConnect?"
                            font_style: "Body2"
                            font_size: "14sp"
                            halign: "center"
                            theme_text_color: "Custom"
                            text_color: 0.5, 0.5, 0.5, 1
                            size_hint_y: None
                            height: "18dp"
                        
                        MDTextButton:
                            text: "Create Account"
                            theme_text_color: "Custom"
                            text_color: 0.15, 0.7, 0.15, 1
                            font_style: "Subtitle1"
                            font_size: "15sp"
                            bold: True
                            pos_hint: {"center_x": 0.5}
                            size_hint: None, None
                            size: "130dp", "31dp"
                            on_release: root.manager.current = "register"

<RegisterScreen>:
    MDScrollView:
        MDFloatLayout:
            size_hint_y: None
            height: "950dp"
            md_bg_color: 0.94, 0.98, 0.94, 1
            
            # Mobile registration card
            MDCard:
                size_hint: 0.92, None
                height: "870dp"  # Increased for logo
                pos_hint: {"center_x": 0.5, "center_y": 0.5}
                elevation: 12
                md_bg_color: 1, 1, 1, 1
                
                MDBoxLayout:
                    orientation: "vertical"
                    spacing: 0
                    padding: 0
                    
                    # Logo and Header Section - CIRCULAR CLIPPING
                    MDBoxLayout:
                        size_hint_y: None
                        height: "100dp"
                        orientation: "vertical"
                        md_bg_color: 1, 1, 1, 1
                        spacing: "6dp"
                        padding: "0dp", "16dp", "0dp", "6dp"
                        
                        # Simple Logo
                        MDBoxLayout:
                            size_hint_y: None
                            height: "50dp"

                            Widget:

                            AsyncImage:
                                id: reg_logo
                                source: "images/logo.png"
                                size_hint: None, None
                                size: "40dp", "40dp"
                                pos_hint: {"center_x": 0.5}
                                keep_ratio: True
                                allow_stretch: True

                            Widget:
                        
                        # App name and title
                        MDBoxLayout:
                            orientation: "horizontal"
                            size_hint_y: None
                            height: "28dp"
                            spacing: "8dp"
                            
                            Widget:
                            
                                MDLabel:
                                    text: "AgriConnect"
                                    font_style: "Subtitle1"
                                    font_size: "16sp"
                                    bold: True
                                    halign: "center"
                                    theme_text_color: "Custom"
                                    text_color: 0, 0, 0, 1  # Black
                                    size_hint: None, None
                                    size: "100dp", "14dp"

                            
                            MDLabel:
                                text: "• CREATE ACCOUNT"
                                font_style: "Subtitle2"
                                font_size: "14sp"
                                bold: True
                                halign: "center"
                                theme_text_color: "Custom"
                                text_color: 0.15, 0.7, 0.15, 1
                                size_hint: None, None
                                size: "140dp", "14dp"
                            
                            Widget:
                    
                    # Form content - Compact for mobile
                    MDBoxLayout:
                        orientation: "vertical"
                        padding: "24dp", "12dp", "24dp", "12dp"
                        spacing: "14dp"
                        
                        # All form fields - compact mobile style
                        MDBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "46dp"
                            spacing: "4dp"
                            
                            MDLabel:
                                text: "Full Name"
                                font_style: "Caption"
                                font_size: "11sp"
                                size_hint_y: None
                                height: "14dp"
                                theme_text_color: "Custom"
                                text_color: 0.4, 0.4, 0.4, 1
                            
                            MDTextField:
                                id: r_name
                                size_hint_y: None
                                height: "28dp"
                                font_size: "13sp"
                                line_color_focus: 0.15, 0.7, 0.15, 1
                                max_text_length: 50
                        
                        MDBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "46dp"
                            spacing: "4dp"
                            
                            MDLabel:
                                text: "Phone Number"
                                font_style: "Caption"
                                font_size: "11sp"
                                size_hint_y: None
                                height: "14dp"
                                theme_text_color: "Custom"
                                text_color: 0.4, 0.4, 0.4, 1
                            
                            MDTextField:
                                id: r_phone
                                size_hint_y: None
                                height: "28dp"
                                font_size: "13sp"
                                input_filter: "int"
                                max_text_length: 10
                                line_color_focus: 0.15, 0.7, 0.15, 1
                        
                        MDBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "46dp"
                            spacing: "4dp"
                            
                            MDLabel:
                                text: "Email Address"
                                font_style: "Caption"
                                font_size: "11sp"
                                size_hint_y: None
                                height: "14dp"
                                theme_text_color: "Custom"
                                text_color: 0.4, 0.4, 0.4, 1
                            
                            MDTextField:
                                id: r_email
                                size_hint_y: None
                                height: "28dp"
                                font_size: "13sp"
                                line_color_focus: 0.15, 0.7, 0.15, 1
                                max_text_length: 100
                        
                        MDBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "46dp"
                            spacing: "4dp"
                            
                            MDLabel:
                                text: "Location (Optional)"
                                font_style: "Caption"
                                font_size: "11sp"
                                size_hint_y: None
                                height: "14dp"
                                theme_text_color: "Custom"
                                text_color: 0.4, 0.4, 0.4, 1
                            
                            MDTextField:
                                id: r_location
                                size_hint_y: None
                                height: "28dp"
                                font_size: "13sp"
                                line_color_focus: 0.15, 0.7, 0.15, 1
                                max_text_length: 50
                        
                        MDBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "46dp"
                            spacing: "4dp"
                            
                            MDLabel:
                                text: "Password"
                                font_style: "Caption"
                                font_size: "11sp"
                                size_hint_y: None
                                height: "14dp"
                                theme_text_color: "Custom"
                                text_color: 0.4, 0.4, 0.4, 1
                            
                            MDTextField:
                                id: r_pass
                                password: True
                                size_hint_y: None
                                height: "28dp"
                                font_size: "13sp"
                                line_color_focus: 0.15, 0.7, 0.15, 1
                                max_text_length: 20
                        
                        # Role selection - Compact mobile
                        MDLabel:
                            text: "I am a:"
                            font_style: "Subtitle2"
                            font_size: "13sp"
                            theme_text_color: "Custom"
                            text_color: 0.15, 0.7, 0.15, 1
                            bold: True
                            size_hint_y: None
                            height: "20dp"
                        
                        MDBoxLayout:
                            size_hint_y: None
                            height: "40dp"
                            spacing: "12dp"
                            
                            MDRaisedButton:
                                text: "🌾 Farmer"
                                font_size: "12sp"
                                md_bg_color: (0.15, 0.7, 0.15, 1) if root.seller_selected else (0.92, 0.92, 0.92, 1)
                                theme_text_color: "Custom"
                                text_color: (1, 1, 1, 1) if root.seller_selected else (0.5, 0.5, 0.5, 1)
                                elevation: 2 if root.seller_selected else 1
                                on_release: root.select_role("seller")
                            
                            MDRaisedButton:
                                text: "🛒 Buyer"
                                font_size: "12sp"
                                md_bg_color: (0.15, 0.7, 0.15, 1) if root.buyer_selected else (0.92, 0.92, 0.92, 1)
                                theme_text_color: "Custom"
                                text_color: (1, 1, 1, 1) if root.buyer_selected else (0.5, 0.5, 0.5, 1)
                                elevation: 2 if root.buyer_selected else 1
                                on_release: root.select_role("buyer")
                        
                        Widget:
                            size_hint_y: None
                            height: "16dp"
                        
                        # Create Account Button
                        MDRaisedButton:
                            text: "CREATE ACCOUNT"
                            size_hint: None, None
                            size: "220dp", "42dp"
                            pos_hint: {"center_x": 0.5}
                            md_bg_color: 0.15, 0.7, 0.15, 1
                            elevation: 3
                            font_style: "Button"
                            font_size: "14sp"
                            on_release: root.handle_register()
                        
                        Widget:
                            size_hint_y: None
                            height: "14dp"
                        
                        # Login link
                        MDBoxLayout:
                            orientation: "vertical"
                            size_hint_y: None
                            height: "40dp"
                            spacing: "3dp"
                            
                            MDLabel:
                                text: "Already have an account?"
                                font_style: "Body2"
                                font_size: "12sp"
                                halign: "center"
                                theme_text_color: "Custom"
                                text_color: 0.5, 0.5, 0.5, 1
                            
                            MDTextButton:
                                text: "Login"
                                theme_text_color: "Custom"
                                text_color: 0.15, 0.7, 0.15, 1
                                font_style: "Subtitle1"
                                font_size: "13sp"
                                bold: True
                                pos_hint: {"center_x": 0.5}
                                size_hint: None, None
                                size: "70dp", "18dp"
                                on_release: root.manager.current = "login"
""")

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

def validate_phone(phone):
    """Validate Indian phone number"""
    phone = phone.strip()
    if not phone:
        return False, "Phone number is required"
    if not phone.isdigit():
        return False, "Phone number must contain only digits"
    if len(phone) != 10:
        return False, "Phone number must be exactly 10 digits"
    if not phone.startswith(('6', '7', '8', '9')):
        return False, "Phone number must start with 6, 7, 8, or 9"
    return True, "Valid phone number"

def validate_email(email):
    """Validate email address"""
    email = email.strip()
    if not email:
        return False, "Email is required"
    
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not re.match(pattern, email):
        return False, "Please enter a valid email address (e.g., user@example.com)"
    
    if len(email) > 100:
        return False, "Email address is too long"
    
    return True, "Valid email"

def validate_name(name):
    """Validate full name"""
    name = name.strip()
    if not name:
        return False, "Full name is required"
    if len(name) < 2:
        return False, "Name must be at least 2 characters"
    if not all(char.isalpha() or char.isspace() for char in name):
        return False, "Name must contain only letters and spaces"
    if len(name) > 50:
        return False, "Name is too long (maximum 50 characters)"
    return True, "Valid name"

def validate_password(password):
    """Validate password strength"""
    password = password.strip()
    if not password:
        return False, "Password is required"
    if len(password) < 6:
        return False, "Password must be at least 6 characters long"
    if len(password) > 20:
        return False, "Password is too long (maximum 20 characters)"
    return True, "Valid password"

class LoginScreen(Screen):
    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def toggle_password_visibility(self):
        """Toggle password visibility"""
        password_field = self.ids.password
        checkbox = self.ids.show_password_check
        password_field.password = not checkbox.active

    def forgot_password(self):
        """Handle forgot password"""
        show_message("📧 Password recovery will be implemented soon!")

    def handle_login(self):
        phone = self.ids.phone.text.strip()
        password = self.ids.password.text.strip()
        
        # Validate phone
        phone_valid, phone_msg = validate_phone(phone)
        if not phone_valid:
            show_message(phone_msg)
            return
        
        # Validate password
        if not password:
            show_message("Password is required")
            return
        
        # Authenticate user
        try:
            result = self.app.db_manager.authenticate_user(phone, password)
            
            if result:
                name, role, location = result
                self.app.store.put("session", phone=phone, name=name, role=role, location=location or "")
                
                next_screen = "seller_dashboard" if role == "seller" else "buyer_dashboard"
                self.manager.current = next_screen
                
                self.app.load_dashboard_data(role)
                
                emoji = "🌾" if role == "seller" else "🛒"
                show_message(f"Welcome back, {name}! {emoji}")
                
                # Clear form
                self.ids.phone.text = ""
                self.ids.password.text = ""
                self.ids.show_password_check.active = False
            else:
                show_message("❌ Invalid phone number or password")
                
        except Exception as e:
            show_message("❌ Login failed. Please try again.")
            print(f"Login error: {e}")

class RegisterScreen(Screen):
    role = StringProperty("")
    seller_selected = BooleanProperty(False)
    buyer_selected = BooleanProperty(False)

    def __init__(self, app=None, **kwargs):
        super().__init__(**kwargs)
        self.app = app

    def select_role(self, role):
        self.role = role
        
        if role == "seller":
            self.seller_selected = True
            self.buyer_selected = False
            show_message("🌾 Selected: Farmer/Seller")
        else:
            self.buyer_selected = True
            self.seller_selected = False
            show_message("🛒 Selected: Buyer")

    def handle_register(self):
        name = self.ids.r_name.text.strip()
        phone = self.ids.r_phone.text.strip()
        email = self.ids.r_email.text.strip()
        location = self.ids.r_location.text.strip()
        password = self.ids.r_pass.text.strip()
        
        # Comprehensive validation
        name_valid, name_msg = validate_name(name)
        if not name_valid:
            show_message(name_msg)
            return
        
        phone_valid, phone_msg = validate_phone(phone)
        if not phone_valid:
            show_message(phone_msg)
            return
        
        email_valid, email_msg = validate_email(email)
        if not email_valid:
            show_message(email_msg)
            return
        
        password_valid, password_msg = validate_password(password)
        if not password_valid:
            show_message(password_msg)
            return
        
        if not self.role:
            show_message("⚠️ Please select your role (Farmer or Buyer)")
            return
        
        try:
            # Create user account
            success = self.app.db_manager.create_user(name, phone, email, password, self.role, location)
            
            if success:
                self.app.store.put("session", phone=phone, name=name, role=self.role, location=location)
                
                next_screen = "seller_dashboard" if self.role == "seller" else "buyer_dashboard"
                self.manager.current = next_screen
                
                self.app.load_dashboard_data(self.role)
                
                emoji = "🌾" if self.role == "seller" else "🛒"
                show_message(f"🎉 Welcome to AgriConnect, {name}! {emoji}")
                
                # Clear form
                for field in [self.ids.r_name, self.ids.r_phone, self.ids.r_email, self.ids.r_location, self.ids.r_pass]:
                    field.text = ""
                self.role = ""
                self.seller_selected = False
                self.buyer_selected = False
            else:
                show_message("❌ Phone number already registered. Please use a different number.")
                
        except Exception as e:
            show_message("❌ Registration failed. Please try again.")
            print(f"Registration error: {e}")

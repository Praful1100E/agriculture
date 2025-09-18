# database/db_manager.py - FIXED with Database Migration Support
import sqlite3
from datetime import datetime
import os

class DatabaseManager:
    def __init__(self, db_path="data/agrimart.db"):
        self.db_path = db_path
        os.makedirs(os.path.dirname(db_path), exist_ok=True)

    def get_connection(self):
        return sqlite3.connect(self.db_path)

    def check_and_migrate_database(self):
        """Check database schema and migrate if needed"""
        conn = self.get_connection()
        c = conn.cursor()
        
        try:
            # Check if users table exists and get its schema
            c.execute("PRAGMA table_info(users)")
            columns = [column[1] for column in c.fetchall()]
            
            # If location column doesn't exist, add it
            if columns and 'location' not in columns:
                print("🔄 Migrating database: Adding location column...")
                c.execute("ALTER TABLE users ADD COLUMN location TEXT DEFAULT ''")
                conn.commit()
                print("✅ Database migration completed")
                
        except sqlite3.OperationalError as e:
            # Table doesn't exist yet, will be created in init_database
            pass
        except Exception as e:
            print(f"Migration error: {e}")
        finally:
            conn.close()

    def init_database(self):
        """Initialize database with proper migration support"""
        # First check and migrate existing database
        self.check_and_migrate_database()
        
        conn = self.get_connection()
        c = conn.cursor()
        
        # Users table - Create with full schema
        c.execute("""CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT UNIQUE NOT NULL,
            email TEXT,
            password TEXT NOT NULL,
            role TEXT NOT NULL CHECK(role IN ('seller', 'buyer')),
            location TEXT DEFAULT '',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP
        )""")
        
        # Products table
        c.execute("""CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            seller_phone TEXT NOT NULL,
            name TEXT NOT NULL,
            category TEXT NOT NULL,
            variety TEXT,
            unit TEXT NOT NULL,
            price REAL NOT NULL CHECK(price > 0),
            stock_qty REAL NOT NULL CHECK(stock_qty >= 0),
            description TEXT,
            image_path TEXT,
            status TEXT DEFAULT 'active',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(seller_phone) REFERENCES users(phone)
        )""")
        
        # Orders table
        c.execute("""CREATE TABLE IF NOT EXISTS orders(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            order_number TEXT UNIQUE NOT NULL,
            buyer_phone TEXT NOT NULL,
            seller_phone TEXT NOT NULL,
            product_id INTEGER NOT NULL,
            quantity REAL NOT NULL CHECK(quantity > 0),
            unit_price REAL NOT NULL CHECK(unit_price > 0),
            total_amount REAL NOT NULL CHECK(total_amount > 0),
            status TEXT DEFAULT 'pending',
            delivery_address TEXT,
            payment_method TEXT,
            notes TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            delivered_at TEXT,
            FOREIGN KEY(buyer_phone) REFERENCES users(phone),
            FOREIGN KEY(seller_phone) REFERENCES users(phone),
            FOREIGN KEY(product_id) REFERENCES products(id)
        )""")
        
        # Shopping cart table
        c.execute("""CREATE TABLE IF NOT EXISTS cart(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            buyer_phone TEXT NOT NULL,
            product_id INTEGER NOT NULL,
            quantity REAL NOT NULL CHECK(quantity > 0),
            added_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(buyer_phone) REFERENCES users(phone),
            FOREIGN KEY(product_id) REFERENCES products(id),
            UNIQUE(buyer_phone, product_id)
        )""")
        
        # Government schemes table
        c.execute("""CREATE TABLE IF NOT EXISTS govt_schemes(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            description TEXT NOT NULL,
            benefits TEXT,
            eligibility TEXT,
            how_to_apply TEXT,
            department TEXT,
            website_url TEXT,
            contact_info TEXT,
            is_active INTEGER DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )""")
        
        # Price history table
        c.execute("""CREATE TABLE IF NOT EXISTS price_history(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_name TEXT NOT NULL,
            market_price REAL NOT NULL,
            source TEXT DEFAULT 'market_api',
            location TEXT DEFAULT 'Hamirpur',
            recorded_at TEXT DEFAULT CURRENT_TIMESTAMP
        )""")
        
        # User addresses table
        c.execute("""CREATE TABLE IF NOT EXISTS addresses(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_phone TEXT NOT NULL,
            label TEXT NOT NULL,
            address_line1 TEXT NOT NULL,
            address_line2 TEXT,
            city TEXT NOT NULL,
            state TEXT NOT NULL,
            pincode TEXT NOT NULL,
            is_default INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_phone) REFERENCES users(phone)
        )""")
        
        # Notifications table
        c.execute("""CREATE TABLE IF NOT EXISTS notifications(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_phone TEXT NOT NULL,
            title TEXT NOT NULL,
            message TEXT NOT NULL,
            notification_type TEXT DEFAULT 'general',
            is_read INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(user_phone) REFERENCES users(phone)
        )""")
        
        conn.commit()
        conn.close()
        
        # Verify migration worked
        self.verify_schema()
        self.insert_sample_data()
        print("✅ Database initialized successfully")

    def verify_schema(self):
        """Verify that all expected columns exist"""
        conn = self.get_connection()
        c = conn.cursor()
        
        try:
            c.execute("PRAGMA table_info(users)")
            columns = [column[1] for column in c.fetchall()]
            
            expected_columns = ['id', 'name', 'phone', 'email', 'password', 'role', 'location', 'created_at', 'updated_at']
            missing_columns = [col for col in expected_columns if col not in columns]
            
            if missing_columns:
                print(f"❌ Missing columns in users table: {missing_columns}")
                # Try to add missing columns
                for col in missing_columns:
                    if col == 'location':
                        c.execute("ALTER TABLE users ADD COLUMN location TEXT DEFAULT ''")
                conn.commit()
                print("✅ Added missing columns")
            else:
                print("✅ Database schema verified")
                
        except Exception as e:
            print(f"Schema verification error: {e}")
        finally:
            conn.close()

    def insert_sample_data(self):
        schemes = [
            ("PM-KISAN", "Pradhan Mantri Kisan Samman Nidhi", "₹6000 per year in 3 installments", 
             "Small and marginal farmers", "Apply through CSC centers", 
             "Ministry of Agriculture", "https://pmkisan.gov.in", "1800-115-526"),
            ("Soil Health Card", "Free soil testing", "Free soil testing", 
             "All farmers", "Contact agriculture department", 
             "Department of Agriculture", "https://soilhealth.dac.gov.in", "1800-180-1551"),
            ("KCC", "Kisan Credit Card", "Credit up to ₹3 lakh", 
             "All farmers", "Apply through banks", 
             "NABARD", "https://nabard.org", "1800-103-0982")
        ]
        
        conn = self.get_connection()
        c = conn.cursor()
        for scheme in schemes:
            try:
                c.execute("""INSERT OR IGNORE INTO govt_schemes 
                           (name, description, benefits, eligibility, how_to_apply, department, website_url, contact_info) 
                           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", scheme)
            except Exception as e:
                pass
        conn.commit()
        conn.close()

    def create_user(self, name, phone, email, password, role, location=""):
        """Create user with proper error handling and duplicate detection"""
        conn = self.get_connection()
        c = conn.cursor()
        try:
            # First check if user already exists
            c.execute("SELECT phone FROM users WHERE phone = ?", (phone,))
            existing_user = c.fetchone()
            
            if existing_user:
                print(f"❌ User with phone {phone} already exists")
                return False
            
            # Insert new user
            c.execute("""INSERT INTO users (name, phone, email, password, role, location) 
                        VALUES (?, ?, ?, ?, ?, ?)""", (name, phone, email, password, role, location))
            conn.commit()
            print(f"✅ User {name} ({role}) created successfully")
            return True
            
        except sqlite3.IntegrityError as e:
            print(f"❌ User creation failed - Integrity error: {e}")
            return False
        except Exception as e:
            print(f"❌ Database error during user creation: {e}")
            return False
        finally:
            conn.close()

    def authenticate_user(self, phone, password):
        """Authenticate user with proper error handling"""
        conn = self.get_connection()
        c = conn.cursor()
        try:
            # Use COALESCE to handle null location values
            c.execute("SELECT name, role, COALESCE(location, '') FROM users WHERE phone = ? AND password = ?", 
                     (phone, password))
            result = c.fetchone()
            return result
        except Exception as e:
            print(f"Authentication error: {e}")
            return None
        finally:
            conn.close()

    def get_user_products(self, phone):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM products WHERE seller_phone = ? ORDER BY created_at DESC", (phone,))
            products = c.fetchall()
            return products
        except Exception as e:
            print(f"Error getting products: {e}")
            return []
        finally:
            conn.close()

    def get_all_products(self):
        """Get all active products from all sellers for marketplace"""
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM products WHERE status = 'active' ORDER BY created_at DESC")
            products = c.fetchall()
            return products
        except Exception as e:
            print(f"Error getting all products: {e}")
            return []
        finally:
            conn.close()

    def add_product(self, seller_phone, name, category, variety, unit, price, stock_qty, description=""):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute("""INSERT INTO products 
                        (seller_phone, name, category, variety, unit, price, stock_qty, description) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)""", 
                      (seller_phone, name, category, variety, unit, price, stock_qty, description))
            conn.commit()
            return c.lastrowid
        except Exception as e:
            print(f"Error adding product: {e}")
            return None
        finally:
            conn.close()

    def get_available_products(self, limit=None):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            query = """SELECT p.*, u.name as seller_name, COALESCE(u.location, '') as seller_location 
                      FROM products p 
                      JOIN users u ON p.seller_phone = u.phone 
                      WHERE p.stock_qty > 0 AND p.status = 'active' 
                      ORDER BY p.created_at DESC"""
            if limit:
                query += f" LIMIT {limit}"
            c.execute(query)
            products = c.fetchall()
            return products
        except Exception as e:
            print(f"Error getting available products: {e}")
            return []
        finally:
            conn.close()

    def search_products(self, search_term):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute("""SELECT p.*, u.name as seller_name FROM products p 
                        JOIN users u ON p.seller_phone = u.phone 
                        WHERE p.stock_qty > 0 AND p.status = 'active' 
                        AND (p.name LIKE ? OR p.category LIKE ?) 
                        ORDER BY p.name""", (f"%{search_term}%", f"%{search_term}%"))
            products = c.fetchall()
            return products
        except Exception as e:
            print(f"Error searching products: {e}")
            return []
        finally:
            conn.close()

    def add_to_cart(self, buyer_phone, product_id, quantity):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT quantity FROM cart WHERE buyer_phone = ? AND product_id = ?", 
                     (buyer_phone, product_id))
            existing = c.fetchone()
            if existing:
                new_qty = existing[0] + quantity
                c.execute("UPDATE cart SET quantity = ? WHERE buyer_phone = ? AND product_id = ?", 
                         (new_qty, buyer_phone, product_id))
            else:
                c.execute("INSERT INTO cart (buyer_phone, product_id, quantity) VALUES (?, ?, ?)", 
                         (buyer_phone, product_id, quantity))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error adding to cart: {e}")
            return False
        finally:
            conn.close()

    def get_cart_items(self, buyer_phone):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute("""SELECT c.*, p.name, p.price, p.unit, u.name as seller_name 
                        FROM cart c 
                        JOIN products p ON c.product_id = p.id 
                        JOIN users u ON p.seller_phone = u.phone 
                        WHERE c.buyer_phone = ?""", (buyer_phone,))
            items = c.fetchall()
            return items
        except Exception as e:
            print(f"Error getting cart items: {e}")
            return []
        finally:
            conn.close()

    def get_govt_schemes(self):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute("SELECT * FROM govt_schemes WHERE is_active = 1 ORDER BY name")
            schemes = c.fetchall()
            return schemes
        except Exception as e:
            print(f"Error getting schemes: {e}")
            return []
        finally:
            conn.close()

    def get_user_orders(self, phone, role):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            if role == 'seller':
                c.execute("""SELECT o.*, p.name as product_name, u.name as buyer_name 
                            FROM orders o 
                            JOIN products p ON o.product_id = p.id 
                            JOIN users u ON o.buyer_phone = u.phone 
                            WHERE o.seller_phone = ? 
                            ORDER BY o.created_at DESC""", (phone,))
            else:
                c.execute("""SELECT o.*, p.name as product_name, u.name as seller_name 
                            FROM orders o 
                            JOIN products p ON o.product_id = p.id 
                            JOIN users u ON o.seller_phone = u.phone 
                            WHERE o.buyer_phone = ? 
                            ORDER BY o.created_at DESC""", (phone,))
            orders = c.fetchall()
            return orders
        except Exception as e:
            print(f"Error getting orders: {e}")
            return []
        finally:
            conn.close()

    def record_price_data(self, product_name, market_price, location="Hamirpur"):
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO price_history (product_name, market_price, location) VALUES (?, ?, ?)", 
                     (product_name, market_price, location))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error recording price: {e}")
            return False
        finally:
            conn.close()

    def clear_cart(self, buyer_phone):
        """Clear all items from buyer's cart"""
        conn = self.get_connection()
        c = conn.cursor()
        try:
            c.execute("DELETE FROM cart WHERE buyer_phone = ?", (buyer_phone,))
            conn.commit()
            return True
        except Exception as e:
            print(f"Error clearing cart: {e}")
            return False
        finally:
            conn.close()

    def update_user(self, phone, name=None, email=None, location=None):
        """Update user profile information"""
        conn = self.get_connection()
        c = conn.cursor()
        try:
            # Build update query dynamically based on provided fields
            update_fields = []
            values = []

            if name is not None:
                update_fields.append("name = ?")
                values.append(name)
            if email is not None:
                update_fields.append("email = ?")
                values.append(email)
            if location is not None:
                update_fields.append("location = ?")
                values.append(location)

            if not update_fields:
                return False  # Nothing to update

            # Add updated_at timestamp
            update_fields.append("updated_at = CURRENT_TIMESTAMP")
            values.append(phone)  # For WHERE clause

            query = f"UPDATE users SET {', '.join(update_fields)} WHERE phone = ?"
            c.execute(query, values)
            conn.commit()

            if c.rowcount > 0:
                print(f"✅ User {phone} profile updated successfully")
                return True
            else:
                print(f"❌ User {phone} not found")
                return False

        except Exception as e:
            print(f"❌ Error updating user profile: {e}")
            return False
        finally:
            conn.close()

    def reset_database(self):
        """EMERGENCY: Reset database completely - USE WITH CAUTION"""
        try:
            if os.path.exists(self.db_path):
                os.remove(self.db_path)
                print("🗑️ Old database removed")
            self.init_database()
            print("🆕 Fresh database created")
        except Exception as e:
            print(f"Error resetting database: {e}")

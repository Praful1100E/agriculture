# utils/notifications.py - Notification management system
from datetime import datetime

class NotificationManager:
    def __init__(self):
        self.notifications = []

    def send_notification(self, title, message, notification_type="general"):
        """Send notification to user"""
        try:
            # Try system notification first
            try:
                from plyer import notification as plyer_notification
                plyer_notification.notify(
                    title=title,
                    message=message,
                    timeout=10
                )
            except:
                pass  # System notifications not available

            # Store notification for in-app display
            notification = {
                "id": len(self.notifications) + 1,
                "title": title,
                "message": message,
                "type": notification_type,
                "timestamp": datetime.now().isoformat(),
                "read": False
            }
            self.notifications.append(notification)

            return True
        except Exception as e:
            print(f"Error sending notification: {e}")
            return False

    def get_notifications(self, user_phone=None):
        """Get notifications for user"""
        return self.notifications

    def mark_as_read(self, notification_id):
        """Mark notification as read"""
        for notification in self.notifications:
            if notification["id"] == notification_id:
                notification["read"] = True
                return True
        return False

    def send_price_alert(self, product_name, old_price, new_price):
        """Send price increase alert"""
        increase_percent = ((new_price - old_price) / old_price) * 100

        title = "Price Alert 📈"
        message = f"{product_name} price increased by {increase_percent:.1f}% (₹{old_price:.2f} → ₹{new_price:.2f})"

        return self.send_notification(title, message, "price_alert")

    def send_order_notification(self, order_details):
        """Send order-related notification"""
        title = "Order Update 📦"
        message = f"Order #{order_details.get('order_number', 'Unknown')} status: {order_details.get('status', 'Updated')}"

        return self.send_notification(title, message, "order_update")
from .models import Notification

def send_notification(notification_id):
    notification = Notification.objects.get(id=notification_id)
    # 3. Simulate sending the notification for each channel
    if notification.channel == "email":
        print(f"[EMAIL] Sending notification {notification.id} to user {notification.user_id}")
    elif notification.channel == "sms":
        print(f"[SMS] Sending notification {notification.id} to user {notification.user_id}")
    elif notification.channel == "push":
        print(f"[PUSH] Sending notification {notification.id} to user {notification.user_id}")
    notification.status = "sent"
    notification.save()

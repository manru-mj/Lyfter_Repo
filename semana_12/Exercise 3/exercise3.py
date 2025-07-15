class EmailMixin:
    def send_welcome_email(self, message):
        print(f"Sending email: {message}")


class LoggerMixin:
    def log_event(self, event):
        print(f"Action Registered: {event}")


class User:
    def __init__(self, username):
        self.username = username


class RegisteredUser(User, EmailMixin, LoggerMixin):
    def welcome(self):
        self.send_welcome_email(f"Welcome, {self.username}")
        self.log_event("User has been registered")


usuario = RegisteredUser("Manrus2025")
usuario.welcome()

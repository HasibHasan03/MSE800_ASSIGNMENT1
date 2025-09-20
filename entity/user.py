class User:
    def __init__(self, user_id, username, password, role="customer"):
        self.user_id = user_id
        self.username = username
        self.password = password
        self.role = role

    def __str__(self):
        return f"{self.username} ({self.role})"

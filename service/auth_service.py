from entity.user import User
from repo.user_repo import UserRepo
from db.database import Database

class AuthService:
    logged_in_user = None

    @staticmethod
    def login(username, password):
        user = UserRepo.get_user_by_username(username)
        if user and user.password == password:
            AuthService.logged_in_user = user
            print(f"✅ Welcome {user.username} ({user.role})")
            return True
        print("❌ Invalid credentials!")
        return False

    @staticmethod
    def register(username, password):
        new_user = User(None, username, password, role="customer")
        UserRepo.add_user(new_user)
        print(f"✅ User {username} registered successfully!")

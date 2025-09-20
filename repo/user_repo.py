from db.database import Database
from entity.user import User

class UserRepo:
    @staticmethod
    def get_user_by_username(username):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=?", (username,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return User(row[0], row[1], row[2], row[3])
        return None

    @staticmethod
    def add_user(user):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                       (user.username, user.password, user.role))
        conn.commit()
        conn.close()

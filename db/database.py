import sqlite3

class Database:
    DB_NAME = "car_rental.db"

    @staticmethod
    def connect():
        return sqlite3.connect(Database.DB_NAME)

    @staticmethod
    def init_db():
        conn = Database.connect()
        cursor = conn.cursor()

        # Users
        cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            username TEXT UNIQUE,
                            password TEXT,
                            role TEXT)''')

        # Cars
        cursor.execute('''CREATE TABLE IF NOT EXISTS cars (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            make TEXT,
                            model TEXT,
                            year INTEGER,
                            mileage INTEGER,
                            available INTEGER,
                            min_rent_days INTEGER,
                            max_rent_days INTEGER,
                            daily_rate REAL)''')

        # Rentals
        cursor.execute('''CREATE TABLE IF NOT EXISTS rentals (
                            id INTEGER PRIMARY KEY AUTOINCREMENT,
                            customer_id INTEGER,
                            car_id INTEGER,
                            start_date TEXT,
                            end_date TEXT,
                            status TEXT)''')

        conn.commit()
        conn.close()

    @staticmethod
    def seed_data():
        conn = Database.connect()
        cursor = conn.cursor()

        # Add one admin if not exists
        cursor.execute("SELECT * FROM users WHERE username='admin'")
        if not cursor.fetchone():
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                           ("admin", "admin123", "admin"))

        # Add one customer
        cursor.execute("SELECT * FROM users WHERE username='john'")
        if not cursor.fetchone():
            cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                           ("john", "pass123", "customer"))

        # Add some cars
        cursor.execute("SELECT * FROM cars")
        if not cursor.fetchone():
            cursor.execute("INSERT INTO cars (make, model, year, mileage, available, min_rent_days, max_rent_days, daily_rate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           ("Toyota", "Corolla", 2020, 25000, 1, 1, 30, 40))
            cursor.execute("INSERT INTO cars (make, model, year, mileage, available, min_rent_days, max_rent_days, daily_rate) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                           ("Honda", "Civic", 2021, 15000, 1, 1, 30, 50))

        conn.commit()
        conn.close()

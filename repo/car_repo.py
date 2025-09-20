from db.database import Database
from entity.car import Car

class CarRepo:
    @staticmethod
    def add_car(car):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO cars (make, model, year, mileage, available, min_rent_days, max_rent_days, daily_rate)
                          VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
                       (car.make, car.model, car.year, car.mileage, int(car.available),
                        car.min_rent_days, car.max_rent_days, car.daily_rate))
        conn.commit()
        conn.close()

    @staticmethod
    def get_car_by_id(car_id):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars WHERE id=?", (car_id,))
        row = cursor.fetchone()
        conn.close()
        if row:
            return Car(*row)
        return None

    @staticmethod
    def get_all_cars():
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM cars")
        rows = cursor.fetchall()
        conn.close()
        return [Car(*row) for row in rows]

    @staticmethod
    def delete_car(car_id):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM cars WHERE id=?", (car_id,))
        conn.commit()
        conn.close()

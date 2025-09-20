from db.database import Database
from entity.rental import Rental

class RentalRepo:
    @staticmethod
    def add_rental(rental):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("""INSERT INTO rentals (customer_id, car_id, start_date, end_date, status)
                          VALUES (?, ?, ?, ?, ?)""",
                       (rental.customer_id, rental.car_id, rental.start_date, rental.end_date, rental.status))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_rentals():
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM rentals")
        rows = cursor.fetchall()
        conn.close()
        return [Rental(*row) for row in rows]

    @staticmethod
    def update_status(rental_id, status):
        conn = Database.connect()
        cursor = conn.cursor()
        cursor.execute("UPDATE rentals SET status=? WHERE id=?", (status, rental_id))
        conn.commit()
        conn.close()

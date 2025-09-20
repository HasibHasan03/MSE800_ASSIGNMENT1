class Rental:
    def __init__(self, rental_id, customer_id, car_id, start_date, end_date, status="Pending"):
        self.rental_id = rental_id
        self.customer_id = customer_id
        self.car_id = car_id
        self.start_date = start_date
        self.end_date = end_date
        self.status = status

    def __str__(self):
        return f"Rental {self.rental_id}: CarID {self.car_id}, CustomerID {self.customer_id}, Status: {self.status}"

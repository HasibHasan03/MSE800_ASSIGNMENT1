class Car:
    def __init__(self, car_id, make, model, year, mileage,
                 available=True, min_rent_days=1, max_rent_days=30, daily_rate=50):
        self.car_id = car_id
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.available = available
        self.min_rent_days = min_rent_days
        self.max_rent_days = max_rent_days
        self.daily_rate = daily_rate

    def __str__(self):
        return f"{self.car_id} - {self.make} {self.model} ({self.year}), Rate: ${self.daily_rate}/day"

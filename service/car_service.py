from entity.car import Car
from repo.car_repo import CarRepo
from service.auth_service import AuthService

class CarService:
    @staticmethod
    def add_car(make, model, year, mileage, rate):
        if AuthService.logged_in_user.role != "admin":
            print("❌ Only admins can add cars!")
            return
        car = Car(None, make, model, year, mileage, daily_rate=rate)
        CarRepo.add_car(car)
        print(f"✅ Car {make} {model} added.")

    @staticmethod
    def view_cars():
        for car in CarRepo.get_all_cars():
            if car.available:
                print(car)

    @staticmethod
    def delete_car(car_id):
        if AuthService.logged_in_user.role != "admin":
            print("❌ Only admins can delete cars!")
            return
        CarRepo.delete_car(car_id)
        print(f"✅ Car {car_id} deleted.")

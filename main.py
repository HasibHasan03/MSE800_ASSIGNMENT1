from db.database import Database
from service.auth_service import AuthService
from service.car_service import CarService
from service.rental_service import RentalService
from datetime import datetime

def main():
    Database.init_db()
    Database.seed_data()

    while True:
        print("\n=== Car Rental System ===")
        if not AuthService.logged_in_user:
            print("1. Login")
            print("2. Register")
            print("0. Exit")
            choice = input("Choose: ")
            if choice == "1":
                u = input("Username: ")
                p = input("Password: ")
                AuthService.login(u, p)
            elif choice == "2":
                u = input("Username: ")
                p = input("Password: ")
                AuthService.register(u, p)
            elif choice == "0":
                break
        else:
            user = AuthService.logged_in_user
            if user.role == "admin":
                print("1. Add Car")
                print("2. Delete Car")
                print("3. Manage Rentals")
                print("0. Logout")
                choice = input("Choose: ")
                if choice == "1":
                    make = input("Make: ")
                    model = input("Model: ")
                    year = int(input("Year: "))
                    mileage = int(input("Mileage: "))
                    rate = float(input("Daily Rate: "))
                    CarService.add_car(make, model, year, mileage, rate)
                elif choice == "2":
                    car_id = int(input("Car ID: "))
                    CarService.delete_car(car_id)
                elif choice == "3":
                    RentalService.manage_rentals()
                elif choice == "0":
                    AuthService.logged_in_user = None
            else:  # Customer
                print("1. View Cars")
                print("2. Book Car")
                print("0. Logout")
                choice = input("Choose: ")
                if choice == "1":
                    CarService.view_cars()
                elif choice == "2":
                    car_id = int(input("Car ID: "))
                    start = datetime.strptime(input("Start Date (YYYY-MM-DD): "), "%Y-%m-%d")
                    end = datetime.strptime(input("End Date (YYYY-MM-DD): "), "%Y-%m-%d")
                    RentalService.book_car(car_id, start, end)
                elif choice == "0":
                    AuthService.logged_in_user = None

if __name__ == "__main__":
    main()

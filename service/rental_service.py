from entity.rental import Rental
from repo.rental_repo import RentalRepo
from repo.car_repo import CarRepo
from service.auth_service import AuthService

class RentalService:
    @staticmethod
    def book_car(car_id, start_date, end_date):
        if AuthService.logged_in_user.role != "customer":
            print("❌ Only customers can book cars!")
            return
        car = CarRepo.get_car_by_id(car_id)
        if not car or not car.available:
            print("❌ Car not available!")
            return

        rental = Rental(None, AuthService.logged_in_user.user_id, car.car_id,
                        start_date.strftime("%Y-%m-%d"), end_date.strftime("%Y-%m-%d"))
        RentalRepo.add_rental(rental)
        days = (end_date - start_date).days + 1
        fee = days * car.daily_rate
        print(f"✅ Rental request created. Fee: ${fee}")

    @staticmethod
    def manage_rentals():
        if AuthService.logged_in_user.role != "admin":
            print("❌ Only admins can manage rentals!")
            return
        rentals = RentalRepo.get_all_rentals()
        for r in rentals:
            print(r)
        rental_id = int(input("Enter Rental ID to manage: "))
        decision = input("Approve (A) / Reject (R): ").strip().upper()
        RentalRepo.update_status(rental_id, "Approved" if decision == "A" else "Rejected")
        print(f"✅ Rental {rental_id} updated.")

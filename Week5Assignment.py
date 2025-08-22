# oop_activities.py

# Activity 1: Smartphone Class with Inheritance
class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self._storage = storage  # encapsulated (protected)
        self._battery = battery  # encapsulated (protected)

    def info(self):
        return f"{self.brand} {self.model} | Storage: {self._storage}GB | Battery: {self._battery}mAh"

    def call(self, number):
        return f"{self.brand} {self.model} is calling {number}..."

    def upgrade_storage(self, new_storage):
        if new_storage > self._storage:
            self._storage = new_storage
            return f"Storage upgraded! New storage: {self._storage}GB"
        else:
            return "New storage must be larger than current storage."


class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage, battery, gpu):
        super().__init__(brand, model, storage, battery)
        self.gpu = gpu

    def play_game(self, game):
        return f"{self.brand} {self.model} is running {game} with {self.gpu} GPU!"


# Activity 2: Polymorphism Challenge
class Vehicle:
    def move(self):
        return "Moving in some way..."


class Car(Vehicle):
    def move(self):
        return "Driving on the road"


class Plane(Vehicle):
    def move(self):
        return "Flying in the sky"


class Boat(Vehicle):
    def move(self):
        return "Sailing on the water"


class Bicycle(Vehicle):
    def move(self):
        return "Pedaling along the path"


# Menu Interface
def main():
    while True:
        print("\n=== Python OOP Activities ===")
        print("1. Smartphone Demo")
        print("2. Polymorphism Demo (Vehicles)")
        print("3. Exit")

        choice = input("Choose an option (1-3): ")

        if choice == "1":
            # Smartphone Demo
            phone1 = Smartphone("Samsung", "Galaxy S22", 128, 3700)
            print(phone1.info())
            print(phone1.call("0712345678"))
            print(phone1.upgrade_storage(256))

            print("\n--- Gaming Phone Demo ---")
            gphone = GamingPhone("Asus", "ROG Phone 6", 256, 6000, "Adreno 730")
            print(gphone.info())
            print(gphone.play_game("Call of Duty Mobile"))

        elif choice == "2":
            # Polymorphism Demo
            vehicles = [Car(), Plane(), Boat(), Bicycle()]
            for v in vehicles:
                print(v.move())

        elif choice == "3":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()

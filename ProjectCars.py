class Car:
    def __init__(self, car_id, name, make, body, year, value):
        self.car_id = car_id
        self.name = name
        self.make = make
        self.body = body
        self.year = year
        self.value = value

    def __str__(self):
        return f"{self.car_id},{self.name},{self.make},{self.body},{self.year},{self.value}"

    def display(self):
        print(
            f"ID: {self.car_id} | "
            f"Name: {self.name} | "
            f"Make: {self.make} | "
            f"Body: {self.body} | "
            f"Year: {self.year} | "
            f"Value: ${self.value}"
        )


def load_cars(filename):
    cars = []

    file = open(filename, "r")

    for line in file:
        line = line.strip()
        if line != "":
            parts = line.split(",")

            car_id = int(parts[0])
            name = parts[1]
            make = parts[2]
            body = parts[3]
            year = int(parts[4])
            value = float(parts[5])

            car = Car(car_id, name, make, body, year, value)
            cars.append(car)

    file.close()
    return cars


def save_cars(filename, cars):
    file = open(filename, "w")

    for car in cars:
        file.write(str(car) + "\n")

    file.close()
    print("Data saved to file.")


def find_car_by_id(cars, car_id):
    for car in cars:
        if car.car_id == car_id:
            return car
    return None


def add_car(cars):
    car_id = int(input("Enter Car ID: "))

    if find_car_by_id(cars, car_id) != None:
        print("A car with that ID already exists.")
        return

    name = input("Enter name: ")
    make = input("Enter make: ")
    body = input("Enter body type: ")
    year = int(input("Enter year: "))
    value = float(input("Enter value: "))

    car = Car(car_id, name, make, body, year, value)
    cars.append(car)
    print("Car added.")


def search_car(cars):
    search_id = int(input("Enter Car ID to search: "))
    car = find_car_by_id(cars, search_id)

    if car == None:
        print("Car not found.")
    else:
        car.display()


def edit_car(cars):
    search_id = int(input("Enter Car ID to edit: "))
    car = find_car_by_id(cars, search_id)

    if car == None:
        print("Car not found.")
        return

    print("Leave blank to keep current value.")

    new_name = input(f"New name ({car.name}): ")
    new_make = input(f"New make ({car.make}): ")
    new_body = input(f"New body ({car.body}): ")
    new_year = input(f"New year ({car.year}): ")
    new_value = input(f"New value ({car.value}): ")

    if new_name != "":
        car.name = new_name
    if new_make != "":
        car.make = new_make
    if new_body != "":
        car.body = new_body
    if new_year != "":
        car.year = int(new_year)
    if new_value != "":
        car.value = float(new_value)

    print("Car updated.")


def remove_car(cars):
    search_id = int(input("Enter Car ID to remove: "))
    car = find_car_by_id(cars, search_id)

    if car == None:
        print("Car not found.")
    else:
        cars.remove(car)
        print("Car removed.")


def print_car_list(cars):
    if len(cars) == 0:
        print("No cars in inventory.")
    else:
        print("\n--- Car Inventory ---")
        for car in cars:
            car.display()


def main():
    filename = "data.txt"
    cars = load_cars(filename)

    print("Welcome to the Car Inventory Program")

    choice = ""
    while choice != "6":
        print("\nMain Menu")
        print("1. Add a car")
        print("2. Search for car")
        print("3. Edit car info")
        print("4. Remove a car")
        print("5. Print the car list")
        print("6. Save the data to a file and Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_car(cars)
        elif choice == "2":
            search_car(cars)
        elif choice == "3":
            edit_car(cars)
        elif choice == "4":
            remove_car(cars)
        elif choice == "5":
            print_car_list(cars)
        elif choice == "6":
            save_cars(filename, cars)
            print("Goodbye!")
        else:
            print("Invalid choice.")


main()



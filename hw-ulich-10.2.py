# 1
import json
import pickle

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.speed = 0
        self.fuel_level = 100

    def accelerate(self, speed_increase):
        self.speed += speed_increase
        print(f"The {self.make} {self.model} is now going {self.speed} km/h.")

    def refuel(self, fuel_amount):
        self.fuel_level += fuel_amount
        if self.fuel_level > 100:
            self.fuel_level = 100
        print(f"The {self.make} {self.model} has been refueled. Fuel level is now {self.fuel_level}%.")

    def to_json(self):
        return json.dumps({
            "make": self.make,
            "model": self.model,
            "year": self.year,
            "speed": self.speed,
            "fuel_level": self.fuel_level
        })

    def from_json(self, json_data):
        data = json.loads(json_data)
        self.make = data["make"]
        self.model = data["model"]
        self.year = data["year"]
        self.speed = data["speed"]
        self.fuel_level = data["fuel_level"]

    def to_pickle(self):
        return pickle.dumps(self)

    @staticmethod
    def from_pickle(pickle_data):
        return pickle.loads(pickle_data)




# проверка
my_car = Car("Toyota", "Corolla", 2020)

json_data = my_car.to_json()
print(json_data)

new_car = Car("", "", 0)
new_car.from_json(json_data)
print(new_car.make, new_car.model, new_car.year)

pickle_data = my_car.to_pickle()
print(pickle_data)

restored_car = Car.from_pickle(pickle_data)
print(restored_car.make, restored_car.model, restored_car.year)

# 2

import json
import pickle

class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre

    def display_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")

    def update_genre(self, new_genre):
        self.genre = new_genre
        print(f"Genre updated to: {self.genre}")

    def pack_to_json(self):
        book_data = {
            "title": self.title,
            "author": self.author,
            "genre": self.genre
        }
        return json.dumps(book_data, indent=4)

    def unpack_from_json(self, json_data):
        book_data = json.loads(json_data)
        self.title = book_data["title"]
        self.author = book_data["author"]
        self.genre = book_data["genre"]

    def pack_to_pickle(self):
        return pickle.dumps(self)

    def unpack_from_pickle(self, pickle_data):
        unpacked_book = pickle.loads(pickle_data)
        self.title = unpacked_book.title
        self.author = unpacked_book.author
        self.genre = unpacked_book.genre


# Проверка
book = Book("The Great Gatsby", "F. Scott Fitzgerald", "Fiction")

book.display_info()

book.update_genre("Classic Literature")

json_data = book.pack_to_json()
print(json_data)

new_book = Book("", "", "")
new_book.unpack_from_json(json_data)
new_book.display_info()

pickle_data = book.pack_to_pickle()

unpacked_book = Book("", "", "")
unpacked_book.unpack_from_pickle(pickle_data)
unpacked_book.display_info()

# 3
import json

class StadiumAdapter:
    def __init__(self, stadium):
        self.stadium = stadium

    def to_json(self):
        return json.dumps({
            "name": self.stadium.name,
            "capacity": self.stadium.capacity,
            "location": self.stadium.location
        })

    def from_json(self, json_data):
        data = json.loads(json_data)
        self.stadium.name = data["name"]
        self.stadium.capacity = data["capacity"]
        self.stadium.location = data["location"]
        return self.stadium

class Stadium:
    def __init__(self, name, capacity, location):
        self.name = name
        self.capacity = capacity
        self.location = location

    def get_info(self):
        return f"Name: {self.name}, Capacity: {self.capacity}, Location: {self.location}"

    def update_capacity(self, new_capacity):
        self.capacity = new_capacity

    def pack_to_json(self):
        adapter = StadiumAdapter(self)
        return adapter.to_json()

    def unpack_from_json(self, json_data):
        adapter = StadiumAdapter(self)
        return adapter.from_json(json_data)

    def pack_to_pickle(self):
        import pickle
        return pickle.dumps(self)

    def unpack_from_pickle(self, pickle_data):
        import pickle
        return pickle.loads(pickle_data)

# проверка
stadium = Stadium("Estadio Santiago Bernabéu", 81044, "Madrid, Spain")
print(stadium.get_info())

json_data = stadium.pack_to_json()
print(json_data)

unpacked_stadium = stadium.unpack_from_json(json_data)
print(unpacked_stadium.get_info())

pickle_data = stadium.pack_to_pickle()
print(pickle_data)

unpacked_stadium = stadium.unpack_from_pickle(pickle_data)
print(unpacked_stadium.get_info())
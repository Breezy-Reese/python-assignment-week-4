# ----------------------------
# Assignment 1: Custom Class with Inheritance
# ----------------------------

class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def device_info(self):
        print(f"Device: {self.brand} {self.model}")

class Smartphone(Device):
    def __init__(self, brand, model, storage, battery_life):
        super().__init__(brand, model)
        self.storage = storage
        self.battery_life = battery_life

    def make_call(self, contact):
        print(f"📞 Calling {contact} from {self.brand} {self.model}")

    def device_info(self):
        print(f"Smartphone: {self.brand} {self.model}, Storage: {self.storage}GB, Battery: {self.battery_life} hours")

class Tablet(Device):
    def __init__(self, brand, model, screen_size):
        super().__init__(brand, model)
        self.screen_size = screen_size

    def device_info(self):
        print(f"Tablet: {self.brand} {self.model}, Screen Size: {self.screen_size}\"")


# Create objects for Assignment 1
phone = Smartphone("Samsung", "Galaxy S23", 256, 24)
tablet = Tablet("Apple", "iPad Pro", 12.9)

print("=== Assignment 1: Device Information ===")
phone.device_info()
phone.make_call("Alice")
tablet.device_info()


# ----------------------------
# Assignment 2: Polymorphism Challenge
# ----------------------------

class Animal:
    def move(self):
        print("The animal is moving.")

class Dog(Animal):
    def move(self):
        print("🐕 The dog is running")

class Bird(Animal):
    def move(self):
        print("🐦 The bird is flying")

class Fish(Animal):
    def move(self):
        print("🐟 The fish is swimming")


# Create objects for Assignment 2
animals = [Dog(), Bird(), Fish()]

print("\n=== Assignment 2: Animal Movements ===")
for animal in animals:
    animal.move()

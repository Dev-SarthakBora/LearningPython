# polymorphism.py
class Cat:
    def speak(self):
        print("Meow")

class Dog:
    def speak(self):
        print("Woof")

# Polymorphism: same method name, different behavior
def animal_sound(animal):
    animal.speak()

cat = Cat()
dog = Dog()

animal_sound(cat)  # Meow
animal_sound(dog)  # Woof


# inheritance.py
# Parent class
class Animal:
    def speak(self):
        print("Some generic sound")

# Child class
class Dog(Animal):
    def speak(self):
        print("Woof! Woof!")

dog = Dog()
dog.speak()  # Woof! Woof!


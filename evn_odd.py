class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Snoopy", 3)
my_dog.bark()  # Snoopy says woof!

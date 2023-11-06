from my_package.module1 import Dog
from my_package.module2 import Beagle

if __name__ == "__main__":
    # Creating instances and demonstrate functionality
    dog = Dog("Buddy")
    print(dog.bark())

    beagle = Beagle("Max", 3)
    print(beagle.description())
    print(beagle.bark())  # Accessing method from the parent class

# Example 1
class Dog: # class
    def __init__(self, name, age, color):
        self.name = name # instance
        self.age = age
        self.color = color


    def bark(self):
        return f"{self.name} is barking!"
    

    def eat(self, food):
        return f"{self.name} is eating {food}."
    
    
    def sleep(self):
        return f"{self.name} is sleeping."
    

# Creating objects of Dog class
dog1 = Dog("Rex", 5, "Black")
dog2 = Dog("Bobby", 3, "Brown")

print(dog1.bark())
print(dog2.eat("chicken"))
print(dog1.sleep())


# Example 2
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = 0 # Initailly, the car isn't moving

    
    def accelerate(self):
        self.speed += 5
        return f"The {self.brand} is going at {self.speed} mph."
    
    
    def brake(self):
        self.speed -= 5
        return f"The {self.brand} {self.model} is going at {self.speed} mph."
    
car1 = Car("Tesla", "Model S", 2022)
car2 = Car("BMW", "i8", 2023)

print("\n")
print(car1.accelerate())
print(car1.accelerate())
print(car1.brake())
print(car2.accelerate())

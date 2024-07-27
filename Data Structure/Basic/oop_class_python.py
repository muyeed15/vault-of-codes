# Example 1
class Student:
    school_name = "XYZ High School" # class state

    def __init__(self, name):
        self.name = name # instance state
    

    def display_name(self): # regular method
        return self.name
    
    
    @classmethod
    def change_scholl_name(cls, new_name): # class method
        cls.school_name = new_name


    @staticmethod
    def is_full_name(name): # static method
        return len(name.split()) > 1
    

student1 = Student("Alice")

print(student1.display_name())
print(Student.school_name)

Student.change_scholl_name("ABC High School")
print(Student.school_name)

print(Student.is_full_name("Alice"))
print(Student.is_full_name("Alice Johnson"))


# Example 2
class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    
    def display_ingredients(self):
        """Instace method: uses 'self' and can modify the object's state"""
        return self.ingredients
    
    
    @classmethod
    def margherita(cls):
        """Class method: uses 'cls' and can't modify a specific object state, but can modify class state"""
        return cls(['mozzarella', 'tomatoes'])
    

    @staticmethod
    def validate_ingredient(ingredient):
        """Static method: doesn't use either 'self' or 'cls;. Can't modify obejct or class state."""
        if ingredient in ['mozzarella', 'tomatoes', 'olives', 'ham', 'mushrooms']:
            return True
        else:
            return False
        


my_pizza = Pizza(['mozzarella', 'tomatoes', 'ham'])
print(my_pizza.display_ingredients())

margherita_pizza = Pizza.margherita()
print(margherita_pizza.display_ingredients())

print(Pizza.validate_ingredient('pineapple'))
print(Pizza.validate_ingredient('ham'))

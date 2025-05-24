# Python OOP Assignments - Complete Solutions
# All 21 assignments with detailed implementations

print("=" * 60)
print("Python OOP Assignments - Complete Solutions")
print("=" * 60)

# 1. Using self
print("\n1. Using self")
print("-" * 30)

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def display(self):
        print(f"Student Name: {self.name}")
        print(f"Marks: {self.marks}")

# Test
student1 = Student("Alice", 95)
student1.display()

# 2. Using cls
print("\n2. Using cls")
print("-" * 30)

class Counter:
    count = 0  # Class variable
    
    def __init__(self):
        Counter.count += 1
    
    @classmethod
    def get_count(cls):
        return cls.count
    
    @classmethod
    def reset_count(cls):
        cls.count = 0

# Test
c1 = Counter()
c2 = Counter()
c3 = Counter()
print(f"Total objects created: {Counter.get_count()}")

# 3. Public Variables and Methods
print("\n3. Public Variables and Methods")
print("-" * 30)

class Car:
    def __init__(self, brand):
        self.brand = brand  # Public variable
    
    def start(self):  # Public method
        print(f"{self.brand} car is starting!")

# Test
car1 = Car("Toyota")
print(f"Car brand: {car1.brand}")  # Accessing public variable
car1.start()  # Calling public method

# 4. Class Variables and Class Methods
print("\n4. Class Variables and Class Methods")
print("-" * 30)

class Bank:
    bank_name = "Default Bank"  # Class variable
    
    def __init__(self, account_holder):
        self.account_holder = account_holder
    
    @classmethod
    def change_bank_name(cls, name):
        cls.bank_name = name
    
    def display_info(self):
        print(f"Bank: {self.bank_name}, Account Holder: {self.account_holder}")

# Test
account1 = Bank("John")
account2 = Bank("Jane")

print("Before changing bank name:")
account1.display_info()
account2.display_info()

Bank.change_bank_name("New Global Bank")

print("\nAfter changing bank name:")
account1.display_info()
account2.display_info()

# 5. Static Variables and Static Methods
print("\n5. Static Variables and Static Methods")
print("-" * 30)

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

# Test
result = MathUtils.add(10, 20)
print(f"10 + 20 = {result}")

# 6. Constructors and Destructors
print("\n6. Constructors and Destructors")
print("-" * 30)

class Logger:
    def __init__(self, name):
        self.name = name
        print(f"Logger '{self.name}' created!")
    
    def __del__(self):
        print(f"Logger '{self.name}' destroyed!")

# Test
logger1 = Logger("SystemLogger")
logger2 = Logger("ErrorLogger")
# Objects will be destroyed when they go out of scope

# 7. Access Modifiers: Public, Private, and Protected
print("\n7. Access Modifiers")
print("-" * 30)

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name          # Public
        self._salary = salary     # Protected
        self.__ssn = ssn          # Private

# Test
emp = Employee("Bob", 50000, "123-45-6789")

print(f"Public name: {emp.name}")  # Works fine
print(f"Protected salary: {emp._salary}")  # Works but not recommended

try:
    print(f"Private SSN: {emp.__ssn}")  # This will cause an error
except AttributeError as e:
    print(f"Error accessing private variable: {e}")

# Name mangling allows access with _ClassName__variable
print(f"Private SSN (via name mangling): {emp._Employee__ssn}")

# 8. The super() Function
print("\n8. The super() Function")
print("-" * 30)

class Person:
    def __init__(self, name):
        self.name = name
        print(f"Person constructor called for {name}")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)  # Call parent constructor
        self.subject = subject
        print(f"Teacher constructor called for {name}, subject: {subject}")
    
    def display(self):
        print(f"Teacher: {self.name}, Subject: {self.subject}")

# Test
teacher1 = Teacher("Mr. Smith", "Mathematics")
teacher1.display()

# 9. Abstract Classes and Methods
print("\n9. Abstract Classes and Methods")
print("-" * 30)

from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

# Test
rect = Rectangle(5, 10)
print(f"Rectangle area: {rect.area()}")

# 10. Instance Methods
print("\n10. Instance Methods")
print("-" * 30)

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed
    
    def bark(self):  # Instance method
        print(f"{self.name} the {self.breed} is barking: Woof! Woof!")

# Test
dog1 = Dog("Buddy", "Golden Retriever")
dog1.bark()

# 11. Class Methods
print("\n11. Class Methods")
print("-" * 30)

class Book:
    total_books = 0  # Class variable
    
    def __init__(self, title):
        self.title = title
        Book.increment_book_count()
    
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books

# Test
book1 = Book("Python Programming")
book2 = Book("Data Structures")
book3 = Book("Algorithms")

print(f"Total books: {Book.get_total_books()}")

# 12. Static Methods
print("\n12. Static Methods")
print("-" * 30)

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(celsius):
        return (celsius * 9/5) + 32
    
    @staticmethod
    def fahrenheit_to_celsius(fahrenheit):
        return (fahrenheit - 32) * 5/9

# Test
temp_c = 25
temp_f = TemperatureConverter.celsius_to_fahrenheit(temp_c)
print(f"{temp_c}°C = {temp_f}°F")

# 13. Composition
print("\n13. Composition")
print("-" * 30)

class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start_engine(self):
        print(f"Engine with {self.horsepower} HP is starting!")

class Car:
    def __init__(self, brand, engine):
        self.brand = brand
        self.engine = engine  # Composition
    
    def start_car(self):
        print(f"Starting {self.brand} car...")
        self.engine.start_engine()

# Test
engine1 = Engine(200)
car1 = Car("Honda", engine1)
car1.start_car()

# 14. Aggregation
print("\n14. Aggregation")
print("-" * 30)

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []  # Aggregation
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def show_employees(self):
        print(f"Department: {self.name}")
        for emp in self.employees:
            print(f"  - {emp.name} ({emp.position})")

class Employee:
    def __init__(self, name, position):
        self.name = name
        self.position = position

# Test
emp1 = Employee("Alice", "Developer")
emp2 = Employee("Bob", "Manager")

dept = Department("IT")
dept.add_employee(emp1)
dept.add_employee(emp2)
dept.show_employees()

# 15. Method Resolution Order (MRO) and Diamond Inheritance
print("\n15. Method Resolution Order (MRO)")
print("-" * 30)

class A:
    def show(self):
        print("Method from class A")

class B(A):
    def show(self):
        print("Method from class B")

class C(A):
    def show(self):
        print("Method from class C")

class D(B, C):
    pass

# Test
d = D()
d.show()  # Will call B's show() due to MRO
print(f"MRO for class D: {D.__mro__}")

# 16. Function Decorators
print("\n16. Function Decorators")
print("-" * 30)

def log_function_call(func):
    def wrapper(*args, **kwargs):
        print("Function is being called")
        return func(*args, **kwargs)
    return wrapper

@log_function_call
def say_hello(name):
    print(f"Hello, {name}!")

# Test
say_hello("World")

# 17. Class Decorators
print("\n17. Class Decorators")
print("-" * 30)

def add_greeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@add_greeting
class Person:
    def __init__(self, name):
        self.name = name

# Test
person = Person("Alice")
print(person.greet())

# 18. Property Decorators
print("\n18. Property Decorators")
print("-" * 30)

class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value
    
    @price.deleter
    def price(self):
        print("Price deleted!")
        del self._price

# Test
product = Product("Laptop", 1000)
print(f"Product price: ${product.price}")

product.price = 1200
print(f"Updated price: ${product.price}")

del product.price

# 19. callable() and __call__()
print("\n19. callable() and __call__()")
print("-" * 30)

class Multiplier:
    def __init__(self, factor):
        self.factor = factor
    
    def __call__(self, value):
        return value * self.factor

# Test
multiply_by_3 = Multiplier(3)
print(f"Is callable: {callable(multiply_by_3)}")
result = multiply_by_3(10)  # Calling object like a function
print(f"10 * 3 = {result}")

# 20. Creating a Custom Exception
print("\n20. Custom Exception")
print("-" * 30)

class InvalidAgeError(Exception):
    def __init__(self, age, message="Age must be 18 or older"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def check_age(age):
    if age < 18:
        raise InvalidAgeError(age)
    return "Age is valid"

# Test
try:
    check_age(16)
except InvalidAgeError as e:
    print(f"Error: {e}")

try:
    result = check_age(25)
    print(result)
except InvalidAgeError as e:
    print(f"Error: {e}")

# 21. Make a Custom Class Iterable
print("\n21. Custom Iterable Class")
print("-" * 30)

class Countdown:
    def __init__(self, start):
        self.start = start
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start <= 0:
            raise StopIteration
        self.start -= 1
        return self.start + 1

print("Countdown from 5:")
for num in Countdown(5):
    print(num)

print("\n" + "=" * 60)
print("All assignments completed successfully!")
print("=" * 60)
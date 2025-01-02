# FACTORIAL
# def factorial(n):
#     if n <= 1:
#         return 1
#     result = 1
#     for i in range(1, n + 1):
#         result *= i
#     return result
# n = int(input("Enter a number: "))
# print(factorial(n))

# BINARY SEARCH
# def binary_search(arr, target):
#     left = 0
#     right = len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             left = mid + 1
#         else:
#             right = mid - 1

# arr = [1, 7, 6, 4, 5]
# arr.sort();
# target = int(input("Enter your target number: "))
# result = binary_search(arr, target)    
# if result != 0:
#     print(f"Number found at index: {result}")
# else:
#     print("Number not found")

# Random_no
# import random
# random_no = random.random()
# print(random_no)

# Raise an error
# def divide(x, y):
#     if y == 0:
#         raise ZeroDivisionError("Division by 0 gives 0")
#     return x/y
# try:
#     result = divide(10, 0)
#     print(int(result))
# except ZeroDivisionError as e:
#     print("Error: ", e)

#CONSTRUCTOR, class, self example
# class Car:
#     def __init__(self, name, color):
#         self.name = name
#         self.color = color
#     def describe(self):
#         print(f"Name of the car: {self.name} and the Colour: {self.color}")
        
# car1 = Car("Toyota", "Black")
# car2 = Car("Mercedes", "White")

# car1.describe()
# print(car2.name)

# Multiple inheritance
# class Flyer:
#     def fly(self):
#         print("I can fly!")

# class Swimmer:
#     def swim(self):
#         print("I can swim!")

# class FlyingFish(Flyer, Swimmer):
#     def fish(self):
#         print("I am fish")

# flying = FlyingFish()
# flying.fly()
# flying.swim()
# flying.fish()

# class A:
#     def display(self):
#         print("Class A")

# class B:
#     def display(self):
#         print("Class B")

# class C(B, A):
#     pass

# obj = C()
# obj.display()  # Output depends on Method Resolution Order (MRO) . priotirize the left most class

#fibo
n = int(input("Enter the number of terms: "))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

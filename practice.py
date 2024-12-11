x, y = map(int, input("Enter the coordinates of the point(x, y): ").split())

if x == 0 and y == 0:
    print("The point is at the origin")
elif x == 0:
    print("The point is at the x-axis")
elif y == 0:
    print("The point is at y-axis")
else:
    print("The point does not lie on either axis or the origin")
# def factorial(n):
#     fact = 1
#     if n <= 0:
#         return 1
    
#     for i in range(1, n + 1):
#         fact *= i
#     return fact
        
# n = int(input("Enter value: "))
# print(factorial(n))
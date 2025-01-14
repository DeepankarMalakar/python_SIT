def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

num = int(input("Enter a number: "))
print("The number is", check_even_odd(num))
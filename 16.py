# Program to print even numbers from a given list

def print_even_numbers(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number)

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
print_even_numbers(my_list)
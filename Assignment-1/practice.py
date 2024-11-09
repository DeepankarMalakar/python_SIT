number = int(input("Enter a five digit number: "))   #23456

if 10000 <= number <= 99999:
    new_number = 0
    place_value = 1

    while number > 0:
        digit = number % 10
        new_digit = (digit + 1) % 10
        new_number = new_digit * place_value + new_number
        place_value = place_value * 10
        number = number // 10
    print(f"The new number is: {new_number}")
else:
    print("Please enter a valid five-digit number!")
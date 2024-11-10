# Decrement the values by 1
num = int(input("Enter a five digit number: "))    #23456

if 10000 <= num <=99999:
    new_number = 0
    place_value = 1

    while num > 0:
        digit = num % 10
        new_digit = (digit - 1) % 10
        new_number = new_digit * place_value + new_number
        place_value = place_value *  10
        num = num // 10
    print(f"The new number is: {new_number}")
else:
    print("Please enter valid five-digit number!")
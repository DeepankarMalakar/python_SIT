# If a five-digit number is input through the keyboard, write a program to calculate the sum of 
# its digits.(Hint: Use the modulus operator ‘%’)

num = int(input("Enter five digit number: "))
num_to_str = str(num)       # converted to string
listing = list(num_to_str)  # converted to list e.g ["1", "2", "3", "4", "5"]
total_sum = 0

for value in listing:
    total_sum += int(value)
print(total_sum)
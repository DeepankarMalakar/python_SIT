def is_palindrome(num):
    return str(num) == str(num)[::-1]

num = int(input("Enter a number: "))
print("Palindrome" if is_palindrome(num) else "Not a Palindrome")
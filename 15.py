# Program that accepts a string and calculate the count of uppercase and lowercase letters

import re
def calculate_letters(text):
    lowercase_count = len(re.findall('[a-z]', text))
    uppercase_count = len(re.findall('[A-Z]', text))
    return lowercase_count, uppercase_count

text = "Hello WORLD"

lowercase, uppercase = calculate_letters(text)
print("Lowercase letters count: ", lowercase)
print("Uppercase letters count: ", uppercase)
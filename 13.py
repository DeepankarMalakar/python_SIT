# Program to count the number of unique capital letters in a file 
import re

def count_unique_capitals(filename):
    """
    Args:
        filename (str): The name of the file to process.

    Returns:
        int: The number of unique capital letters.
    """

    with open(filename, 'r') as file:
        text = file.read()

    # Extract all capital letters
    capital_letters = re.findall(r'[A-Z]', text)

    # Find unique capital letters using a set
    unique_capitals = set(capital_letters)

    return len(unique_capitals)


filename = "your_file.txt"
unique_count = count_unique_capitals(filename)
print("Number of unique capital letters:", unique_count)
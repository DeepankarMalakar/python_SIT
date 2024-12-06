# Write a program to display all the lines in a file python.txt along with line/record number

def print_file_with_line_numbers(filename):
    """Prints the content of a file with line numbers.

    Args:
        filename: The name of the file to process.
    """

    with open(filename, 'r') as file:
        line_number = 1
        for line in file:
            print(f"{line_number}. {line}", end='')
            line_number += 1


filename = "python.txt"
print_file_with_line_numbers(filename)
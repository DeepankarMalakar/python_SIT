# Program to check whether the number falls in the range
def is_in_range(start, num, end):
    return start <= num <= end

start = 5
num = 10
end = 20

if is_in_range(start, num, end):
    print(f"The number {num} falls in range between {start} and {end}")
else:
    print(f"The number {num} doesnt falls in range between {start} and {end}")
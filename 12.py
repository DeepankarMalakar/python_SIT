# Who is GOAT
def goat(a, b, c):
    if a >= b and a >= c:
        return print(f"{a} A is the GOAT")
    elif b >= a and b >= c:
        return print(f"{b} B is the GOAT")
    else:
        return print(f"{c} C is the GOAT")

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
goat(a, b, c)
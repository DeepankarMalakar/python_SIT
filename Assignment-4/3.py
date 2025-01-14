def fibonacci_sum(n):
    a, b = 0, 1
    sum_fib = 0
    for _ in range(n):
        sum_fib += a
        a, b = b, a + b
    return sum_fib

n = int(input("Enter the number of terms: "))
print("Sum of Fibonacci series:", fibonacci_sum(n))
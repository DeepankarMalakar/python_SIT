nums = list(map(int, input("Enter numbers separated by space: ").split()))
sum_pos = sum(n for n in nums if n > 0)
sum_neg = sum(n for n in nums if n < 0)

print("Sum of positive numbers:", sum_pos)
print("Sum of negative numbers:", sum_neg)
#Q2. Find the sum 1+2+3+4...+100 
def sum_of_num(n):
    sum = 0
    for i in range(1, n+1): 
        sum+=i
    return sum
    
sum_of_num = sum_of_num(100)
print("Sum of numbers from 1-100 will be:", sum_of_num)
# 14. A  machine  is  purchased  which  will  produce  earning  of  Rs.  1000  per  year  while  it  lasts. The machine costs Rs. 6000 and will have a salvage of Rs. 2000 when it is condemned. If 12 percent 
# per  annum  can  be  earned  on  alternate  investments  what  would  be  the  minimum  life  of  the 
# machine to make it a more attractive investment compared to alternative investment?

# Solution with a limit for n
cost = 6000
salvage = 2000
annual_earning = 1000
alternative_rate = 0.12

n = 0
max_years = 100

while n <= max_years:
    machine_value = salvage + (annual_earning * n)
    alternative_investment = cost * (1 + alternative_rate) ** n
    if machine_value > alternative_investment:
        break
    n += 1

if n > max_years:
    print("The machine cannot become a better investment within 100 years.")
else:
    print(f"The minimum life of the machine should be {n} years.")
# Exercise 35: Dog Years

human_years = float(input("Enter the number of human years:"))
if human_years < 0:
    print("Invalid")
else: 
    if human_years < 2:
        dog_years = human_years * 10.5
    else: dog_years = 2 * 10.5 + (human_years - 2)*4
    
print("Dog years:",dog_years)
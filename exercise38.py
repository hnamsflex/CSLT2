# Read the name of the month from the user
month_name = input("Enter the name of a month: ")
num_days=""

# Convert the month name to lowercase 
month_name = month_name.lower()

if month_name == "january" or month_name == "march" or month_name == "may" or month_name == "july" or month_name == "august" or month_name == "october" or month_name == "december":
    num_days = 31
elif month_name == "april" or month_name == "june" or month_name == "september" or month_name == "november":
    num_days = 30
elif month_name == "february":
    print("The month of February has 28 or 29 days.")
else:
    print("Invalid month name. Please enter a valid month.")
# Display the number of days in the month
if num_days != "" :
    print(f"The month of {month_name.capitalize()} has {num_days} days.")

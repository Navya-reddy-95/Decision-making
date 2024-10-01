'''
Ask a user for their birth year encoded as two digits (like "62") and for the current year, also encoded as two digits (like "99"). Write a program to find the users current age in years.
Input format:
Input consists of 2 integers
The first integer corresponds to the last 2 digits of the birth year
The second integer corresponds to the last 2 digits of the current year
Output format:
Print the user's current age
Refer below sample output for formatting.
Sample Input:
62
00
Sample Output:
38
'''
# Function to calculate age
def calculate_age(birth_year_last2, current_year_last2):
    # Assume the birth year and current year are in the 1900s or 2000s
    # Handle the century based on the current year
    if current_year_last2 < birth_year_last2:
        current_year = 2000 + current_year_last2
    else:
        current_year = 1900 + current_year_last2
        
    birth_year = 1900 + birth_year_last2
    
    age = current_year - birth_year
    return age

# Read input from the user
birth_year_last2 = int(input().strip())
current_year_last2 = int(input().strip())

# Calculate age
age = calculate_age(birth_year_last2, current_year_last2)

# Output the age
print(age)

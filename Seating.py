'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z. A single lab needs to be allocated to a class of 'n' students. How many of the 3 labs can accommodate 'n' students?
Input format:
Input consists of 4 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the number of students(x)
Output format:
Print the number of labs which can accommodate the 'n' number of students
Refer the Sample output for formatting
Sample Input:
30
40
20
25
Sample Output:
2 
'''
# Function to count labs that can accommodate the number of students
def count_accommodating_labs(capacities, num_students):
    count = 0
    for capacity in capacities:
        if capacity >= num_students:
            count += 1
    return count

# Read input from the user
a = int(input().strip())  # Capacity of L1
b = int(input().strip())  # Capacity of L2
c = int(input().strip())  # Capacity of L3
num_students = int(input().strip())  # Number of students

# Store the capacities in a list
capacities = [a, b, c]

# Count labs that can accommodate the number of students
accommodating_labs_count = count_accommodating_labs(capacities, num_students)

# Output the count of labs
print(accommodating_labs_count)


'''
There are 3 labs in the CSE department are L1, L2, and L3 with a seating capacity of x, y, and z respectively. One of the 3 labs has been allocated for ACE training. Out of the available labs, find the lab which has minimal seating capacity.
Input format:
Input consists of 3 integers and a string
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
The fourth input denotes the lab which is allocated for ACE training
Output format:
Print the minimal seating capacity lab amongst the available labs.
Refer the Sample output for formatting
Sample Input:
30
40
20
L3
Sample Output:
L1
'''
# Function to find the lab with minimal seating capacity
def find_min_capacity_lab(capacities, allocated_lab):
    # Remove the allocated lab from the dictionary
    del capacities[allocated_lab]
    
    # Find the lab with the minimum capacity
    min_lab = min(capacities, key=capacities.get)
    return min_lab

# Read input from the user
a = int(input().strip())  # Capacity of L1
b = int(input().strip())  # Capacity of L2
c = int(input().strip())  # Capacity of L3
allocated_lab = input().strip()  # Allocated lab

# Store the capacities in a dictionary
capacities = {
    "L1": a,
    "L2": b,
    "L3": c
}

# Find the lab with the minimal seating capacity
min_lab = find_min_capacity_lab(capacities, allocated_lab)

# Output the lab with the minimal capacity
print(min_lab)

'''
There are 3 labs in the CSE department(L1, L2, and L3) with a seating capacity of x, y, and z respectively. Find the lab which has minimal seating capacity.  
Input format:
Input consists of 3 integers
The first input denotes the seating capacity of L1(a)
The second input denotes the seating capacity of L2(b)
The third input denotes the seating capacity of L3(c)
Output format:
Print the minimal seating lab capacity
Refer the Sample output for formatting
Sample Input:
30
40
20
Sample Output:
L3
'''
L1=int(input())
L2=int(input())
L3=int(input())
if((L1<L2) and (L1<L3)):
    print("L1")
elif(L2<L3 and L2<L1):
    print("L2")
else:
    print("L3")


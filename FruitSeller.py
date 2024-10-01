'''
 A fruit seller buys a dozen of banana at Rs.X. He sells 1 banana at Rs.Y. Write a program to determine the profit or loss in Rs. for the fruitseller.
Input format:
Input consists of 2 floating point numbers
The first input corresponds to the total cost(X)
The second input corresponds to the sold cost(Y)
Output format:
Print "Profit or Loss" with Rupees.
Sample Input:
60
4
Sample Output:
Loss : Rs.12.00
'''
# Function to calculate profit or loss
def calculate_profit_loss(total_cost, selling_price_per_banana):
    # Total selling price for a dozen bananas
    total_selling_price = selling_price_per_banana * 12
    
    # Calculate profit or loss
    profit_or_loss = total_selling_price - total_cost
    
    return profit_or_loss

# Read input from the user
total_cost = float(input())
selling_price_per_banana = float(input())

# Calculate profit or loss
result = calculate_profit_loss(total_cost, selling_price_per_banana)

# Determine and print the result
if result > 0:
    print(f"Profit : Rs.{result:.2f}")
elif result < 0:
    print(f"Loss : Rs.{abs(result):.2f}")
else:
    print("No Profit No Loss")

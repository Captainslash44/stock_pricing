"""
This code gives you the best value for buying and selling stock
on different days.
"""


def Stock_pricing(array):

    lowest_buying = 9999999999 #This number represents infinity.
    highest_selling = 0
    lowest_day , highest_day = 0, 0

    for i in range(len(array)):

        if array[i] < lowest_buying and i != (len(array) - 1):
            lowest_buying = array[i]
            lowest_day = i

        if array[i] > highest_selling and i != 0:
            highest_selling = array[i]
            highest_day = i

    maximum_profit = highest_selling - lowest_buying

    if maximum_profit > 0:
        return f"Your maximum profit is {maximum_profit}, you should buy on day {lowest_day} and sell on day {highest_day}"

    else:
        return f"There is no profit on this market :("
    

#I've used this tedious method to enter the array
#yet it ensures that all values are valid.
numbers = []

while True:
    n = input("Please enter a number to add to list, or press 'N' to continue: ")

    if n.upper() == "N": # Exit option for loop.
        break

    elif n.isdigit():
        numbers.append(int(n))

    else:
        print("Please enter a valid value.")

print(f"Original array: {numbers}")
print(Stock_pricing(numbers))
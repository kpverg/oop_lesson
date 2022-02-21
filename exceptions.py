"""try:
    print(8/1)
except ZeroDivisionError:
    print("devision with zero..") """

"""
while True:
    try:
        x = int(input("Please enter a number:"))
        break
    except ValueError:
        print("Not a number.Please try again")
print(x)"""


divident, divisor=eval(input("Please select two numbers to divide :"))

try:
    print(divident/divisor)
except ZeroDivisionError:
    print("You cannot devide with zero")

    

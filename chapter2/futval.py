# futval.py
#   A program to calculate the interest of an investement
#   carried 10 years in to the future.

def main():
    print("This program calculates the future value ")
    print("of an 10 year investement.")
    
    principal = eval(input("What is the principal of the investement? "))
    apr = eval(input("What is the anual interest rate? "))

    for i in range(10):
        principal = principal * (1+apr)

    print("The value in 10 years is: ", principal)

main()
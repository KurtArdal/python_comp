# futval.py
#   A program to calculate the interest of an investement
#   carried 10 years in to the future.

def main():
    print("This program calculates the future value ")
    print("of an investement.")
    
    principal = eval(input("What is the principal of the investement? "))
    apr = eval(input("What is the anual interest rate? "))
    years = eval(input("For how many years? "))

    for i in range(years):
        principal = principal * (1+apr)

    print("The value in", years, " years is: ", principal)

main()
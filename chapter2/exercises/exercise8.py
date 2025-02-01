# futval.py
#   A program to calculate the interest of an investement
#   carried 10 years in to the future.

def main():
    print("This program calculates the future value ")
    print("of an 10 year investement.")
    
    principal = eval(input("What is the principal of the investement? "))
    apr = eval(input("What is the anual interest rate? "))
    times_a_year = eval(input("How many times pr year? "))

    for i in range(10):
        principal = principal * (1+((apr/times_a_year) * times_a_year))

    print("The value in 10 years is: ", principal)

main()
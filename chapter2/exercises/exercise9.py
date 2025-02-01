# Convert.py
#   A program to convert Fahrenheit temps to Celsius
#

def main():
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = (fahrenheit - 32) / 9*5

    print("The temperature is", celsius, "degrees Celsius.")

main()
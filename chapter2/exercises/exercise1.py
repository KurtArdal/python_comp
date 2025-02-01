# Convert.py
#   A program to convert Celsius temps to Fahrenheit
#

def main():
    print("This program converts temperatures from Fahrenheit to Celsius.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperture is", fahrenheit, "degrees Fahrenheit.")

main()
# Convert.py
#   A program to convert Celsius temps to Fahrenheit
#

def main():
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperture is", fahrenheit, "degrees Fahrenheit.")

main()
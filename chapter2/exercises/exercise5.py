# Convert.py
#   A program to convert Celsius temps to Fahrenheit
#

def main():
    for i in range(0, 101, 10):
        celsius = i #eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperture is", fahrenheit, "degrees Fahrenheit, for", celsius, "degree Celsius.")

main()
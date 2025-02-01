# exercise12.py
#   A program to evaluate the input given and calculate it.
#   Program runs for 100 iteration, or to failure state.

def main():
    for i in range(100):
        print(eval(input("Please enter a your inputs: ")))

main()
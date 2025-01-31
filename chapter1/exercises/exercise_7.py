def main():
    print("This program illustrates a chaotic function.")
    x = eval(input("Enter a number between 0 and 1: "))
    y = eval(input("Enter a second number between 0 and 1: "))
    print(f"Input:\t{x}\t{y}")
    print("-"*30)
    for i in range(100):
        x = 3.9 * x * (1 - x)
        y = 3.9 * y * (1 - y)
        print(x, " ", y)

main()
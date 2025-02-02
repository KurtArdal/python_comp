# A program to calculate the cost per square inch of a circular pizza.

def main():
    diameter = int(input("What is the diameter of the pizza? "))
    prize = int(input("What is the prize of the pizza? "))
    radius = diameter / 2

    area = 3.14 * radius * radius

    cost = prize / area

    print("The cost per square inch is", cost)

main()
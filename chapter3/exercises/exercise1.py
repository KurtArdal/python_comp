# A program that calculate the volume and surface area of a sphere.

def main():
    radius = int(input("Please give the radius: "))
    volume = 0.75 * 3.14 * radius * radius * radius
    area = 4 * 3.14 * radius * radius

    print(volume)
    print(area)

main()

#!/usr/bin/python3
def circumference_circle(radius):
    """
    Calculate the circumference of a circle.

    Variables:
    radius: Radius of a circle.

    Returns:
    float: The circumference of circle.
    """
    pi = 3.14
    circumference = 2*pi*radius
    return circumference


def main():
    # Ask the user for radius(radius)
    radius = float(input("Enter the value of a radius of a circle: "))

    # Find the circumference of a circle
    circumference = circumference_circle(radius)

    # Show the circumference of a circle
    print(f"The circumference of a circle with radius {radius} is {circumference:.2f}")


if __name__ == "__main__":
    main()

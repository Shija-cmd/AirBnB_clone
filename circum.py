#!/usr/bin/python3
def circumference_circle(r):
    """
    Calculate the circumference of a circle.

    Variables:
    radius: Radius of a circle.

    Returns:
    float: The circumference of circle.
    """
    p = 3.14
    circumference = 2*p*r
    return circumference


def main():
    # Ask the user for radius(r)
    r = float(input("Enter the value of a radius (r) of a circle: "))

    # Find the circumference of a circle
    circumference = circumference_circle(r)

    # Show the circumference of a circle
    print(f"The circumference of a circle with radius {r} is {circumference:.2f}")


if __name__ == "__main__":
    main()

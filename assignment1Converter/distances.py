"""A module that provides functions related to distance conversions.

Functions:


    miles_to_kiloms(mi): 
        Returns mi miles in kilometres.

    kiloms_to_miles(km): 
        Returns km kilometres in miles.

    feet_to_metres(ft): 
        Returns ft feet in metres.

    metres_to_feet(m): 
        Returns m metres in feet.

    inches_to_centims(ins): 
        Returns ins inches in centimetres. 

    centims_to_inches(cm): 
        Returns cm centimetres in inches.

Author: Kai Ellis
Date: 2020-01-16
Section: 002
Student number: 20019803

"""


def miles_to_kiloms(mi):
    """Returns mi miles in kilometres."""
    return mi * 1.609


def kiloms_to_miles(km):
    """ Returns km kilometres in miles."""
    return km / 1.609


def feet_to_metres(ft):
    """Returns ft feet in metres."""
    return ft / 3.281


def metres_to_feet(m):
    """Returns m metres in feet."""
    return m * 3.281


def inches_to_centims(ins):
    """Returns ins inches in centimetres. """
    return ins * 2.54


def centims_to_inches(cm):
    """Returns cm centimetres in inches."""
    return cm / 2.54


if __name__ == "__main__":
    # Test code for module.
    print(miles_to_kiloms(0))  # 0
    print(kiloms_to_miles(0))  # 0
    print(feet_to_metres(0))  # 0
    print(metres_to_feet(0))  # 0
    print(inches_to_centims(0))  # 0
    print(centims_to_inches(0))  # 0
    print(miles_to_kiloms(2))  # 3.22
    print(kiloms_to_miles(4))  # 2.48
    print(feet_to_metres(6))  # 1.828
    print(metres_to_feet(8))  # 26.25
    print(inches_to_centims(10))  # 25.4
    print(centims_to_inches(12))  # 4.72

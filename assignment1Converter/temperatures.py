"""A module that provides functions related to temperature conversions.

Functions:

    cels_to_fahr(deg_c)
        Return deg_c degrees Celsius in degrees Fahrenheit.

    fahr_to_cels(deg_f)
        Return deg_f degrees Fahrenheit in degrees Celsius.
        
    cels_to_kelv(deg_c): 
        Return deg_c degrees Celsius in Kelvin.

    kelv_to_cels(kelv): 
        Return kelv Kelvin in degrees Celsius.

    fahr_to_kelv(deg_f): 
        Return deg_f degrees Fahrenheit in Kelvin.

    kelv_to_fahr(kelv): 
        Return kelv Kelvin in degrees Fahrenheit.


Author: R. Linley
Date: 2019-12-18

Modified by: Kai Ellis
Date: 2020-01-16
Section: 002
Student number: 20019803
"""


def cels_to_fahr(deg_c):
    """Return deg_c degrees Celsius in degrees Fahrenheit."""
    return (deg_c * 9.0 / 5.0) + 32


def cels_to_kelv(deg_c):
    """Return deg_c degrees Celsius in degrees Kelvin."""
    return deg_c + 273.15


def fahr_to_cels(deg_f):
    """Return deg_f degrees Fahrenheit in degrees Celsius."""
    return (deg_f - 32) * 5.0 / 9.0


def fahr_to_kelv(deg_f):
    """Return deg_f degrees Fahrenheit in degrees Kelvin."""
    return (deg_f - 32) * 5.0 / 9.0 + 273.15


def kelv_to_fahr(deg_k):
    """Return deg_k degrees Kelvin in degrees Fahrenheit."""
    return (deg_k - 273.15) * 9.0 / 5.0 + 32


def kelv_to_cels(deg_k):
    """Return deg_k degrees Fahrenheit in degrees Celsius."""
    return deg_k - 273.15


if __name__ == "__main__":
    # Test code for module.
    print("Base functions test:")
    print(cels_to_fahr(100))  # 212.0
    print(fahr_to_cels(212))  # 100.0
    print(cels_to_fahr(0))  # 32.0
    print(fahr_to_cels(32))  # 0
    print("Added functions test:")
    print(cels_to_kelv(0))  # 273.15
    print(fahr_to_kelv(0))  # 255.372
    print(kelv_to_cels(0))  # -273.15
    print(kelv_to_fahr(0))  # -459.67
    print(cels_to_kelv(25))  # 298.15
    print(fahr_to_kelv(50))  # 283.15
    print(kelv_to_cels(75))  # -198.15
    print(kelv_to_fahr(69))  # -335.47

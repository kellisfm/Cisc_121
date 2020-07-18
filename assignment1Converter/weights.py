"""A module that provides functions related to weight conversions.

Functions:

    tons_to_tonnes(t_us):
         Return t_us US tons in metric tonnes.

    tonnes_to_tons(t_m):
         Return t_m metric tonnes in US tons.

    pounds_to_kgrams(lb): 
        Return lb pounds in kilograms.

    kgrams_to_pounds(kg):
        Return kg kilograms in pounds.

    ounces_to_grams(oz): 
        Return oz ounces in grams.

    grams_to_ounces(g): 
        Return g grams in ounces.


Author: Kai Ellis
Date: 2020-01-16
Section: 002
Student number: 20019803

"""


def tons_to_tonnes(t_us):
    """Return t_us US tons in metric tonnes"""
    return t_us / 1.102


def tonnes_to_tons(t_m):
    """ Return t_m metric tonnes in US tons."""
    return t_m * 1.102


def pounds_to_kgrams(lb):
    """ Return lb pounds in kilograms."""
    return lb / 2.205


def kgrams_to_pounds(kg):
    """Return kg kilograms in pounds."""
    return kg * 2.205


def ounces_to_grams(oz):
    """ Return oz ounces in grams. """
    return oz * 28.35


def grams_to_ounces(g):
    """Return g grams in ounces."""
    return g / 28.35


if __name__ == "__main__":
    # Test code for module.
    print(tons_to_tonnes(0))  # 0
    print(tonnes_to_tons(0))  # 0
    print(pounds_to_kgrams(0))  # 0
    print(kgrams_to_pounds(0))  # 0
    print(ounces_to_grams(0))  # 0
    print(grams_to_ounces(0))  # 0
    print(tons_to_tonnes(2))  # 1.815
    print(tonnes_to_tons(4))  # 4.408
    print(pounds_to_kgrams(6))  # 2.72
    print(kgrams_to_pounds(8))  # 17.64
    print(ounces_to_grams(10))  # 283.495
    print(grams_to_ounces(12))  # 0.423


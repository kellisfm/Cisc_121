"""This program allows the user to perform conversions between
measurement systems for:

    temperatures
    distances
    weights

Author: R. Linley
Date: 2019-12-18

Modified by: Kai Ellis
Section: 002
Student number: 20019803
Date: 2020-01-16
"""

import menu
import get_int
import temperatures
import distances
import weights


def main():
    """Program execution starts here."""

    # Set up main menu and sub-menus.
    main_menu_choices = ["Temperatures", "Distances", "Weights"]

    temperatures_menu_choices = [
        "Celsius to Fahrenheit",  # 1
        "Fahrenheit to Celsius",  # 2
        "Farenheit to Kelvin",  # 3
        "Celsius to Kelvin",  # 4
        "Kelvin to Farenheit",  # 5
        "Kelvin to Celsius",  # 6
    ]

    distances_menu_choices = [
        "Miles to Kilometers",  # 1
        "Kilometres to Miles",  # 2
        "Feet to Metres",  # 3
        "Metres to Feet",  # 4
        "Inches to Centimetres",  # 5
        "Centimetres to Inches",  # 6
    ]

    weights_menu_choices = [
        "Tons to Tonnes",  # 1
        "Tonnes to Tons",  # 2
        "Pounds to Kilograms",  # 3
        "Kilograms to Pounds",  # 4
        "Ounces to Grams",  # 5
        "Grams to Ounces",  # 6
    ]

    # Loop until user wants to quit.
    while True:
        choice = menu.do_menu("Choose a conversion type:", main_menu_choices)
        # Did the user choose "Exit?"
        if choice is None:
            # Yes, then exit.
            break
        if choice == 1:  # User chose temperature conversions.
            # Loop until user wants to return to the main menu.
            while True:
                choice = menu.do_menu(
                    "Choose a temperature conversion", temperatures_menu_choices
                )
                if choice is None:
                    break
                if choice is 1:  # Celsius to Fahrenheit chosen.
                    cels = get_int.input_int("\nDegrees Celsius: ")
                    print(
                        (
                            f"\n{cels} degrees Celsius is: "
                            f"{temperatures.cels_to_fahr(cels):.1f} "
                            "degrees Fahrenheit."
                        )
                    )
                if choice is 2:  # Fahrenheit to Celsius chosen.
                    fahr = get_int.input_int("\nDegrees Fahrenheit: ")
                    print(
                        (
                            f"\n{fahr} degrees Fahrenheit is: "
                            f"{temperatures.fahr_to_cels(fahr):.1f} "
                            "degrees Celsius."
                        )
                    )
                if choice is 3:  # Farenheit to kelvin chosen
                    fahr = get_int.input_int("\nDegrees Farenheit: ")
                    print(
                        (
                            f"\n{fahr} degrees Fahrenheit is: "
                            f"{temperatures.fahr_to_kelv(fahr):.1f}"
                            " degrees Kelvin."
                        )
                    )
                if choice is 4:  # Celsius to Kelvin chosen
                    cels = get_int.input_int("\nDegrees Celsius: ")
                    print(
                        (
                            f"\n{cels} degrees Celsius is: "
                            f"{temperatures.cels_to_kelv(cels):.1f}"
                            " degrees Kelvin."
                        )
                    )
                if choice is 5:  # Kelvin to Farenheit chosen
                    kelv = get_int.input_int("\nDegrees Kelvin: ")
                    print(
                        (
                            f"\n{kelv} degrees Kelvin is: "
                            f"{temperatures.kelv_to_fahr(kelv):.1f}"
                            " degrees Farenheit."
                        )
                    )
                if choice is 6:  # Kelvin to Celsius chosen
                    kelv = get_int.input_int("\nDegrees Kelvin: ")
                    print(
                        (
                            f"\n{kelv} degrees Kelvin is: "
                            f"{temperatures.kelv_to_cels(kelv):.1f}"
                            " degrees Celsius."
                        )
                    )
        if choice == 2:  # User chose distance conversions.
            # Loop until user wants to return to the main menu.
            while True:
                choice = menu.do_menu(
                    "Choose a distance conversion", distances_menu_choices
                )
                if choice is None:
                    break
                if choice is 1:  # Miles to Kilometeres chosen.
                    miles = get_int.input_int("\nMiles: ")
                    print(
                        (
                            f"\n{miles} miles is: "
                            f"{distances.miles_to_kiloms(miles):.1f} "
                            " kilometers."
                        )
                    )
                if choice is 2:  # Kilometers to Miles chosen.
                    kiloms = get_int.input_int("\nKilometers: ")
                    print(
                        (
                            f"\n{kiloms} kilometers is: "
                            f"{distances.kiloms_to_miles(kiloms):.1f} "
                            " miles."
                        )
                    )
                if choice is 3:  # Feet to meters chosen
                    feet = get_int.input_int("\nFeet: ")
                    print(
                        (
                            f"\n{feet} feet is: "
                            f"{distances.feet_to_metres(feet):.1f}"
                            " meters."
                        )
                    )
                if choice is 4:  # Meters to feet chosen
                    metres = get_int.input_int("\nMeters: ")
                    print(
                        (
                            f"\n{metres} meters is: "
                            f"{distances.metres_to_feet(metres):.1f}"
                            " feet."
                        )
                    )
                if choice is 5:  # Inches to centimeters chosen
                    inches = get_int.input_int("\nInches: ")
                    print(
                        (
                            f"\n{inches} inches is: "
                            f"{distances.inches_to_centims(inches):.1f}"
                            " centimeters."
                        )
                    )
                if choice is 6:  # Centimeters to inches chosen
                    centims = get_int.input_int("\nCentimeters: ")
                    print(
                        (
                            f"\n{centims} centimeters is: "
                            f"{distances.centims_to_inches(centims):.1f}"
                            " Inches"
                        )
                    )
        if choice == 3:  # User chose weight conversions.
            # Loop until user wants to return to the main menu.
            while True:
                choice = menu.do_menu(
                    "Choose a weight conversion", weights_menu_choices
                )
                if choice is None:
                    break
                if choice is 1:  # tons to tonnes.
                    tons = get_int.input_int("\nTons: ")
                    print(
                        (
                            f"\n{tons} tons is: "
                            f"{weights.tons_to_tonnes(tons):.1f} "
                            " tonnes."
                        )
                    )
                if choice is 2:  # Tonnes to tons chosen
                    tonnes = get_int.input_int("\nTonnes: ")
                    print(
                        (
                            f"\n{tonnes} Tonnes is: "
                            f"{weights.tonnes_to_tons(tonnes):.1f} "
                            " tons."
                        )
                    )
                if choice is 3:  # Pounds to kilograms chosen
                    pounds = get_int.input_int("\nPounds: ")
                    print(
                        (
                            f"\n{pounds} pounds is: "
                            f"{weights.pounds_to_kgrams(pounds):.1f}"
                            " kilograms."
                        )
                    )
                if choice is 4:  # Meters to feet chosen
                    kgrams = get_int.input_int("\nKilograms: ")
                    print(
                        (
                            f"\n{kgrams} kilograms is: "
                            f"{weights.kgrams_to_pounds(kgrams):.1f}"
                            " pounds."
                        )
                    )
                if choice is 5:  # Ounces to grams chosen
                    ounces = get_int.input_int("\nOunces: ")
                    print(
                        (
                            f"\n{ounces} ounces is: "
                            f"{weights.ounces_to_grams(ounces):.1f}"
                            " grams."
                        )
                    )
                if choice is 6:  # Centimeters to inches chosen
                    grams = get_int.input_int("\nGrams: ")
                    print(
                        (
                            f"\n{grams} grams is: "
                            f"{weights.grams_to_ounces(grams):.1f}"
                            " ounces."
                        )
                    )


"""
"""

main()

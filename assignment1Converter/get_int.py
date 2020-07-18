"""This module provides functions to control input for numbers.

Functions:

    input_int(prompt, minimum_value=None)
        Return an integer entered by the user in response to prompt.

Author: R. Linley
Date: 2019-12-18
"""


def input_int(prompt, minimum_value=None):
    """Return an integer as entered by the user in response to the
    printed prompt.  Repeat as necessary until the user enters an
    integer.

    Parameters:
    
        prompt: Message to the user suggesting the type of input.

        minimum_value (optional, default None): If not None, an
        integer specifying the lowest acceptable input value.

    Returns:
    
        An integer provided by the user.
    """
    # Repeat as necessary until valid user input received.
    while True:
        try:
            # Put prompt on the screen and get the user's (string) input.
            # A ValueError is triggered if the string cannot be
            # converted to a number.
            user_input_float = float(input(prompt))
            # Now make sure user_input is an integer.
            user_input_int = int(user_input_float)
            # If it's not, the user entered some non-integer float,
            # so raise an exception to resolve the ambiguity.
            if user_input_int != user_input_float:
                raise ValueError
            # If a minimum value has been specified, then reject any
            # lower value by raising an exception.
            if minimum_value is not None:
                if user_input_int < minimum_value:
                    raise ValueError
            # If execution gets this far, all is well. Return the user's
            # input as an integer value.
            return user_input_int  # Breaks out of the input loop.
        except ValueError:
            # Any non-integer input causes execution to come here.
            if minimum_value is not None:
                print(
                    (
                        f"You must enter an integer value of {minimum_value} "
                        "or greater. Try again."
                    )
                )
            else:
                print("You must enter an integer value. Try again.")


if __name__ == "__main__":
    # Test code for module.

    # Testing input_int() with default minimum_value (None)
    print("Test 1 (no minimum value specified):")
    while True:
        i = input_int("Enter an integer: ")
        if isinstance(i, int):  # Is i an integer?
            print(f"input_int() worked. {i} returned.")
        else:
            print("input_int() failed.")
        if input("Run again (y/n): ")[0] in ["N", "n"]:
            break
    # Testing input_int() with a minimum_value
    print("\nTest 2 (minimum value set at 1):")
    while True:
        i = input_int("Enter an integer greater than 0: ", 1)
        if isinstance(i, int):  # Is i an integer?
            print(f"input_int() worked. {i} returned.")
        else:
            print("input_int() failed.")
        if input("Run again (y/n): ")[0] in ["N", "n"]:
            break


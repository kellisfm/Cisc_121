"""This is the menu module.

Functions:

    do_menu(title, choices)
        Print a text menu, return an int representing the user's choice.

Author: R. Linley
Date: 2019-01-06
Revised: 2019-12-18
"""


def do_menu(title, choices):
    """Display a text menu of choices and return the user's choice.
    Loop on invalid choices.

    All but the last choice are customizeable and are numbered 1, 2, and
    so on.  The last choice is always "X. Exit."  For example:

        My Menu

        1. Do something
        2. Do something else
        3. Do some other thing

        X. Exit

        Your choice: 

    Parameters:

        title: A str representing a title for the menu.  (In the example
        above, "My Menu" is the value of title.)

        choices: A list of strings representing the menu choices,
        excluding "Exit".  These are presented in order of occurrence in
        the list.  As menu item numbers are generated automatically,
        these should not appear in the list.  (In the example above, the
        list ["Do something", "Do something else",
        "Do some other thing"] is the value of choices.)

    Returned value:

        An integer representing the user's choice if the user selects a
        numbered choice, or None if the user selects "x" or "X" to exit.    
    """
    num_choices = len(choices)
    # Make a list of the valid choice numbers.
    valid_choices = list(range(1, num_choices + 1))
    while True:  # Loop until the user makes a valid choice.
        title_border = "*" * (len(title) + 4)
        # print menu title with asterisks border
        print(f"\n{title_border}\n* {title} *\n{title_border}\n")
        # print numbered choices
        for choice_num in valid_choices:
            print(f"{choice_num}. {choices[choice_num-1]}")
        print("\nX. Exit\n")
        choice = input("Your choice: ")
        try:
            choice = int(choice)  # Non-int input throws a ValueError.
            if choice in valid_choices:
                return choice
        except ValueError:  # Execution branches here on non-int input.
            pass  # Take no action on non-int input.
        if choice in ["x", "X"]:  # If so...
            return None  # Done here. The user wants out.
        # Still here? User made an invalid choice, so...
        print("\nInvalid choice.")
        print("Valid choices: ", end="")
        if num_choices > 0:
            print(f"{', '.join(str(i) for i in valid_choices)} and ", end="")
        print("X (to exit).\nTry again.")


if __name__ == "__main__":
    # If this module is being executed directly, and not by means of an
    # import, then this code will execute. Otherwise, it won't.
    """Test function for module."""
    # Test with an empty title, empty menu (just to make sure it
    # won't break).
    while True:
        c = do_menu("", [])
        if c is None:
            break
        else:
            # Since there are no choices, execution should
            # never be able to get here.
            print(f"Problem: a choice of {c} was returned from an empty menu.")

    # Test with a single item menu.
    m = ["Only choice"]
    while True:
        c = do_menu("Testing!", m)
        if c is None: 
            break
        else:
            print(f"\nYou chose {c}.")

    # Test with multiple menu items.
    m = ["This", "That", "The other thing"]
    while True:
        c = do_menu("test Menu", m)
        if c is None:
            break
        print("\nYou chose:", c)

    print("\nTests complete.")

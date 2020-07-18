import web_scraper
import parse_logons
import dict_quad_sorts
import dict_bin_search
import long_list_printer
import menu


def main():
    """Program execution starts here."""
    url = "http://sites.cs.queensu.ca/courses/cisc121/a2/logons.txt"
    data = web_scraper.scrape(url)
    n = len(data)
    data = parse_logons.logons_to_list_of_dicts(data)
    # The data list (and the file it came from) are in chronological
    # order. That means data is currently sorted by timestamp.
    sort_on_key = "timestamp"

    main_menu_title = "Select an operation:"
    main_menu_choices = [
        "Sort logons data", "Show a selection of the data",
        f"Search for a particular {sort_on_key}"
    ]

    sort_on_menu_title = "Select a key to sort on:"
    sort_on_menu_choices = list(data[0].keys())

    sort_menu_title = "Select a sort algorithm:"
    sort_menu_choices = [
        "Insertion sort", "Bubble sort", "Bubble sort (optimized)",
        "Selection sort"
    ]

    while True:
        choice = menu.do_menu(main_menu_title, main_menu_choices)
        if choice is None:
            return  # Exit main() (and program).
        if choice == 1:  # Sort logons data.
            while True:
                sort_on_choice = menu.do_menu(sort_on_menu_title,
                                              sort_on_menu_choices)

                if sort_on_choice is None:
                    break  # Return to main menu.
                sort_on_key = sort_on_menu_choices[sort_on_choice - 1]
                # Change last choice in main menu to reflect the new
                # sort_on_choice.
                main_menu_choices[
                    -1] = f"Search for a particular {sort_on_key}"

                sort_choice = menu.do_menu(sort_menu_title, sort_menu_choices)
                if sort_choice is None:
                    break  # Return to main menu.

                # If we're here, we can proceed with a sort.
                print()
                if sort_choice == 1:  # Insertion sort
                    sort_function = dict_quad_sorts.insertion_sort
                elif sort_choice == 2:  # Bubble sort
                    sort_function = dict_quad_sorts.bubble_sort
                elif sort_choice == 3:  # Bubble sort (opt)
                    sort_function = dict_quad_sorts.bubble_sort_opt
                else:  # Selection sort
                    sort_function = dict_quad_sorts.selection_sort

                # Do the sort.
                print(f"Sorting on key '{sort_on_key}'...")
                sort_function(data, sort_on_key)
                print("Done.")

                # Show it worked.
                long_list_printer.print_list(data, 5)

        elif choice == 2:  # Show a selection of the data.
            long_list_printer.print_list(data, 10)

        elif choice == 3:  # Search for a specific value.
            search_val = input(f"\nSearch for what {sort_on_key}? ")
            found_at = dict_bin_search.search(data, sort_on_key, search_val)
            if found_at is None:
                print(f"{sort_on_key} {search_val} not found.")
            else:
                print(f"{sort_on_key} {search_val} found at position "\
                      f"{found_at}.")


main()

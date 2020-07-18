"""Solution to CISC 121 Assignment 2. A program that gives the student
programmer a lot of practice at things like loop-writing, file input and
output, and manipulating lists and dictionaries.

The data used by the is program real, but anonymized. It is a record of
users logging on to PCs on a campus computer network.

Original author: R. Linley
Date: 2020-01-21
Modified by: Kai Ellis
Date: 2020-01-16
Section: 002
Student number: 20019803
"""
import web_scraper
import json_writer
import dict_maker


def month_word_to_number(m_word):
    # Returns a month's numeric position in the gregorian calander with information from its first three letters
    month = {
        "jan": "01",
        "feb": "02",
        "mar": "03",
        "apr": "04",
        "may": " 05",
        "jun": "06",
        "jul": "07",
        "aug": "08",
        "sep": "09",
        "oct": "10",
        "nov": "11",
        "dec": "12",
    }
    first_three = m_word.strip()[:3].lower()

    try:
        out = month[first_three]
        return out
    except:
        print(f"{m_word} is not a month in the gregorian calander.")


def format_datetime(raw_datetime):
    # This function splits a datetime string into blocks based on the location of spaces,
    # then replaces months with their corresponding number using of the month_word_to_number function.
    # Adds missing 0s in cases where there are single numbers e.g. 9 -> 09,
    # before concatenating the strings into the requested format of yyyy-mm-dd hh:mm:ss.

    split_datetime = raw_datetime.split()
    split_datetime[1] = month_word_to_number(split_datetime[1])
    for i in range(len(split_datetime)):

        if len(split_datetime[i]) == 1:
            split_datetime[i] = "0" + split_datetime[i]
        if len(split_datetime[i]) == 7:
            split_datetime[i] = "0" + split_datetime[i]

    return (
        split_datetime[5]
        + "-"
        + split_datetime[1]
        + "-"
        + split_datetime[2]
        + " "
        + split_datetime[3]
    )


def line_to_list(file_str):
    # This function breaks apart the given string at the semicolons to give a list
    # before formating the 4th element with the format_datetime function
    l = file_str.split(" ; ")
    l[3] = format_datetime(l[3])
    return l


def main():
    # Program execution starts here.
    url = "http://sites.cs.queensu.ca/courses/cisc121/a2/logons.txt"
    print(f"Retrieving data from {url}.")
    data = web_scraper.scrape(url)
    n = len(data)
    print(f"{n} records read.")

    # This loop converts the data from a list of strings to a list of lists.
    for i in range(n):
        data[i] = line_to_list(data[i])

    # CSV file creation
    # This code first opens a file with the requested name,
    # then joins all values in each interior array with commas and
    # makes a newline between each array, writing the result into the csv.
    csv_filename = "logons.csv"
    csv_file = open(f"{csv_filename}", "w")
    for i in data:
        csv_file.write(",".join([str(x) for x in i]) + "\n")
    csv_file.close()

    # JSON file creation
    # Note: Once your dict_make.make_dict() function is working,
    # this code will create a JSON file for you.  You don't need
    # to do anything in this section.
    json_filename = "logons.json"
    dict_keys = ["user_id", "os", "pc_id", "datetime"]
    dict_list = []
    for i in range(n):
        dict_list.append(dict_maker.make_dict(dict_keys, data[i]))
    if json_writer.write_json_file(json_filename, dict_list):
        print(f"Write to {json_filename} complete.")
    else:
        print(f"Write to {json_filename} failed.")

    while True:
        # This code checks all entries in data for the input PC id,
        # if it finds a match, it checks if the operating system is Linux.
        # In cases where both conditions are met, adds 1 to the Linux login count,
        # and prints the count after the whole list has been checked.
        print("Checking the number of Linux logons for a specific PC.")
        pc_id = input("Enter the PC's ID number or just press Enter to quit: ")
        logon_count = 0
        if pc_id == "":
            break
        for i in range(n):
            if data[i][2] == pc_id:
                if data[i][1] == "Linux":
                    logon_count = logon_count + 1
        print(f"PC {pc_id} was logged onto in Linux {logon_count} times.")
    print("Done.")


main()

"""This is a solution to part of CISC 121 Winter 2020 Assignment 5.

Functions:
    print_file_listing(file_listing, indent="")
    Format and print file_listing, a dictionary representing the
    description of a disk file.

    Parameters:

        file_listing:  a dictionary with keys "name", "timestamp",
            "type" and "size".  The "type" value (always "file") is
            omitted from the printed output.

        indent (optional):  a string of spaces representing the
            level at which the file is nested in the folder
            structure.
    print_folder(folder, indent=""):

    Format and print folder, a dictionary representing a file
    system.

    Parameters:

        folder:  a dictionary with keys "name", "timestamp", "type" and
            "files".  "files" is a list of zero or more files and
            folders.  The "type" value (always "dir") is omitted from
            the printed output.

        indent (optional):  a string of spaces representing the
            level at which the folder is nested in the file system.
Author: K. Ellis
SN: 20019803
Section: 002
Date: 2020-04-01
"""
import json_reader


def print_file_listing(file_listing, indent=""):
    """Format and print file_listing, a dictionary representing the
    description of a disk file.

    Parameters:

        file_listing:  a dictionary with keys "name", "timestamp",
            "type" and "size".  The "type" value (always "file") is
            omitted from the printed output.

        indent (optional):  a string of spaces representing the
            level at which the file is nested in the folder
            structure.
    """
    print(f"{indent}{file_listing['name']:<12} "\
          f"{file_listing['timestamp']} "\
          f"{file_listing['size']:>8}")


indent = ""


def print_folder(folder, indent=""):
    """Format and print folder, a dictionary representing a file
    system.

    Parameters:

        folder:  a dictionary with keys "name", "timestamp", "type" and
            "files".  "files" is a list of zero or more files and
            folders.  The "type" value (always "dir") is omitted from
            the printed output.

        indent (optional):  a string of spaces representing the
            level at which the folder is nested in the file system.
    """
    print(f"{indent}{folder['name']:<12} {folder['timestamp']}")
    # Add your code below this line.
    indent = indent + "\t"
    if folder['type'] == 'dir':
        for i in range(len(folder['files'])):
            if folder['files'][i]['type'] == 'dir':
                print_folder(folder['files'][i], indent)
            if folder['files'][i]['type'] == 'file':
                print_file_listing(folder['files'][i], indent)


def main():

    root = json_reader.read_json("dir_tree_1.json")
    print_folder(root)


main()

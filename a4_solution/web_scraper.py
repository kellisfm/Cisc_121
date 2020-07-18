"""This module facilitates the extraction of text from a web page into a
list of strings (an operation known as scraping).

Function:

    scrape(url): Return a list of strings scraped from web page url.

Author: R. Linley
Date: 2020-01-20
"""
import urllib.request


def scrape(url):
    """Return a list of strings scraped from web page url."""
    # See https://stackoverflow.com/questions/24153519/how-to-read-html-from-a-url-in-python-3
    reader = urllib.request.urlopen(url)
    raw_data = reader.read()
    data_rows = raw_data.decode("utf-8").split("\n")
    # Trim off any empty rows.
    while data_rows[-1] == "":
        del data_rows[-1]
    # Get rid of any nuisance carriage return ("\r") characters.
    for i in range(len(data_rows)):
        data_rows[i] = data_rows[i].replace("\r", "")
    return data_rows


if __name__ == "__main__":
    # Test code for module.
    url = "http://sites.cs.queensu.ca/courses/cisc121/a2/logons.txt"
    data = scrape(url)
    len_data = len(data)
    print(f"{len_data} lines retrieved from\n\t{url}")
    if len_data > 0:
        print(f"First {min(10, len_data)} lines:")
        for i in range(min(10, len_data)):
            print(data[i])

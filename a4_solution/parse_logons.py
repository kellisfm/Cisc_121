"""Module for parsing computer lab logon data as found at
    http://sites.cs.queensu.ca/courses/cisc121/a2/logons.txt
into a two-dimensional list.

Functions:

    parse_datetime(raw_datetime): Return a date-and-time string of the
        form yyyy-MM-dd HH:mm:ss with information from string
        raw_datetime, a date and time string as found in logons.txt.

    parse_logons_line(raw_str): Return a list of strings of data items
        extracted from raw_str, a string read from logons.txt.

    logons_to_2d_list(raw_list): Return a two-dimensional list of
        strings of data extracted from raw_list, a list of strings
        extracted from logons.txt.

    logons_to_list_of_dicts(raw_list): Return a list of dictionaries
        of data items extracted from raw_list, a list of strings
        extracted from logons.txt.


Author: R. Linley
Date: 2020-02-14
"""
import dict_maker


def parse_datetime(raw_datetime):
    """Return a date-and-time string of the form yyyy-MM-dd HH:mm:ss
    with information from string raw_datetime, a date and time string
    as found in logons.txt.
    """
    # Note: No imported modules required. A dict definition and six
    # lines of code (not counting comments) and we're done.
    mnths = {
        "Jan": "01",
        "Feb": "02",
        "Mar": "03",
        "Apr": "04",
        "May": "05",
        "Jun": "06",
        "Jul": "07",
        "Aug": "08",
        "Sep": "09",
        "Oct": "10",
        "Nov": "11",
        "Dec": "12"
        }
    parts = raw_datetime.split(" ")
    # parts now contains the following as strings:
    #   a day name abbreviation (not used) at index 0,
    #   a month name abbreviation at index 1,
    #   a day number at index 2,
    #   a time in h:mm:ss form at index 3,
    #   a time zone (not used) at index 4, and
    #   a four-digit year at index 5.
    day = ("0" + parts[2])[-2:]  # Left-pad single digit day with "0".
    month = mnths[parts[1]]  # Convert month abbreviation to number.
    time = ("0" + parts[3])[-8:]  # Left-pad single digit hour with "0".
    year = parts[5]
    return f"{year}-{month}-{day} {time}"


def parse_logons_line(raw_str):
    """Return a list of strings of data items extracted from raw_str, a
    string read from logons.txt.
    """
    parts = raw_str.split(" ; ")
    # parts now contains the following as strings:
    #   a student ID at index 0,
    #   an operating system (one of "Windows" or "Linux") at index 1,
    #   a machine id at index 2,
    #   a date and time at index 3.
    datetime = parse_datetime(parts[3])
    return [parts[0], parts[1], parts[2], datetime]


def logons_to_2d_list(raw_list):
    """Return a two-dimensional list of strings of data extracted from
    raw_list, a list of strings extracted from logons.txt.
    """
    ret_list = []
    for row in raw_list:
        ret_list.append(parse_logons_line(row))
    return ret_list


def logons_to_list_of_dicts(raw_list):
    """Return a list of dictionaries of data extracted from raw_list, a
    list of strings extracted from logons.txt.
    """
    ret_list = []
    dict_keys = ["user_id", "os", "pc_id", "timestamp"]
    for row in raw_list:
        ret_list.append(dict_maker.make_dict(dict_keys, \
                                             parse_logons_line(row)))
    return ret_list


if __name__ == "__main__":
    # Module testing.

    # Testing function
    # parse_datetime()

    # Test with single-digit day and hour.
    print(parse_datetime("Wed Sep 5 9:18:08 EDT 2018"))
    # 2018-09-05 09:18:08

    # Test with single-digit day, two-digit hour.
    print(parse_datetime("Wed Sep 5 12:18:08 EDT 2018"))
    # 2018-09-05 12:18:08

    # Test with two-digit day, single-digit hour.
    print(parse_datetime("Wed Sep 25 9:18:08 EDT 2018"))
    # 2018-09-25 09:18:08

    # Test with different months.
    print(parse_datetime("Wed Jan 5 9:18:08 EDT 2018"))
    # 2018-01-05 09:18:08
    print(parse_datetime("Wed Dec 5 9:18:08 EDT 2018"))
    # 2018-12-05 09:18:08

    # Testing function
    # parse_logons_line()

    # Test with Windows entry:
    print(parse_logons_line("26423740 ; Windows ; 192 ; "\
                         "Thu Sep 6 15:57:49 EDT 2018"))
    # ['26423740', 'Windows', '192', '2018-09-06 15:57:49']

    # Test with Linux entry:
    print(parse_logons_line("25566141 ; Linux ; 187 ; Wed "\
                            "Sep 5 13:41:49 EDT 2018"))
    # ['25566141', 'Linux', '187', '2018-09-05 13:41:49']

    # Testing function
    # logons_to_2d_list()

    # Test with some data copied from 
    # "http://sites.cs.queensu.ca/courses/cisc121/a2/logons.txt"
    data = [
        "26223857 ; Windows ; 183 ; Wed Sep 5 9:18:08 EDT 2018",
        "25175295 ; Windows ; 183 ; Wed Sep 5 9:22:49 EDT 2018",
        "25917378 ; Windows ; 182 ; Wed Sep 5 9:23:03 EDT 2018",
        "25554845 ; Windows ; 184 ; Wed Sep 5 10:09:24 EDT 2018",
        "25566141 ; Linux ; 187 ; Wed Sep 5 13:41:49 EDT 2018",
        "26423740 ; Windows ; 188 ; Wed Sep 5 16:11:16 EDT 2018",
        "26423740 ; Windows ; 192 ; Thu Sep 6 15:48:05 EDT 2018",
        "26423740 ; Windows ; 192 ; Thu Sep 6 15:57:49 EDT 2018",
        "25591503 ; Windows ; 181 ; Thu Sep 6 15:58:45 EDT 2018",
        "26448303 ; Windows ; 182 ; Thu Sep 6 15:59:42 EDT 2018",
        "25251783 ; Windows ; 186 ; Fri Sep 7 14:12:44 EDT 2018",
        "25786222 ; Linux ; 187 ; Fri Sep 7 15:31:30 EDT 2018",
        "26544150 ; Windows ; 198 ; Sat Sep 8 11:39:36 EDT 2018",
        "25752214 ; Windows ; 197 ; Sat Sep 8 13:29:05 EDT 2018"
        ]

    # Try to parse it into a 2d list.
    data_2d = logons_to_2d_list(data)

    # data_2d and data should have the same lengths.
    print(len(data) == len(data_2d))  # True

    # Check the first, middle, and last items in both lists to make
    # sure they correspond with each other.

    print(data[0])
    print(data_2d[0])
    print(data[len(data) // 2])
    print(data_2d[len(data_2d) // 2])
    print(data[-1])
    print(data_2d[-1])

    # Testing function
    # logons_to_list_of_dicts()

    # Try to parse data into a list of dicts.
    data_list_of_dicts = logons_to_list_of_dicts(data)

    # data_2d and data should have the same lengths.
    print(len(data) == len(data_list_of_dicts))  # True

    # Check the first, middle, and last items in both lists to make
    # sure they correspond with each other.

    print(data[0])
    print(data_list_of_dicts[0])
    print(data[len(data) // 2])
    print(data_list_of_dicts[len(data_list_of_dicts) // 2])
    print(data[-1])
    print(data_list_of_dicts[-1])

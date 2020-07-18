"""Module to enable searching of user defined values for a user defined key in a list of dictionaries. 
Function:
    search(a_list_dict, key, v): Returns the position of value v in sequence a_list_dict if v is
    in a_list_dict, else returns none
    

Academic integrety note: code was taken from course slides and modidified to correctly function on 
lists of dicts
Author: Kai Ellis
Section: 002
Student number: 20019803
Date: 2020-03-03


"""


def search(a_list_dict, key, v):
    """Returns the position of value v in sequence a_list_dict if v is
    in a_list_dict, else returns none
    """
    low = 0
    high = len(a_list_dict) - 1
    while low <= high:
        mid = (low + high) // 2
        if v == a_list_dict[mid][f"{key}"]:
            return mid
        if v < a_list_dict[mid][f"{key}"]:
            high = mid - 1
        else:
            low = mid + 1
    return None


if __name__ == "__main__":

    tstlistdict = []
    tstlistdict.append({'fs': 'a', 'fi': 1, 'ff': 1.1})
    tstlistdict.append({'fs': 'b', 'fi': 2, 'ff': 2.2})
    tstlistdict.append({'fs': 'c', 'fi': 3, 'ff': 3.3})
    tstlistdict.append({'fs': 'd', 'fi': 4, 'ff': 3.3})

    t = search(tstlistdict, "ff", 15)  #none
    print(t)
    t = search(tstlistdict, "fs", "b")  #1
    print(t)
    t = search(tstlistdict, "fi", 1)  # 0
    print(t)
    t = search(tstlistdict, "ff", 3.3)  #2
    print(t)

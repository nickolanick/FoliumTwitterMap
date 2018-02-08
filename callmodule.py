from parser import read_file
from placement import layer_placement, map_placement


def inp_data():
    """
    None -->None


    inputs the year of the films
    and the data limit
    Then calls of of the modules and creates a Map With all Films
    you asked
    """
    year = input("Enter the year of films : ")
    data_lim = input("Enter the number of films to see  positive integer > then 5: ")

    try:

        data_lim = int(data_lim)
        year = int(year)
        assert (data_lim > 5)
    except ValueError:
        print("Limit must be an positive integer > then 5: ")
        exit()
    except AssertionError:
        print("Limit must be an positive integer > then 5")
        exit()
    layer_placement(map_placement(read_file("locations.list", year), data_lim))


inp_data()

from collections import defaultdict


def read_file(path, year):
    """
    (file) -- > dict


    reads file and return dictionary with film name as
    a key and locations of this film as a value
    """
    dic_all_films = defaultdict(set)
    with open(path, 'r', encoding='utf-8', errors="ignore") as file_to_read:
        line = file_to_read.readline()
        while line != "==============\n":
            line = file_to_read.readline()
        for i in str(file_to_read.read()).split("\n"):
            line_split = i.split("\t")
            if "(" + str(year) in line_split[0]:
                line_normal = line_split[0]

                if "(" in line_split[-1]:
                    index_call = -2
                else:
                    index_call = -1
                dic_all_films[line_split[index_call]].add(line_normal)
    return dic_all_films
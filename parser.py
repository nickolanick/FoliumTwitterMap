from collections import defaultdict
def read_file(path,year):
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
            try:
                if "(" + str(year) in line_split[0]:
                    if "{" in line_split[0]:
                        line_normal = i[0:i.index("{")]
                    else:
                        line_normal = line_split[0]

                    if dic_all_films.get(line_normal, False):
                        if "(" in line_split[-1]:

                            dic_all_films[line_normal].add(line_split[-2])
                        else:

                            dic_all_films[line_normal].add(line_split[-1])

                    else:
                        if "(" in line_split[-1]:

                            dic_all_films[line_normal] = {line_split[-2]}
                        else:

                            dic_all_films[line_normal] = {line_split[-1]}

            except UnicodeEncodeError:
                continue
        return dic_all_films


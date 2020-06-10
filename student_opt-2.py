import random

"""
A short script to divide students into groups, while maintaining average scores of each group within a particular range.
"""

def import_students(fp):
    """
    Import students from file
    @param fp: File path
    @return: Dictionary of students
    """
    students = {}
    with open(fp) as st_file:
        lines = st_file.readlines()
        _id = 0
        for l in lines:
            data = l.replace('\n', '').split(",")
            students[_id] = (data[0], data[1], float(data[2]))  # Name, email, grade
            _id += 1

    return students


def evaluate_group(group, s_dict):
    """
    Calculates the average score of a group of students
    """
    _sum = 0
    for i in group:
        _sum += s_dict[i][2]

    return _sum / len(group)


def evaluate_all(groups, s_dict):
    avgs = []
    for group in groups:
        avgs.append(evaluate_group(group, s_dict))
    return avgs


def shuffle_groups(s_dict, min_size):
    lst = list(range(0, len(s_dict)))
    random.shuffle(lst)
    groups = []
    start_i = 0

    while start_i + min_size < len(lst) - 1:
        end_i = start_i + min_size
        groups.append(lst[start_i:end_i])
        start_i = end_i

    leftover = lst[start_i:]

    g_list = list(range(0, len(groups) - 1))
    random.shuffle(g_list)
    count = 0
    for l in leftover:
        groups[g_list[count]].append(l)
        count += 1

    return groups


def print_group(s_dict, groups):
    counter = 0
    teamNames = ['Deportivo La Coruña', 'Benfica', 'Porto', 'Córdoba', 'Athletic Bilbao', 'Sevilla', 'Valencia']
    print('===================================================')
    for g in groups:
        print("===== Average score: {} =====".format(evaluate_group(g, s_dict)))
        for s in g:
            print("{},{}@student.bham.ac.uk,{},{}".format(s_dict[s][0], s_dict[s][1], teamNames[counter],
                                                                 s_dict[s][2]))  # Name, username, grade
        counter += 1
    print('===================================================')


def var(lst):
    x_bar = sum(lst) / len(lst)
    total = 0
    for n in lst:
        total += (n - x_bar) ** 2

    return total / len(lst)


def main():
    file_path = "students.csv"

    students = import_students(file_path)
    min_group_size = 4

    groups = shuffle_groups(students, min_group_size)
    while var(evaluate_all(groups, students)) ** 0.5 > 0.7:
        groups = shuffle_groups(students, min_group_size)
        print("Variance: {}".format(evaluate_all(groups, students)))

    print_group(students, groups)


if __name__ == "__main__":
    main()

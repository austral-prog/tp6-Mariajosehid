def remove_elements(lst):
    new_list = lst[:]
    for i in sorted([0, 4, 5], reverse=True):
        if i < len(new_list):
            new_list.pop(i)
    return new_list


def add_elements(lst):
    new_list = ['Pink'] + lst + ['Yellow']
    return new_list


def is_empty(lst):
    return len(lst) == 0


def check_lists(lst1, lst2):
    if len(lst1) >= 3 and len(lst2) >= 3:
        return lst1[2] == lst2[2]
    return False


def list_of_lists(big_list):
    new_list = []
    if len(big_list) >= 1:
        new_list.append(big_list[0][:2])
    if len(big_list) >= 2:
        new_list.append(big_list[1][1:4])
    if len(big_list) >= 3:
        new_list.append(big_list[2][-2:])
    return new_list

def print_reversed_list_integer(my_list=[]):
    if not my_list:
        return None
    my_list.reverse()
    for a in my_list:
        print("{:d}".format(a))

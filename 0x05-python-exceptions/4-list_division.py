#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    number = 0
    a = 0
    num_list = []
    for a in range(list_length):
        try:
            p = my_list_1[a] / my_list_2[a]
        except TypeError:
            print("wrong type")
            p = 0
        except ZeroDivisionError:
            print("division by 0")
            p = 0
        except IndexError:
            print("out of range")
            p = 0
        finally:
            num_list.append(p)
    return num_list

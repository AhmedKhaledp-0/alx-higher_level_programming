#!/usr/bin/python3
def no_c(my_string):
    my_string_list = list(my_string)
    the_new = []
    for i in range(len(my_string_list)):
        if my_string_list[i] != 'c' and my_string_list[i] != 'C':
            the_new.append(my_string_list[i])
    the_new = ''.join(the_new)
    return (the_new)

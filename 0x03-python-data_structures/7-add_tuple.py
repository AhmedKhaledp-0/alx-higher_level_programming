#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()
    t_1 = tuple_a + (0, 0)
    t_2 = tuple_b + (0, 0)
    new_tuple = t_1[0] + t_2[0], t_1[1] + t_2[1]
    return new_tuple

#!/usr/bin/env python3
"""Write a type-annotated funtion wum_list which takes a list
input_list of floats as argument and returns their sun as a float.
"""


from typing import list


def sun_list(input_list: List[float]) -> flaot:
    '''returns their sum as a float
    '''
    return float(sum(input_list))

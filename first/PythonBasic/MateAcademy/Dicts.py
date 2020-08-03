"""
1. Sum Values
Write a function named sum_values that takes a dictionary named my_dictionary as a parameter.
The function should return the sum of the values of the dictionary
"""
from typing import Dict


def sum_values(my_dictionary):
    return sum(my_dictionary.values())


# print(sum_values({"milk": 5, "eggs": 2, "flour": 3}))


"""
2. EvenKeys
Create a function called sum_even_keys that takes a dictionary named my_dictionary, with all integer keys and values, 
as a parameter. This function should return the sum of the values of all even keys.
"""


def sum_even_keys(my_dictionary: Dict[int, int]):
    new_dictionary = {k: v for k, v in my_dictionary.items() if k % 2 == 0}
    return sum(new_dictionary.values())


# print(sum_even_keys({1:5, 2:2, 3:3}))


"""
3. Add Ten
Create a function named add_ten that takes a dictionary with integer values named my_dictionary as a parameter. 
The function should add 10 to every value in my_dictionary and return my_dictionary
"""


def add_ten(my_dictionary: Dict[int, int]):
    new_dictionary = dict()
    for k, v in my_dictionary.items():
        new_dictionary[k] = v+10
    return new_dictionary


# print(add_ten({1:5, 2:2, 3:3}))


"""
4. Values That Are Keys
Create a function named values_that_are_keys that takes a dictionary named my_dictionary as a parameter. 
This function should return a list of all values in the dictionary that are also keys.
"""


def values_that_are_keys(my_dictionary):
    return set(my_dictionary.keys()).intersection(my_dictionary.values())


# print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))


"""
5. Largest 
Write a function named max_key that takes a dictionary named my_dictionary as a parameter. 
The function should return the key associated with the largest value in the dictionary.
"""


def max_key(my_dictionary):
    v = list(my_dictionary.values())
    k = list(my_dictionary.keys())
    index_max = v.index(max(v))
    return k[index_max]


print(max_key({1:100, 2:1, 3:4, 4:10}))
# should print 1
print(max_key({"a":100, "b":10, "c":1000}))
# should print "c"
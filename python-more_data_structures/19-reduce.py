#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):

    ages = []
    salaries = []

    for key, value in a_dictionary.items():
        if key == "age":
            ages.append(value)
        elif key == "salary":
            salaries.append(value)

    total_age = reduce(lambda x, y: x + y, ages)
    total_salary = reduce(lambda x, y: x + y, salaries)

    average_age = total_age / len(ages)
    average_salary = total_salary / len(salaries)

    return average_salary, average_age

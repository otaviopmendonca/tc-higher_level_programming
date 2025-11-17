#!/usr/bin/python3
from functools import reduce
def calc_average(a_dictionary):
    ages = [a_dictionary[key] for key in a_dictionary if key == 'age']
    salaries = [a_dictionary[key] for key in a_dictionary if key == 'salary']

    total_age = reduce(lambda x, y: x + y, ages)
    total_salary = reduce(lambda x, y: x + y, salaries)

    average_age = total_age / len(ages)
    average_salary = total_salary / len(salaries)
    return average_salary, average_age

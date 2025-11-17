#!/usr/bin/python3
def filtering_data(employees):
    employes_hs = filter(lambda emp: emp['salary'] > 10000, employees)

    names = map(lambda emp: emp['name'], employes_hs)

    return list(names)

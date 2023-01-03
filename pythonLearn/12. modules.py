"""Logically organize your python code
Module should contain related code """

import helperForModules
#  or from helperForModules import validate, user input messages
#  or from helperForModules import *

data = ""
while data != "exit":
    data = input("Hey user, enter a number of days and conversion unit\n ")
    # easy to convert list to sets use set() method
    daysAndUnit = data.split(":")
    print(daysAndUnit)
    dict = {"days":daysAndUnit[0], "units":daysAndUnit[1]}
    helperForModules.validate(dict)
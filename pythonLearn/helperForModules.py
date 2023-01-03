# another built-in data type of python
# as with lists, used to store multiple items of data
# does not allow duplicate values


# validate user input
def func(numberOfDays, conversion_unit):
    if (conversion_unit == "hours"):
        return f"{numberOfDays} days are {numberOfDays * 24} {conversion_unit}"
    elif conversion_unit == "minutes":
        return f"{numberOfDays} days are {numberOfDays * 24 * 60} {conversion_unit}"
    else:
        return "unsupported unit"




def validate(dict):
    try:
        casting = int(dict["days"])
        if casting > 0:
            convertedValue = func(casting, dict["units"])
            # type_check = convertedValue
            # print(type(type_check))
            print(convertedValue)
        elif casting == 0:
            print("you enter a 0, enter a valid positive number")
        else:
            print("you enetered a negative number")
    except ValueError:
        print("your input is not a integer number")




# dict = {"days":20, "unit":hours}
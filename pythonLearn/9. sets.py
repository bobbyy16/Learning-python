# another built-in data type of python
# as with lists, used to store multiple items of data
# does not allow duplicate values


# validate user input
def func(numberOfDays):
    return f"{numberOfDays} days are {numberOfDays * 24} hours"


def validate():
    try:
        casting = int(num_of_days)
        if casting > 0:
            convertedValue = func(casting)
            # type_check = convertedValue
            # print(type(type_check))
            print(convertedValue)
        elif casting == 0:
            print("you enter a 0, enter a valid positive number")
        else:
            print("you enetered a negative number")
    except ValueError:
        print("your input is not a integer number")


data = ""
while data != "exit":
    data = input("Hey user, enter a number of days and I will convert it to hours\n ")
    # easy to convert list to sets use set() method
    for num_of_days in set(data.split(", ")):
        validate()

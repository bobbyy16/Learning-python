
# validate user input
def func(numberOfDays):
    # print(numberOfDays > 0)
    if numberOfDays > 0:
        return f"{numberOfDays} days are {numberOfDays * 24} hours"
    elif numberOfDays == 0:
        return "you enter a 0, enter a valid positive number"
    else:
        return "you entered negative number"

def validate():
    if data.isdigit():
        casting = int(data)
        convertedValue = func(casting)
        # type_check = convertedValue
        # print(type(type_check))
        print(convertedValue)
    else:
        print("your input is not a number")


data = input("Hey user, enter a number of days and I will convert it to hours\n ")
validate()

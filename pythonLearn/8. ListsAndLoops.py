
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
            print ("you enter a 0, enter a valid positive number")
        else:
            print("you enetered a negative number")
    except ValueError:
        print("your input is not a integer number")

data = ""
while data != "exit":
    data = input("Hey user, enter a number of days and I will convert it to hours\n ")
    for num_of_days in data.split(", "):
        validate()
 
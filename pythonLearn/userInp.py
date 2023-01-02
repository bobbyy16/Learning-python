def fun(numberOfDays):
    return f"{numberOfDays} days are {numberOfDays * 24} hours"

data = int(input("Hey user, enter a number of days and I will convert it to hours\n "))
convertedValue = fun(data)
print(convertedValue)
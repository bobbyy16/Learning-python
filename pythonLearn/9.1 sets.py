sets = {"January", "Febraury", "March"}

# sets are unordered and unchangeable
#     Items in a set do not have a defined order
#     Items cannot be reffered to by index
#     Items cannot be changed, only added/removed

for ele in sets:
    print(ele)

sets.add("April")
print(sets)

sets.remove("April")
print(sets)
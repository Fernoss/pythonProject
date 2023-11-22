# testing out set()
my_set = {"January", "February", "March"}
print(my_set)

# items in a set do not have a defined order like list
# items cannot be referred to by index
# items cannot be changed, only added/removed
# we can use loop to go through items

for element in my_set:
    print(element)

# to add
my_set.add("April")
print(my_set)

# to remove
my_set.remove("March")
print(my_set)
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1  # list3 refers to the same object as list1

print(list1 == list2)  # True, because they have the same values
print(list1 is list2)  # False, because they are different objects in memory
print(list1 is list3)  # True, because list3 refers to list1

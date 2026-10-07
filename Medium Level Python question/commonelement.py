list1 = [10, 20, 30, 40, 50, 60]
list2 = [30, 40, 50, 70, 80, 90]

#Convert lists to sets
set1 = set(list1)
set2 = set(list2)

#common values
common = set1.intersection(set2)

#Only in list1
only_list1 = set1.difference(set2)

only_list2 = set2.difference(set1)
print("Values present in both lists:", sorted(common))
print("Values only in list1:", sorted(only_list1))
print("Values only in list2:", sorted(only_list2))
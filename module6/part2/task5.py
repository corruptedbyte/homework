# I originally thought to use list.extend but it didn't work for some reason
def mergeLists(listOne, listTwo):
    return listOne + listTwo

list1 = ["Hello"]
list2 = ["World"]

merged = mergeLists(list1, list2)

print(merged)
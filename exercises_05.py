def find_common_element(list1, list2):
    return list(set(list1) & set(list2))

list1 = [int(input("Enter integer for list 1: "))]
list2 = [int(input("Enter integer for list 2: "))]

common_elements = find_common_element(list1, list2)

print("List 1: ", list1)
print("List 2: ", list2)
print("Common Elements without duplication: ", common_elements)
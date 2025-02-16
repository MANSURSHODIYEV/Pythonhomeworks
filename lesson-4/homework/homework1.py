def uncommon_elements(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return list(set1 ^ set2)
    
list1 = [1, 3, 5, 2, 4]
list2 = [1, 4, 7, 9, 5]
print(uncommon_elements(list1, list2))


      
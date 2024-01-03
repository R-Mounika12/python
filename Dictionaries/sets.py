set1 = {1,2,3,4,5}
set1.add(6)
print(set1)
set1.remove(2)
print(set1)

set2 = {4,5,6,7,8,9}

print("union : ", set1.union(set2))
print("intersection :", set1.intersection(set2))
print("difference : ", set1.difference(set2))

set3 = {4,5,6}

print("is_subset : ", set3.issubset(set1))
print("is_subset : ", set1.issubset(set3))
print("is_subset : ", set1.issuperset(set3))
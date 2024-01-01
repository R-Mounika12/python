# A list is a fundamental data structure in programming 
#that allows you to store a collection of items. 
#Lists are ordered and can contain elements of various data types, 
#such as numbers, strings, and objects.
# list are mutable
# Lists generally consume more memory than tuples because they need to store additional
# information to support their mutability.

studentList = ["rahul", "Rakshith", "Pravalika", "Ambika"]
commonList = [1, 2, 3, 6.0, "Rakshith", "Pravalika"]

print(studentList)
print(commonList)
print("type : ", type(studentList))
print("type : ", type(commonList))
print("first element in the list : ", studentList[0])
print("length of the commonList : ", len(commonList))
print("appending the element to the list : ", commonList.append(8))
print("commonList after appending : ", commonList)
print("removing the element from the list : ", commonList.remove(3))
print("commonList after removing : ", commonList)
print("subset from the list : ", commonList[1:4])

#concatinating the list
commonList = commonList + [10, 11]
print("list after concatination : ", commonList)

# sorting
studentList.sort()
print("sorted list : ", studentList)

if 10 in commonList :
    print(" 10 is present in the commonList")

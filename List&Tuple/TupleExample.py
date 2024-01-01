# memory management for tuple is better than list
#A tuple is a data structure similar to a list, but unlike lists, tuples are immutable, 
#meaning their contents cannot be changed after creation. 
#Tuples are typically used for grouping related data.

studentTuple = ("rahul", "Rakshith", "Pravalika", "Ambika")

print("student tuple : ", studentTuple)
print("type : ", type(studentTuple))
print("length of the tuple : ", len(studentTuple))
#print("5th ele : ", studentTuple[5])

for item in studentTuple :
    print(item)

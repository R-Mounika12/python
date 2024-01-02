
numList = [1, 2,3,4,5]

# break --> breaks the loop execution

for num in numList :
    if num == 3 :
        break
    print("break")
    print(num) # prints 1, 2

# continue --> skips the loop execution when the condition is met
for num in numList :
    if num == 3 :
        continue
    print("continue")
    print(num) # prints 1,2,4,5

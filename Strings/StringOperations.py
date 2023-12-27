## Concat Opertaion
str1 = "hello"
str2 = "world"

str3 = str1 + " "+str2
print(str3)

## length of the String
print("length of the String: ", len(str3))

## to uppercase
print("upper ", str3.upper())

## to lower case
print("upper ", str3.lower())

## string replacement
print("replacement ", str3.replace("world", "python"))

## split
print("split ", str3.split())

## strip
text = " abc "
print("stripped text ", text.strip())

## substring
str4 = "world"
if str4 in str3 :
    print(str4, " found in str3")
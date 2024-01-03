#A dictionary in Python is a data structure that allows you to store and retrieve values using keys. 
#It is also known as a hashmap or associative array in other programming languages.

emp_dict = {"name":"John", "age":"34", "company":"abb"}
print(emp_dict)
print(emp_dict["name"])

for key, value in emp_dict.items():
    print(key, value)

students_info = [
    {"name": "Jessica","age":"23","city":"newyork"},
    {"name": "John","age":"25","city":"chicago"}
]
for student in students_info:
    print(student["name"]+ " "+student["age"]+" "+student["city"])

print(students_info[0]["name"])

for student in students_info:
    del student["city"]
    print(student["name"]+ " "+student["age"])
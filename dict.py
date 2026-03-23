# student = {"Amit": 85, "Riya": 90, "John": 78}

# # print all students name
# print(student.keys())

# print(student.values())

# # add new students
# student["Sara"]=92
# student["Amit"]=67
# # delete 
# del student["John"]
# print(student)



text = "banana"
freq={}
for char in text:
    if char in freq:
        freq[char]+=1
    else:
        freq[char] = 1
print(freq) 



# sentence="hi sakshi here i am bored" 
# words = sentence.split()

# freq = {}

# for word in words:
#     if word in freq:
#         freq[word] += 1
#     else:
#         freq[word] = 1

# print(freq) 



# # merge two dict
# d1 ={"a":1, "b":2}
# d2 ={"x":0 , "y":4}
# d1.update(d2)
# print(d1)



# marks = {"Amit": 85, "Riya": 90, "John": 78}
# max_student = max(marks, key=marks.get)
# print(f"Top student: {max_student} with marks: {marks[max_student]}")



# iterating using values
# student={ 
#     "name":"sakshi",
#     "age": 23,
#     "marks":87
# }
# for value in student.values():
#  print(value)




# student.update({
#     "age": 23,
#     "marks": 95
# })

# print(student)

# student = {
#     "name": "Sam",
#     "age": 21,
#     "marks": 85
# }

# for key in student:
#     if key == "marks":
#         student[key] = student[key] + 5

# print(student)

# '''Create a dictionary of your biodata.
# Add a new key "salary" in dictionary.
# Update "age" value.
# Delete "city" key.
# Loop and print all keys and values.
# Create a nested dictionary for 3 students.
# Count how many keys dictionary has.
# Check if key "name" exists.
# Merge two dictionaries.
# Convert two lists to a dictionary.'''

# 1) Create biodata
biodata = {
    "name": "Vilas Paradkar",
    "age": 25,
    "city": "Pune",
    "role": "Software Engineer",
    "skills": ["Python", "FastAPI", "SQL"]
}
print("Biodata:", biodata)

# 2) Add salary
biodata["salary"] = 650000
print("After adding salary:", biodata)

# 3) Update age
biodata["age"] = 26
print("After updating age:", biodata)

# 4) Delete city
del biodata["city"]
print("After deleting city:", biodata)

# 5) Loop keys & values
print("---- Looping keys and values ----")
for key, value in biodata.items():
    print(f"{key}: {value}")

# 6) Nested dictionary for 3 students
students = {
    "s1": {"name": "harsh", "age": 26, "marks": {"math": 88, "cs": 92}},
    "s2": {"name": "Sakshi", "age": 22, "marks": {"math": 91, "cs": 89}},
    "s3": {"name": "A", "age": 27, "marks": {"math": 85, "cs": 90}},
}
print("Students:", students)
print("Sakshi CS:", students["s2"]["marks"]["cs"])

# 7) Count keys
print("Number of keys in biodata:", len(biodata))
print("Number of students:", len(students))

# 8) Check key existence
print("Does 'name' exist in biodata?", "name" in biodata)
print("Does 'salary' exist in biodata?", "salary" in biodata)

# 9) Merge two dicts
d1 = {"a": 1, "b": 2}
d2 = {"b": 20, "c": 3}
merged = d1 | d2
print("Merged (|):", merged)

d3 = {"x": 10, "y": 20}
d4 = {"y": 200, "z": 30}
d3_copy = d3.copy()
d3_copy.update(d4)
print("Merged (update):", d3_copy)

# 10) Convert two lists to dict
keys = ["name", "age", "city"]
values = ["Vilas", 26, "Pune"]
converted = dict(zip(keys, values))
print("Converted dict:", converted)


# use of popitem() removes last item from dict and returns it as tuple

dict = {"a": 1, "b": 2, "c": 3}
print("before popitem:", dict)
removed= dict.popitem()
print("after popitem:", dict)


# Print Harsh’s CS marks.
# Print Adya’s Math marks.
# Print Shrey’s age.
print("harsh cs marks" , students["s1"]["marks"]["cs"])
print("adya math marks" , students["s1"]["marks"]["math"])
print("shrey age" , students["s3"]["age"])

#  add  values city to all students
for student in students.values():
    student["city"]="pune"
    print(student)

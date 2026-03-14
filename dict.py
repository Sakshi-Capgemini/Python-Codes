student = {"Amit": 85, "Riya": 90, "John": 78}

# # print all students name
# print(student.keys())

# print(student.values())

# # add new students
# student["Sara"]=92
# student["Amit"]=67
# # delete 
# del student["John"]
# print(student)



# text = "banana"
# freq={}
# for char in text:
#     if char in freq:
#         freq[char]+=1
#     else:
#         freq[char] = 1
# print(freq) 
# 


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

student = {
    "name": "Sam",
    "age": 21,
    "marks": 85
}

for key in student:
    if key == "marks":
        student[key] = student[key] + 5

print(student)




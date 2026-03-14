# # String operations demonstration
# name = "  python developer  "

# clean_name = name.strip().title()

# print("Original:", name)
# print("Cleaned:", clean_name)
# print("Length:", len(clean_name))
# print("Contains 'Python':", "Python" in clean_name)

# text = "Python programming"

# print(text.startswith("Python"))
# print(text.endswith("programming"))

# text = "Python"

# print(text.upper())
# print(text.lower())

# print("123".isdigit())
# print("Python".isalpha())
# print("Python123".isalnum())



# # string interpolation
# name = "Rahul"
# age = 25

# print(f"My name is {name} and I am {age} years old.")

# without string interpolation using concat
# name = "Rahul"
# age = 25

# text = "My name is " + name + " and I am " + str(age) + " years old."
# print(text)
# # Need to convert numbers using str()(NOTE)

# # interpolation with calculation
# a=12
# b=34
# print(f"sum is {a + b}")


#  Accessing list or dict
person = {"name":"sakshi" , "age":"23"}
print(f"Name:{person['name']}, Age:{person['age']}")
 
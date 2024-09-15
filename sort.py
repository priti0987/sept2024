num = [31,2,4,6,7,8,9,45]
print(sorted(num,reverse=True))

#sorting dictionary

people = [
    {"name":"priti","age":42},
    {"name": "priya", "age": 40},
    {"name": "bhavika", "age": 20},
    {"name": "pratap", "age": 10}
]

print(sorted(people,key=lambda person : person["age"]))
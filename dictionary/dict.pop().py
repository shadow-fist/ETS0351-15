person = {"name": "Alex", "age": 25}

age = person.pop("age")
print(age)     #the output is going to be 25
print(person)  #the output is going to be {'name': 'Alex'}

job = person.pop("job", "Not specified")
print(job)  # 
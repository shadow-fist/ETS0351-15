person = {"name": "Alex", "age": 25, "job": "Dev"}

last_item = person.popitem()
print(last_item)  # since it is the last inserted pair the out put will be ('job', 'Dev')
print(person)     # {'name': 'Alex', 'age': 25}
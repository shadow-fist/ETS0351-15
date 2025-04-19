user = {"name": "Alex", "age": 25}
user_copy = user.copy()

print(user_copy)         # {'name': 'Alex', 'age': 25'}
print(user_copy is user) # False (different objects)
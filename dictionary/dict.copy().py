user = {"name": "Alex", "age": 25}
user_copy = user.copy()

print(user_copy)          # the output is going to be {'name': 'Alex', 'age': 25'}
print(user_copy is user)  # the output is going to beFalse (different objects)
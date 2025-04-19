user = {"name": "Alex", "age": 25}

print(user.get("name"))       # the output is going to be Alex
print(user.get("job"))        # the output is going to be  None 
print(user.get("job", "N/A")) #the output is going to be N/A
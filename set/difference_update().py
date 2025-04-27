x = {1, 2, 3, 4, 5}
y = {2, 3}
z = {4, 6}

x.difference_update(y, z)
print(x)  # without the elements in y and z our output will be {1, 5}

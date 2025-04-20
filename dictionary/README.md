dict.clear()
This method removes all key-value pairs from the dictionary, leaving it completely empty.

dict.copy()
This method returns a shallow copy of the dictionary.

dict.fromkeys()
Creates a new dictionary with keys from an iterable and sets all values to the same specified value (defaults to None if not given).

dict.get(key, default)
Returns the value for the specified key if the key is in the dictionary. If not, it returns the default value instead of throwing an error.

dict.items()
Returns a view object that displays a list of a dictionary's (key, value) tuple pairs.

dict.pop(key[, default])
Removes the specified key from the dictionary and returns its value.
If the key is not found and a default is provided, it returns the default.
If the key is not found and no default is given it's going to desplay KeyError.

dict.setdefault(key[, default])
If the key exists, returns its value.
If the key doesn’t exist, adds it to the dict with the given default value (default is None), and returns that.

dict.popitem()
Removes and returns the last inserted (key, value) pair from the dictionary as a tuple.
Acts like a stack (LIFO: Last-In, First-Out).
If the dict is empty, you'll get a KeyError.

dict.update([other])
This method adds key-value pairs from another dictionary or iterable to the current dictionary.
If the key already exists, its value will be overwritten.

dict.values()
Returns a view object containing all the values in the dictionary. It reflects changes made to the dictionary.
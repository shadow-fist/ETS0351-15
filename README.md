String methods

 str.upper() is a built-in Python string method that returns a new string where all lowercase alphabetic characters are converted to uppercase. Non-alphabetic characters remain unchanged.
 
str.lower() is a built-in string method that converts all uppercase letters in a string to lowercase. It does not modify the original string but returns a new one with all characters converted to lowercase

str.title() is a built-in string method that converts the first letter of every word to uppercase while making the rest of the letters lowercase. This is useful for formatting text into title case (like headings or names).

str.swapcase() – returns a new string where all uppercase letters are converted to lowercase, and all lowercase letters are converted to uppercase.

str.find() - is a built-in string method that is used to Finds the first occurrence of sub and returns its index. Returns -1 if not found

str.index() - Just like find(),it is used to Finds the first occurrence of sub and returns its index. but it raises an error if sub is not found

str.startswith() is a built-in Python method used to check if a string starts with a specified prefix. It returns True if the string starts with the given prefix; otherwise, it returns False.

str.endswith() is a built-in Python method that checks whether a string ends with a specified suffix. It returns True if the string ends with the given suffix; otherwise, it returns False.

str.count() is a built-in Python method that counts the number of times a substring appears in a given string

str.replace()
The .replace(old, new, count) method replaces occurrences of a substring with another substring.
old: The substring to be replaced.
new: The substring to replace with.
count (optional): Number of times to replace (default: all occurrences).

str.strip()
The .strip() method removes leading and trailing whitespace (or specified characters) from a string.

str.lstrip()
The .lstrip() method removes leading whitespace (or specified characters) from the left side of a string.

str.rstrip()
str.rstrip() method removes trailing whitespace (or specified characters) from the right side of a string.

str.split()
The .split() method splits a string into a list of substrings based on a specified delimiter. By default, it splits on whitespace.

str.join()
The .join() method joins elements of an iterable (like a list) into a single string using a specified separator.

str.isalpha()
This method checks if all characters in the string are alphabetic (letters) and there are no numbers or special characters.
If the string contains only letters, it returns True; otherwise, it returns False.

str.isalnum()
This method returns True if all characters in the string are alphanumeric (i.e., only letters and numbers).
If the string contains spaces, symbols, or is empty, it returns False.

isdigit()  is an example of string methods used in python and it Checks if the string consists of only digits or not. Its output is boolean

str.isspace()
This method returns True if the string only contains whitespace characters (spaces, tabs, newlines).
If the string has any non-space characters, it returns False.








































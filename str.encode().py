text = "Hello, world!"
encoded_text = text.encode()  # Default UTF-8 encoding
print(encoded_text) 
 # Output: b'Hello, world!'

# Encoding with a different format
encoded_utf16 = text.encode("utf-16")
print(encoded_utf16)  
# Output: b'\xff\xfeH\x00e\x00l\x00l\x00o\x00,\x00 \x00w\x00o\x00r\x00l\x00d\x00!\x00'

# Handling errors
text = "Héllo"
  # Ignores characters not in ASCII
print(text.encode("ascii", errors="ignore"))  
# Output: b'Hllo'
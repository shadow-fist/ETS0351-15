settings = {"theme": "dark"}

value = settings.setdefault("theme", "light")
print(value)        # this will print 'dark' since it's the original value
print(settings)     # {'theme': 'dark'}


volume = settings.setdefault("volume", 75)  # since it doesn't exist in the original line it will add it
print(volume)       # our output will be 75
print(settings)     # {'theme': 'dark', 'volume': 75}
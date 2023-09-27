words = "HELLO world THESE are WORDS"
print(words.lower())
print(words.upper())
print(words.isdigit())

locworld = words.find("world")
print(locworld)

print(words[::-1])
print("Palindrome?", words == words[::-1])
print(words.split(' '))
print("Hi" * 5)
message = "One of Python's strengths is its diverse community."
print(message)
name = "Eric"

print(f"Hello {name}, would you like to learn some Python today?")
print(f"{name.lower()}{name.title()}{name.upper()}")

famous_person = "Albert Einstein"
message = f'{famous_person} once said, "A person who never made a mistake never tried anything new."'
print('Albert Einstein once said, "A person who never made a mistake never tried anything new."')
print(message)


new_name = "\tHans \nWurst    "
print(new_name)
print(new_name.lstrip())
print(new_name.rstrip())
print(new_name.strip())

file = "filename.txt"
print(file.removesuffix(".txt"))

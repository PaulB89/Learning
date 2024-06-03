


first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!"

print(full_name)

print(f"Hello, {full_name.title()}!")

print(message) 

print("\tPython")
print("Languages:\nPython\nC\nJavaScript")
print("Languages:\n\tPython\n\tC\n\tJavaScript")

favorite_language = 'python xD      '
print(f"{favorite_language.rstrip()}")
print(favorite_language)

favorite_language = favorite_language.rstrip()

print(favorite_language)

nostarch_url = 'https://nostarch.com'
print(f"{nostarch_url.removeprefix('nostarch.com')}")
print(f"{nostarch_url.removeprefix('https://')}")
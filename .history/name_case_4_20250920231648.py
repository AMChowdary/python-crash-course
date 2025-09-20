
famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
print(f'{famous_person} once said, "{quote}"')
message = f'{famous_person} once said, "{quote}"'
print(message)
# Store a person’s name in a variable, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name_with_whitespace = "\tEric\n"
print(name_with_whitespace)
print(name_with_whitespace.lstrip())
print(name_with_whitespace.rstrip())
print(name_with_whitespace.strip())
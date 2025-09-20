# Store a person’s name in a variable, and print a message to that person. Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”
name = "Eric"
print(f"Hello {name}, would you like to learn some Python today?")
# Store a person’s name in a variable, and then print that person’s name in lowercase, uppercase, and titlecase.
print(name.lower())
print(name.upper())
print(name.title())
# Find a quote from a famous person you admire. Print the quote and the name of its author. Your output should look something like the following, including the quotation marks: Albert Einstein once said, “A person who never made a mistake never tried anything new.”
famous_person = "Albert Einstein"
quote = "A person who never made a mistake never tried anything new."
print(f'{famous_person} once said, "{quote}"')
# store the famous person’s name in a variable called famous_person. Then compose your message and store it in a new variable called message. Print your message.
message = f'{famous_person} once said, "{quote}"'
print(message)
# Store a person’s name in a variable, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once. Print the name once, so the whitespace around the name is displayed. Then print the name using each of the three stripping functions, lstrip(), rstrip(), and strip().
name_with_whitespace = "\tEric\n"
print(name_with_whitespace)
print(name_with_whitespace.lstrip())
print(name_with_whitespace.rstrip())
print(name_with_whitespace.strip())
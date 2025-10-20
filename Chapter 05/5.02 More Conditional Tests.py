# Have at least one True and one False result for each of the following:

# Tests for equality and inequality with strings
string1 = "hello"
string2 = "world"
print("Is string1 == 'hello'? I predict True.")
print(string1 == 'hello')
print("\nIs string1 == 'world'? I predict False.")
print(string1 == 'world')

# Tests using the lower() function
print("\nIs string1.lower() == 'hello'? I predict True.")
print(string1.lower() == 'hello')
print("\nIs string1.lower() == 'HELLO'? I predict False.")
print(string1.lower() == 'HELLO')

# Numerical tests involving equality and inequality
num1 = 10
num2 = 20
print("\nIs num1 == 10? I predict True.")
print(num1 == 10)
print("\nIs num1 != 10? I predict False.")
print(num1 != 10)
print("\nIs num1 < num2? I predict True.")
print(num1 < num2)
print("\nIs num1 > num2? I predict False.")
print(num1 > num2)
print("\nIs num1 <= 10? I predict True.")
print(num1 <= 10)
print("\nIs num1 >= 10? I predict True.")
print(num1 >= 10)

# Tests using the and keyword and the or keyword
print("\nIs (num1 < num2 and string1 == 'hello')? I predict True.")
print(num1 < num2 and string1 == 'hello')
print("\nIs (num1 > num2 or string1 == 'hello')? I predict True.")
print(num1 > num2 or string1 == 'hello')

# Test whether an item is in a list
fruits = ['apple', 'banana', 'cherry']
print("\nIs 'banana' in fruits? I predict True.")
print('banana' in fruits)
print("\nIs 'orange' in fruits? I predict False.")
print('orange' in fruits)

# Test whether an item is not in a list
print("\nIs 'orange' not in fruits? I predict True.")
print('orange' not in fruits)
print("\nIs 'banana' not in fruits? I predict False.")
print('banana' not in fruits)
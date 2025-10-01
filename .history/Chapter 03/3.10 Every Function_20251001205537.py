# Think of something you could store in a list. For example,
# you could make a list of mountains, rivers, countries, cities, languages, or anything else you’d like. Write a program that creates a list containing these items
# and then uses each function introduced in this chapter at least once.
items = ['Python', 'JavaScript', 'C++', 'Java', 'Ruby']
print("Original list:", items)
# Using append() to add an item to the end of the list
items.append('Go')
print("After append:", items)
# Using insert() to add an item at a specific position
items.insert(2, 'Swift')
print("After insert:", items)
# Using del to remove an item by index

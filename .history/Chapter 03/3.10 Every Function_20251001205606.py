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
del items[3]
print("After del:", items)
# Using pop() to remove the last item and return it
popped_item = items.pop()
print("After pop:", items)
print("Popped item:", popped_item)
# Using remove() to remove an item by value
items.remove('Java')
print("After remove:", items)
# Using sort() to sort the list permanently
items.sort()
print("After sort:", items)
# Using sorted() to sort the list temporarily
print("Using sorted():", sorted(items))
# Using reverse() to reverse the order of the list
items.reverse()
print("After reverse:", items)
# Using len() to get the number of items in the list
print("Number of items in the list:", len(items))

# A buffet-style restaurant offers only five basic foods. Think of five simple foods, and store them in a tuple.
# •	 Use a for loop to print each food the restaurant offers.
# •	 Try to modify one of the items, and make sure that Python rejects the change.
# •	 The restaurant changes its menu, replacing two of the items with different foods. Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.

buffet = ('pizza', 'pasta', 'salad', 'sushi', 'tacos')
for food in buffet:
    print(food)

# Trying to modify an item
# buffet[0] = 'burger'  # This will raise a TypeError

# Changing the menu
buffet = ('burger', 'fries', 'shake', 'sushi', 'tacos')
for food in buffet:
    print(food)
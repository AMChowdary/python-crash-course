# # Start with your program from Exercise 4-1. Make a copy of the list of pizzas, and call it friend_pizzas.
# Then, do the following:
# •	 Add a new pizza to the original list.
# •	 Add a different pizza to the list friend_pizzas.
# •	 Prove that you have two separate lists. Print the message, My favorite
# pizzas are:, and then use a for loop to print the first list. Print the message,
# My friend’s favorite pizzas are:, and then use a for loop to print the second list. Make sure each new pizza is stored in the appropriate list.
pizzas = ['margherita', 'pepperoni', 'bbq chicken']
friend_pizzas = pizzas[:]  # Make a copy of the original list
# Add a new pizza to the original list
pizzas.append('hawaiian')
# Add a different pizza to the friend_pizzas list
friend_pizzas.append('veggie supreme')
# Prove that you have two separate lists
print("My favorite pizzas are:")
for pizza in pizzas:
    print(f"- {pizza}")
print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
    print(f"- {pizza}")
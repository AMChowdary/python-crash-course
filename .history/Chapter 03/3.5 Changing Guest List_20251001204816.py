# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# •	 Start with your program from Exercise 3-4. Add a print statement at the
# end of your program stating the name of the guest who can’t make it.
# •	 Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# •	 Print a second set of invitation messages, one for each person who is still
# in your list.
guest_list = ['Alice', 'Bob', 'Charlie']
print("Initial invitations:")
for guest in guest_list:
    print(f"Dear {guest}, you are invited to dinner.")
# Guest who can't make it
unable_to_attend = guest_list[1]
print(f"\nUnfortunately, {unable_to_attend} can't make it to the dinner.")
# Replace with a new guest

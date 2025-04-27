 add() 
It adds a single element to a set.
If the element isn’t already in the set, it gets added.
If it’s already there — nothing happens (no error, no duplicate).

remove() 
remove(element) deletes a specific item from a set.
But — if the item doesn’t exist, it throws a KeyError.

discard() 
discard(element) removes an element if it exists — and if it doesn’t, it just shrugs and moves on.

pop() 
pop() removes and returns a random element from a set.
(Well, it feels random — technically it removes some arbitrary element because sets are unordered.)

union()
union() returns a new set with all elements from both sets (no duplicates).

intersection()
Returns a new set with only elements common to both sets

difference()
It returns a new set containing elements that are in the first set but not in the second.

symmetric_difference()
It returns a new set with all the elements that are in either set, but not in both.

update() Does:
update() adds elements from another iterable (like a list, set, tuple) into the current set.
It’s like union() — but it modifies the original set instead of returning a new one.

intersection_update() is the set equivalent of Keep only the items that appear in all the sets you're comparing.

difference_update()
It removes all elements from the original set that are also present in another set (or sets).

symmetric_difference_update()
It updates the original set to keep only elements that are in either one set OR the other, but NOT in both.

issubset()
issubset() checks if all elements of one set are contained inside another set.

issuperset()
issuperset() checks if all elements of another set are inside the current set.

isdisjoint()
isdisjoint() checks if two sets have NO elements in common.
Returns True if the sets are completely different (no shared elements).
Returns False if they have even one thing in common.

clear()
clear() removes all elements from the set.
After calling it, your set becomes empty: {}.
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


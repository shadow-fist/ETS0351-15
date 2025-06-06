appendex()
Adds an element x to the end of the list.
It modifies the original list in-place.
Only one element can be appended at a time.

extend(iterable)
Adds each element from an iterable (like a list, tuple, set) to the end of the list.
It expands the list instead of nesting the iterable.
Modifies the original list in-place

insert(i, x)
Inserts the element x at index i.
Shifts everything after that index to the right.
Doesn't replace anything — it just slides things over.

remove(x)
Removes the first occurrence of the element x from the list.
If x is not found, Python throws a ValueError.
Only removes one match — not all of them

pop([i])
Removes the element at index i and returns it.
If you don’t give it an index, it pops the last item.
If index is out of range → IndexError.

clear()
Removes all elements from the list.
Leaves you with an empty list.
Doesn’t delete the list itself — just clears it out.

 index(x[, start[, end]])
Returns the index of the first occurrence of x.
Optional start and end to search within a specific slice.
If x isn't found it will print ValueError.

 count(x)
Returns the number of times x appears in the list.
Simple, fast, and to the point — no drama, just digits.

sort(key=None, reverse=False)
Sorts the list in-place (changes the original list).
Default is ascending order.
Use reverse=True for descending.
Use key= to customize how items are sorted (like by length, value, etc).

 reverse()
Reverses the order of the list.
Does not sort — just flips it.
Modifies the original list in-place.

copy()
It creates a shallow copy of the list
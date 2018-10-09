# Lists

# Some common lists

# nums = range(1, 10)
# print(sum(nums))
# print(max(nums))
# print(min(nums))
# print(sum(nums) / len(nums))

# How to print the last item in a list

list = ["A", "B", "C", "D", "E"]

# print (list[-1])
# print (list[-3]) # gives us the 3rd last item in the list
# print (list[:]) # i.e. list[start:up to not incluiding], so gives us all items in the list
# print (list[:3]) # gives us start to C i.e. A up to not including D.
# print (list[:-3]) # gives us start to B i.e. A then counting back from end of list up to not including C.

# Another way of looking at this is;
# last = list(-1)
# rest = list(:-1)

# List equality is based on values and order

# l = [1, 2, 3]
# m = [1, 2, 3]

# print(l == m) # Returns True.


# l = [1, 2, 3]
# m = [1, 3, 2]

# print(l == m) # Returns False.


# List comprehension

l = [i*2 for i on range(10)]

print(l)

# ...is the same as;

m = []
for i in range(10):
    m.apend(i*2)
    
print(m)    

s1 = {10, 20, 30}
print (s1)
# creates a set from a list
s2 = set([ 20, 30, 40])
print (s2)
# creates an empty dictionary
s3 = {}
print (type(s3))
# use set() constructor to create empty set
s4 = set()
print (type(s4))
print (s4)

# # set insertions # #
s = {10, 20}
s.add(30)
print (s)
# duplicate items are ignored
s.add(30)
print (s)
# updating set with list
s.update([40, 50])
print (s)
# updating with multiple collection items - set & list
s.update ({60, 70}, [80, 90])
print (s)

# # set removal operations # #
s = {10,30,20,40}
print (s)
s.discard(30)
print (s)
# raises error if item not present
s.remove(20)
print (s)
# empty the set
s.clear()
print (s)
s.add(50)
print (s)
# removes the object s
del s

# # other operations # #
s = {10, 30, 20, 40}
print(len(s))
print (20 in s)
print (50 in s)

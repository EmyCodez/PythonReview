# in and not in operators
s = "Fruit Basket"
# prints False as 'F  is present
# not 'f'
print ("f" in s)
print ("ru" in s)
print ("st" in s)

# membership test in Dictionary
d = { 10:"abc", 20: "efg"}
print (10 in d)
# Prints True 15 is not a key 
print (15 not in d)
# prints False "abc" is value not key
print ("abc" in d)

# not in list
l = [10, 20, 30, 15]
print (30 not in l)
print (40 not in l)
# [20,30] is a sub-list but
# not a member, so prints True
print ([20,30] not in l)
t = (10, 20, "geek")
print (t)
# empty tuple
t = ()
print (type(t))
print (t)
# Cannot create a singe item tuple, it creates an item of specified datatype 
# here it creates int
t = (10)
print (type(t))
# Creates a single item tuple
t = (10, )
print (type(t))
t = 10, 20, 30, 40, 10
print('Tuple t =', t)
print (t[2])
# right side traversal begins from -1
print (t[-1])
# items 1 and 2 are printed, last index 3 is excluded
print (t[1:3])
# return length of tuple
print (len(t))
# finds count of an item in tuple
print (t.count(10))
# returns first index of the item
print (t.index(20))
print ('Max element = ',max(t))
print ('Min element = ',min(t))
       
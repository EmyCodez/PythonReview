s1 = {2, 4, 6, 8}
s2 = {3, 6, 9}
print ("Union of sets: ",s1 | s2)
print ("Intersection of sets: ",s1 & s2)
print ("Set Difference: ", s1 - s2)
print ("Symmetric Difference: ", s1 ^ s2)
# set operations using functions
print ("Union of sets: ",s1.union(s2))
print ("Intersection of sets: ",s1.intersection(s2))
print ("Set Difference: ", s1.difference(s2))
print ("Symmetric Difference: ", s1.symmetric_difference(s2))

s3 = {2, 4, 6, 8}
s4 = {4, 8}
print("Sets: s3 = ",s3,"s4 = ",s4)
print("Is disjoint: ", s3.isdisjoint(s4))
print("Is subset: " , s3 <= s4)
print("Is proper subset: " , s3 < s4)
print("Is superset: " , s3 >= s4)
print("Is proper superset: " , s3 > s4)
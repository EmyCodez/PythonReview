d = {110:"abc", 101: "xyz", 105: "pqr"}
print (d)
# create empty dictionary
d = {}
d["laptop"] = 40000
d["mobile"] = 15000
d["earphone"] = 1000
print (d)
print("Cost of mobile: ",d["mobile"])

# using get()
d = {110:"abc", 101: "xyz", 105: "pqr"}
print (d.get(101))
print (d.get(125))
print (d.get(125, "NA"))
if 125 in d:
    print(d[125])
else:
     print("NA")   

# removal of items in dictionary
d = {110:"abc", 101:"xyz", 105:"pqr", 106:"bcd"}
d[101] = "wry"
print (len(d))
print (d)
print (d.pop(105))
print (d)
del d[106]
print (d)
d[108] = "cde"
# removes last key-value pair
print (d.popitem())
print (d)

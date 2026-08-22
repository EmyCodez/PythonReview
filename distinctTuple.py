arr = (1,2,3,4,5,8)
s = set(arr)
print(s)
print(arr)
print(len(s), len(arr))
if (len(s) == len(arr)) :
    print (True)
else:
    print (False)    
sum = sum(s)
print (sum)

my_dict = {100: "harsh", 101 : "ankit"}
my_dict[102] = "siya"
my_dict.pop(102)
if  my_dict.get(102) :
    print(-1)
else:
    print("Deleted")
print (my_dict.get(108, -1))
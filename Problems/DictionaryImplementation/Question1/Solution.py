# Taking input and initializing dictionary
keys = input().split()
values = map(int, input().split())
my_dict = dict(zip(keys, values))
k, v = input().split()

my_dict[k] = int(v) 
# Consider only correct key-value pairs are given
# Print Inserted if inserted successfully 
print("Inserted")

d = input()

# Delete entry with key d from my_dict
# Print Deleted if deleted successfully else print -1
if d in my_dict :
    del my_dict[d]
    print("Deleted")
else:
    print(-1)
    
p = input()

# Print marks of given key p if key present, else print -1
if p in my_dict :
    print("Marks of "+ p + " is "+ str(my_dict[p]))
else:
    print(-1)
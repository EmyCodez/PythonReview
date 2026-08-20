x = 10
y = x
# is operator
print (x is y)
# is not operator
print ( x is not y)

x1 = 10
x2 = 10
y1 = 10.5
y2 = 10.5
z1 = "Welcome to Python"
z2 = "Welcome to Python"
a1 = None
a2 = None
print (x1 is x2)
print (y1 is y2)
print (z1 is z2)
print (a1 is a2)

# identity comparison in containers
l1 = [10, 20, 30]
l2 = [10, 20, 30]
# prints false as id() is different
# lists are stored in different locations
print (l1 is l2)

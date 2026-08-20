a = 10
b = 20
c = 30
print ( a < b and b < c)
print ( a < b or b > c)
print (not a > b)

# Logical operators evaluating to non-boolean values
s1 = ""
s2 = s1 or "DefaultStr"
# prints DefaultStr as s1 is empty
print (s2)

# short circuiting, last evaluated value is printed
x = 10
print ( x or 20)
y = 0
# prints 30 as y is false
print ( y or 30)
z = 40
# prints 50 as z is true
print (z and 50)
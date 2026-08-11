# implicit type conversion
a = 10
b = 1.5
c = a + b
print (c)
d = True
e = a + d
print (e)

# explicit type conversion
s = "135"
i = 10 + int(s)
f = float(s)
print (i)
print (f)

# explicit type conversion collections
s ="geeks"
print (list(s))
print (tuple(s))
print (set(s))

l = ['a', 'b', 'c']
print (str(l))
a = 10
b = 11
print( str(a) + str(b))
c = 12.5
print (str(c))

# containers to list conversion
t = (10, 20, 30)
print (list(t))
s = {10, 20, 30}
print (list(s))

# integers to binary, hex and octal
a = 20
print (bin(a))
print (hex(a))
print (oct(a))

a = "1001"
print (int(a, 2))
b = "12"
print (int(b, 8))
c = "A1"
print (int(c, 16))
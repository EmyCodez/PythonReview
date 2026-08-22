# bitwise AND(&)
x = 3
y = 6
# 3: 011 & 6: 110
# prints 2: 010
print (x & y)

# bitwise OR(|)
x = 3
y = 6
# 3: 011 | 6: 110
# prints 7: 111
print (x | y)

# bitwise XOR(^)
x = 3
y = 6
# 3: 011 ^ 6: 110
# prints 5: 101
print (x ^ y)

# left shift operator(<<)
x = 5
# prints 10: 5 * 2 ^ 1
print (x << 1)
# prints 20: 5 * 2 ^ 2
print (x << 2)
# prints 40: 5 * 2 ^ 3
print (x << 3)

# right shift operator(>>)
x = 5
# prints 2: floor(5/2 ^ 1)
print (x >> 1)
# prints 1: floor(5/2 ^ 2)
print (x >> 2)
# prints 0: floor(5/2 ^ 3)
print (x >> 3)

# bitwise not operator(~)
x = 5
# toggles the bits and this
# equals two's complement of 6
# output becomes -6
print (~x)
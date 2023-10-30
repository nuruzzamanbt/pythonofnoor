a = 223e4
b = 323E5
c = -4344e12
d = 34.3e8
e = -88.3e5
print(a,b,c,d,e, sep="\n")
print(type(a), type(b), type(c), type(d), type(e), sep="\n")
print("Float variable part done.\n")

m = 4j
n = 5 + 4j
o = -89j
p = 445.3j - 43j
print(m,n,o,p)
print(type(m), type(n), type(o), type(p), sep = "\n")
print("Complex variable part done.\n")

ab = 85
ac = 450.492
ad = -95.3
ae = 49 - 8j
print(ab, ac, ad, ae)
print(type(ab), type(ac), type(ad), type(ae))
print("After Type Casting of the variable")
ba = float(ab)
bb = int(ac)
bc = complex(ad)
bd = complex(ab)
print(ba, bb, bc, bd)
print(type(ba), type(bb), type(bc), type(bd))
print("Type Casting part done.\n")




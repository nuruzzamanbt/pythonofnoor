x = str("Nuruzzaman")
print(x)
print("\n Type casting in with string")
b = str(type(x))
print(b)
p1 = str(1)
p2 = str('134')
p3 = str(43.34)
p4 = str('Python')
print(p1,p2,p3,p4, sep="\n")
print(type(p1), type(p2), type(p3), type(p4), sep= "\n")

str1 = """Hello dear, I am Nuruzzaman Shawon.
Do you remember me ?
We met at Durbachara High School on annual sports day of 2022 at room number 7.
I liked you so much."""
print(str1)

print("\nString is an array of Charecter.")
print(x[7])
print(str1[6])

print("\nLooping Through a String")
for a in x:
    print(a, sep=" ")

print("Length of string 'x' is = ",len(x))
print("loom" in str1)
print("room" in str1)
if "Shawon" in str1:
    print("Data found")
else:
    print("Data not found")
print("sun" not in str1)
print("2022" not in str1)
if "Shawon" not in str1:
    print("Got it")
else:
    print("Didn't got")



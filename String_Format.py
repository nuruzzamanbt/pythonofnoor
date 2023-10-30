print("-----String Format-----")
Year = 2011
scale = 5
result = 4.31
a = "My SSC result is {} out of {:.2f} on the year {}."
print(Year, scale, result, a, sep="\n")
###print("I got" + Year) --> Through Error
print(a.format(Year,scale,result))
print(a.format(result,scale,Year))
print("-----String Format with index-----")
a = "My SSC result is {2} out of {1} on the year {0}."
print(a)
print(a.format(Year,scale,result))
a = "My SSC result is {1:.1f} out of {1:.3f} on the year {0}."
print(a.format(Year,scale))
b = "I bought a {model} car with {price:.3f} dollers."
print(b)
print(b.format(model = "Nissan Urban 3", price = 1320.4))


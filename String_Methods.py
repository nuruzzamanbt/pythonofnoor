a = "nuruzzaman shawon"
b = "BEAUTIFUL BANGLADESH IS BEAUTIFUL"
print(a,b, sep="\n")
print(a.capitalize())
print(b.casefold())
print(a.center(30,'-'))
print(b.count('BEAUTIFUL'))
print(b.index("H"))
#print(b.index("O"))
print(b.find("H"))
print(b.find("O"))
print(b.index("U",20,28))
c = "শাওন"
d = c.encode()
print(d)
print(c.encode(encoding="ASCII",errors="namereplace"))
print(b.endswith('k'))
print(a.endswith('sha', 4, 14))
e = "M\tO\tO\tN\tL\tI\tG\tH\tT"
print(e, e.expandtabs(3), e.expandtabs(11), sep="\n")
print(b.isspace())
print(b.istitle())
print(a.islower())
f = "       nuruzzaman shawon      "
print(a.ljust(42), b)
print(f.lstrip(),b)


g = "Hello Sam Baba"
mytable = str.maketrans("S", "P")
mytable2 = str.maketrans("H", "D")
mytable3 = str.maketrans("loH","kaM")
mytable4 = str.maketrans("loH","kaM","bB")
print(g.translate(mytable))
print(g.translate(mytable2))
print(g.translate(mytable3))
print(g.translate(mytable4))
bana= "I love Rose so much for giving my dearest one."
nana = bana.partition("Rose")
sana = bana.partition("Lily")
print(nana)
print(nana[0],nana[1])
print(sana)
sumation = "two and two makes four and two multiply two makes four also."
print(sumation,sumation.replace("two", "one"),sep="\n")
print(sumation.replace("two", "one",2))
print(sumation.find("two"))
print(sumation.rfind("two"))
print(sumation.rindex("two"))
print(sumation.rfind("two",5,39))
tan = sumation.partition("two")
uan = sumation.rpartition("two")
print(tan)
print(uan)
print(sumation.split("two"))
print(sumation.rsplit("two",2))
print(f.rstrip(),b)
print(f.strip(),b)
nin = """Mohammad
Nuruzzaman
Shawon
"""
nun = nin.splitlines()
nun2 = nin.splitlines(True)
print(nun)
print(nun2)
print(sumation)
print(sumation.startswith("two",8,24))
print(nin)
print(nin.swapcase())
print(sumation.title())
print(sumation.upper())
print(g)
print(g.zfill(20))















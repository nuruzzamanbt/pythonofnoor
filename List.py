nList = ["Nuruzzaman", "Shawon", "Muslima", "Joti", "Alif", "Tanvir"]
nList2 = [1, 44, 22, 10, 88, 44, 20, 99]
nList3 = [True, False, True, True, True, False, False, True]
nList4 = [43.22, 59.3, 99.88]
nList5 = [0, 33, 50.48, "Nuruzzaman", "Shawon", True, False]
nList6 = ["Nuruzzaman", "Shawon", "Muslima", "Joti", "Alif", "Tanvir"]
'''
print(nList,type(nList), nList2, type(nList2), nList3,type(nList3), nList4,type(nList4), nList5, type(nList5), sep="\n")
print(nList[2])
print(nList[1:3])
print(nList[:2])
print(nList[3:])
print(nList[-2])
print(nList[-5:-2])
print(nList[:-3])
'''
nList[4] = "Faisal"
print(nList)
nList[0:2] = ["Mohammad","Nuruzzaman","Shawon","Srabon"]
nList.insert(4,"Mizanur")
nList.append("Nurjahan")
nList6 = nList
nList6.extend(nList5)
nTuple = ("My", "Python", "Coding", "Practice")
nList6.extend(nTuple)
nList6.remove("Practice")
nList6.pop(18)
print(nList6.__len__())
print(nList6)
nList6.pop()
print(nList6)
print(nList6.__len__())
del nList6[3]
print(nList6)
nList6.clear()
print(nList6)
print(nList6.__len__())
#del nList6
print(nList6)
[print(x) for x in nList5]
for i in nList2:
    print(i)
for i in range(len(nList5)):
    print(i)

j=1
while j < len(nList5):
    print(j*11+1)
    j = j + 1




l=[1,2,3,1.1,2.2,3.3,"tops",True,1,10,"Python",False]

print(l)
l.append(100)
print(l)
#l.clear()
#print(l)
l1=l.copy()
print(l1)
print(l.count(1))
l2=[100,200,300]
l.extend(l2)
print(l)
print(l.index(10))
l.insert(5,101)
print(l)
l.pop()
print(l)
l.remove(10)
print(l)
l.reverse()
print(l)

for i in l:
    print(i)
print("tops1" in l)

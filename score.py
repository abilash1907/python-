s=[]
n=int(input("enter the no.of score"))
print("enter the score")
for i in range(n):
	j=int(input())
	s.append(j)
b=set()
L=[]
for x in s:
	if x not in b:
		L.append(x)
		b.add(x)
L.sort()
k=len(L)
print(L[k-2])
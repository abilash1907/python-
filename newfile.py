sum=2
l=[]
c=0
n=int(input("enter a number"))
for i in range(2,n+1):
	if(i>1):
		for j in range(2,i):
			if(i%j==0):
				break
		else:
				l.append(i)
print(l)
for k in range(1,len(l)):
	sum=sum+l[k]
	if sum in l:
		c+=1
print(c)
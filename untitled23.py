n = input("enter the string ")
f = open("new.txt","w")
f.write(n)
f.close()
l = input("enter the letter to be searched")
f = open("new.txt","r")
count = 0
for i in f.read():
    if i==l:
        count+= 1
print(count,"is the occurance of",l)
f.close()

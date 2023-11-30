str=input("Enter the first string :")
dist={}
for i in str:
	if i in  dist:
		dist[i]=dist[i]+1
	else:
		dist[i]=1
str1=input("Enter the second string :")
diste={}
for i in str1:
	if i in  diste:
		diste[i]=diste[i]+1
	else:
		diste[i]=1
dist.update(diste)
print("Merged dictionary:", dist)


l=[]
ans=[]
n= int(input("Enter number of values: "))
for i in range(n): 
    v = int(input("Enter number value of list: "))
    l.append(v)
print(l)
i=0
ln=len(l)
k= int(input("Enter number of cluster: "))
for j in range(k):
    temp=[]
    ans.append(temp)
st=0

for j in ans:
    d=st;
    while (d<ln)):
        j.append(l[d])
        d=d+2
    st = st + 1
    print(j)
print(ans)

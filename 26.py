# f=open('files/26_2650.txt')
# l,m,n=map(int,f.readline().split())
# from itertools import accumulate
# a=[0]*(l+1)
# for i in range(n):
#     st,dl=map(int,f.readline().split())
#     a[st]+=1
#     a[st+dl]-=1
# a=list(accumulate(a))
# st,end=-1,0
# count=ma=0
# for i in range(l+1):
#     if a[i]==0 and st==-1:st=i
#     if (a[i]==1 and a[i-1]==0) or i==l:
#         end=i
#         lenght = end - st
#         if lenght >= m:
#             count += 1
#         ma = max(ma, lenght)
#         st, end = -1, 0
# print(count,ma)
f=open("files/26_2255.txt")
n,m=map(int,f.readline().split())
pr=[]
for i in range(n):
    p,b=f.readline().split()
    p=int(p)
    pr.append([p,b])
pr.sort()
A=[i for i in range(n) if pr[i][1]=="A"]
Ca=c=0
for i in range(n):
    if c+pr[i][0]<=m:
        c+=pr[i][0]
        last = i
        if pr[i][1]=="A":
            Ca+=1
            A.remove(i)
for i in A:
    for j in range(last,-1,-1):
        if pr[j][1]!="A" and c+pr[i][0]-pr[j][0]<=m:
            Ca+=1
            c += pr[i][0] - pr[j][0]
            last=j-1
            break
print(Ca,m-c)

# from random import *
#
# n = 1000
# for _ in range(100):
#     a = [randint(1, 100000) for i in range(n)]
#     mxA = 0
#     for i in range(n):
#         s = k = 0
#         for j in range(i, n):
#             s += a[j]
#             k += a[j] % 11 == 0
#             if k % 7 == 0:
#                 mxA = max(mxA, s)
#     b = [10 ** 20] * 7
#     mxB = k = s = 0
#     for i in range(n):
#         x = a[i]
#         s += x
#         k += x % 11 == 0
#         if k % 7 == 0:
#             mxB = max(mxB, s)
#         s1 = s - b[k % 7]
#         mxB = max(mxB, s1)
#         b[k % 7] = min(b[k % 7], s)
#     print(mxA, mxB, mxB == mxA)
# k,n,*a=map(int,open('27B_9757.txt'))
# m0=m17=m119=m289=m7=m2023=m2_0=m2_17=m2_119=m2_289=m2_7=m2_2023=-10**20
# m=-10**20
# for i in range(2*k,n):
#     p=a[i-2*k]
#     if p%17==0:m17=max(m17,p)
#     if p % 7 == 0: m7 = max(m7, p)
#     if p % 119 == 0: m119 = max(m119, p)
#     if p % 289 == 0: m289 = max(m289, p)
#     if p % 2023 == 0: m2023 = max(m2023, p)
#     m0 = max(m0, p)
#     q=a[i-k]
#     if q % 17 == 0:
#         m2_17 = max(m2_17, q*m0)
#         m2_289=max(m2_289,q*m17)
#         m2_119 = max(m2_119, q * m7)
#         m2_2023 = max(m2_2023, q * m119)
#         m2_7 = max(m2_7, q * m7)
#
#
#     if q % 7 == 0:
#         m2_17 = max(m2_17, q * m17)
#         m2_289 = max(m2_289, q * m289)
#         m2_119 = max(m2_119, q * m17)
#         m2_2023 = max(m2_2023, q * m289)
#         m2_7 = max(m2_7, q * m0)
#
#     if q % 119 == 0:
#         m2_17 = max(m2_17, q * m0)
#         m2_289 = max(m2_289, q * m17)
#         m2_119 = max(m2_119, q * m0)
#         m2_2023 = max(m2_2023, q * m17)
#         m2_7 = max(m2_7, q * m0)
#
#     if q % 289 == 0:
#         m2_17 = max(m2_17, q * m0)
#         m2_289 = max(m2_289, q * m0)
#         m2_119 = max(m2_119, q * m7)
#         m2_2023 = max(m2_2023, q * m7)
#         m2_7 = max(m2_7, q * m7)
#
#     if q % 2023 == 0:
#         m2_17 = max(m2_17, q * m0)
#         m2_289 = max(m2_289, q * m0)
#         m2_119 = max(m2_119, q * m0)
#         m2_2023 = max(m2_2023, q * m0)
#         m2_7 = max(m2_7, q * m0)
#     m2_0 = max(m2_0, p*m0)
#     if a[i]%2023==0:m=max(m,m2_0*a[i])
#     elif a[i]%289==0:m=max(m,a[i]*m2_7)
#     elif a[i]%119==0:m=max(m,a[i]*m2_17)
#     elif a[i] % 17==0:m = max(m,  a[i] * m2_119)
#     elif a[i] % 7==0:m = max(m,  a[i] * m2_289)
#     else:m=max(m,a[i]*m2_2023)
# print(m)
# print(len(str(1142638807748265450)))
from itertools import  accumulate
f=open('27B.txt')
n=int(f.readline())
a=[[int(i) for i in s.split()] for s in f]
m=-10*20
ans=[]
rows=[list(accumulate(a[i])) for i in range(n)]
print( sum(rows[i][-1] for i in range(n)))


from functools import lru_cache
@lru_cache(None)
def f(c,e,k3=0,k5=0):
    if c>e:return 0
    if c%5==0:k5+=1
    if c%3==0:k3+=1
    if c==e:return k5==k3

    return f(c+1,e,k3,k5)+f(c+4,e,k3,k5)+f(c*3,e,k3,k5)
a=f(1,180)
print(sum(int(i) for i in str(a)))
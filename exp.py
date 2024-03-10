def CC(x,n):
    c=sorted('0123456789')+sorted('qwertyuioplkjhgfdaszxcvbnm')
    s=''
    while x>0:
        s=c[x%n]+s
        x//=n
    return s


def to_dec(a,n):
    a=a[::-1]
    return sum(a[i]*n**i for i in range(len(a)))
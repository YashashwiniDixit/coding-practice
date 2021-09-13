# cook your dish here
t=int(input())
for i in range(t):
    x=0
    y=0
    a, b, c, d, e=input().split(" ")
    a=int(a)
    b=int(b)
    c=int(c)
    d=int(d)
    e=int(e)
    x=a+b+c
    l=[a,b,c]
    l.sort(reverse=True)
    for i in l:
        if i<=e:
            y=i
            break
    if (x-y<=d and y!=0):
        print("YES")
    else:
        print("NO")
    
#https://www.codechef.com/SEPT21C/problems/AIRLINE/

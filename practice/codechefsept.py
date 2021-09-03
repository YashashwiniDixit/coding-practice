# cook your dish here
t=int(input())
for i in range(0,t):
    n, a, b= input().split(" ")
    sum=0
    a=int(a)
    b=int(b)
    s=input()
    for i in s:
        if i=="0":
            sum+=a
        else:
            sum+=b
    print(sum)
    
    #https://www.codechef.com/SEPT21C/problems/TRAVELPS

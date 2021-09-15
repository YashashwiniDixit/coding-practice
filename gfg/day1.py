
class Solution:
    def sort012(self,arr,n):
        # code here
        a=0
        b=0
        c=0
        for i in arr:
            if i==0:
                a+=1
            elif i==1:
                b+=1
            elif i==2:
                c+=1
        arr.clear()
        for i in range(a):
            arr.append(0)
        for i in range(b):
            arr.append(1)
        for i in range(c):
            arr.append(2)
            


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends

class Solution:
    
    #Function to find the maximum number of meetings that can
    #be performed in a meeting room.
    def maximumMeetings(self,n,start,end):
        # code here
        count  = 1
        arr = [(i, j) for i,j in zip(start, end)]
        arr = sorted(arr, key = lambda x:x[1])
        n = len(arr)
        s = 0
        for i in range(1, n):
            if arr[i][0] > arr[s][1]:
                count += 1
                s = i
        
        return count
        
        
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        ob=Solution()
        print(ob.maximumMeetings(n,start,end))
# } Driver Code Ends

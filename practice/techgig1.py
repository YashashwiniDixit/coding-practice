''' Read input from STDIN. Print your output to STDOUT '''
    #Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    t=int(input())
    for i in range(t):
        s=input()
        e=0
        o=0
        for i in range(0,len(s)):
            if(i%2==0):
                c=s[i]
                c=ord(c)
                o+=c
            else:
                c=s[i]
                c=ord(c)
                e+=c
        s1=abs(e-o)
        b=0
        for i in range(3,10,2):
            if(s1%i)==0:
                b=1
                break
        if(b==1):
            print("Prime String")
        elif(b==0):
            print("Casual String")
 # Write code here 

main()

'''
Prime String (100 Marks)
Oddia and Evenia are two friends who love strings and prime numbers. Although they have the same taste and like similar things, they are enemies when it comes to even and odd numbers. Oddia likes the odd numbers and Evenia likes the even numbers. They have a problem for you to solve.


A string S of lowercase letters will be provided and you have to figure out if the given string is Prime String or not. The index starts at 1.


Prime String: A string is considered a prime string only if the absolute difference between the sum of odd indexed letters and even indexed letters is completely divisible by any of the odd prime numbers less than 10.


Note: For calculations, consider the ASCII value of lowercase letters.


Example:

String, S = abcdef

Summation of Odd Indexed letters, O = a + c + e = 97 + 99 + 101 = 297

Summation of Even Indexed letters, E = b + d + f = 98 + 100 + 102 = 300


Absolute Difference = |O-E| = |297-300| = 3


This is completely divisible by 3 and leaves 0 as remainder. Thus, the given string is a Prime String.


If the string is prime string, print Prime String otherwise print Causal String. Can you solve it?

Input Format
The first line of input consists of the number of test cases, T

Next N lines each consist of a string, S.


Note: Read the input from the console.

Constraints
1<= T <=10

2<= |S| <=10000


|S| is the length of the string.

Output Format
For each test case, print Prime String if the string is prime string otherwise print Casual String.

Sample TestCase 1
Input
2
bbae
abcdef
Output
Casual String
Prime String
Explanation
Test Case 1: 

Sum of Odd indexed letters, O = 98+97 = 195

Sum of Even indexed letters, E = 98 + 101 = 199


Absolute Difference = |195-199| = 4


This is not divisible by any of the odd prime numbers. The given string is Casual String.
'''

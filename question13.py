'''The function accepts two integers n, m as arguments Find the sum of all numbers 
in range from 1 to m(both inclusive) that are not divisible by n. 
Return difference between sum of integers not divisible by n with sum of numbers 
divisible by n.
Assumption:
n>0 and m>0
Sum lies between integral range
Example
Input
n:4
m:20
Output
90'''

def toss_s(s):
    head=0
    score=0
    for i in s:
        if(i=='H'):
            head+=1
            score=score+2
            if head==3:
                break
        else:
            score-=1
            head=0
    return score
s=str(input().upper())
print(toss_s(s))


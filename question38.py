'''Smallest Number
Prince participated in three Olympiads at school and received marks for all of them. 
He is interested in finding out the lowest mark he obtained among the three 
Olympiads. Write a program to find the minimum mark.
Example:
Input: 50 66 23
Output: Smallest number is 23'''


def min_marks(a,b,c):
    if(a<b and a<c):
        return a
    if(b<a and b<c):
        return b
    if(c<a and c<b):
        return c
     
a=int(input())
b=int(input())
c=int(input())
print(" min marks out of 3 olympiads are: ",min_marks(a,b,c))
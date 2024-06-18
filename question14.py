'''
Toss and score
You are playing a game of Toss and Score in the Hillwood City Mall with your friends.
The game consists of the following rules:
Toss an unbiased coin multiple times.
For each heads you get 2 points and for each tails you lose 1 point.
The game ends as soon as you get 3 heads in a row, or you toss the coin throughout
the length of string S.
You have been given a string 5 consisting of letters H (for heads) and T (for tails)
denoting the sequence results you get on the toss of coin N times. Your task is to find
and return an integer value representing the final score you get once the game ends.
Note: The final score can be negative too.
Input Specification:
Input1: A string s. representing the sequence of results you get on the toss of coin 
N times
Sample Input:
HHHTT
Output:
6
'''

def toss_score(s):
    score=0
    head_count=0
    for toss in s:
        if toss=='H':
            score+=2
            head_count+=1
            if head_count==3:
                break
        else:
            score-=1
            head_count=0
    return score
s=input()
print(toss_score(s))
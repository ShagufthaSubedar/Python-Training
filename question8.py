'''Special String
Alice has a string A consisting of lowercase English letters. Her friend gives her another string S
and asks her to modify string A and replace its characters with the characters present in string S.
But, to achieve the above task, Alice must follow the below steps:
1. Choose a character from string S that has the minimum ASCII distance from the ith character in
string A
Replace the ith character in string A with the chosen character in string S
Your task is to find and return an integer value, representing minimum total ASCII distance that is
required to modify string A to the characters in string S. Return 0, if all the characters in string S
are already present in string A
Sample Input:
abcd
xyz
Sample Output:
86'''



def minimum_ascii_distance(A: str, S: str) -> int:
    if set(S).issubset(set(A)):
        return 0
    total_distance = 0
    for char_a in A:
        min_distance = float('inf')
        for char_s in S:
            distance = abs(ord(char_a) - ord(char_s))
            if distance < min_distance:
                min_distance = distance
        total_distance += min_distance
    return total_distance
A = "abcd"
S = "xyz"
print(minimum_ascii_distance(A, S))

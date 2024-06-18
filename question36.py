'''Peak Element Finder
Description: You are given an N- dimensional array arr[]. A peak element in the array 
is defined as an element whose value is greater than or equal to its neighboring 
elements (if they exist). Your task is to find the index of any peak element in the given 
array
Note: use 0-based indexing
Input:
An integer representing the number of elements in the array. N space-separated 
integers, denoting the elements of the array.
N space-separated integers ,denoting the elements of the array arr[]
Sample Input:
5
1 3 20 4 1
Sample Output:
2'''
 
def peakele(arr):
    n=len(arr)
    for i in range(n):
        if (i == 0 or arr[i] >= arr[i - 1]) and (i == n - 1 or arr[i] >= arr[i + 1]):
            return i
    return -1
n=int(input())
arr=list(map(int,input().split()))
print(peakele(arr))

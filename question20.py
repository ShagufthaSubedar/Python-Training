'''extracting maximum count of vowels in a pharase'''

def max_count(s):
    vowels = 'aeiou'
    max_vowel = max(vowels, key=s.count)
    print(f"The vowel '{max_vowel}' has the maximum count of {s.count(max_vowel)}.")
    return max_vowel
s=input()
max_count(s)




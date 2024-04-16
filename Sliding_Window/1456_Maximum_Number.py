# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.
# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.

s = "abciiidef"
k = 3

def max_vowels(s, k):
    max_count, curr_count = 0, 0
    vowels = "aeiou"
    for i, v in enumerate(s):
        if i >= k:
            if s[i - k] in vowels:
                curr_count -= 1
        if s[i] in vowels:
            curr_count += 1
        max_count = max(curr_count, max_count)
    return max_count



print(max_vowels(s, k))
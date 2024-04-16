# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with
# word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.

def merge_alternately(self, word1, word2):
    result = ""
    for i in range(max(len(word1), len(word2))):
        result += word1[i:i + 1] + word2[i:i + 1]
    return result

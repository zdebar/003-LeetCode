# For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated
# with itself one or more times).
#
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


def gcdOfStrings(str1, str2):
    if str1 + str2 != str2 + str1:
        return ""
    if len(str1) == len(str2):
        return str1
    if len(str1) > len(str2):
        return gcdOfStrings(str1[len(str2):], str2)
    return gcdOfStrings(str1, str2[len(str1):])

str1 = "ABCABC"
str2 = "ABC"
print(gcdOfStrings(str1, str2))

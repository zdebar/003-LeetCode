def isSubsequence(s, t):
    pos = 0
    for i in t:
        if i == s[pos]:
            pos += 1
        if pos == len(s):
            return True
    return False

s = "abc"
t = "ahbgdc"
print(isSubsequence(s,t))
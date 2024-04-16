# Given a string s, reverse only all the vowels in the string and return it.
#
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


def reverseVowels(self, s):
    vowels = []
    for i in s:
        if i in "aeiouAEIOU":
            vowels += i
    s = list(s)
    for i in range(len(s)):
        if s[i] in "aeiouAEIOU":
            s[i] = vowels.pop()
    return "".join(s)


def reverseVowels(s: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
    s_list = list(s)
    left, right = 0, len(s_list) - 1

    while left < right:
        while left < right and s_list[left] not in vowels:
            left += 1
        while left < right and s_list[right] not in vowels:
            right -= 1

        if left < right:
            s_list[left], s_list[right] = s_list[right], s_list[left]
            left += 1
            right -= 1

    return ''.join(s_list)


# Example usage:
s = "hello world"
print(reverseVowels(s))  # Output: "hollo werld"
def closeStrings(self, word1, word2):
    frequency_word1 = Counter(word1)
    frequency_word2 = Counter(word2)

    sorted_values_word1 = sorted(frequency_word1.values())
    sorted_values_word2 = sorted(frequency_word2.values())

    keys_match = set(frequency_word1.keys()) == set(frequency_word2.keys())

    return sorted_values_word1 == sorted_values_word2 and keys_match

def closeStrings(self, word1: str, word2: str) -> bool:
    freq1 = [0] * 26
    freq2 = [0] * 26

    for ch in word1:
        freq1[ord(ch) - ord('a')] += 1

    for ch in word2:
        freq2[ord(ch) - ord('a')] += 1

    for i in range(26):
        if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
            return False

    freq1.sort()
    freq2.sort()

    for i in range(26):
        if freq1[i] != freq2[i]:
            return False

    return True
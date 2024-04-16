from collections import Counter


def compress(chars):

    count = dict(Counter(chars))
    output = []
    for key, value in count.items():
        output.append(key)
        if value != 1:
            output.extend(list(str(value)))
    return len(chars), output


def compress_2(chars):
    i = 0
    place, chars[:] = chars[:], []
    while i < len(place):
        letter = place[i]
        count = 0
        while i < len(place) and letter == place[i]:
            count += 1
            i += 1
        chars.append(str(letter))
        if count > 1:
            chars += (list(str(count)))
    return len(chars)




chars = ["a","a","b","b","c","c","c"]
print(compress_2(chars))
chars = ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]
print(compress_2(chars))
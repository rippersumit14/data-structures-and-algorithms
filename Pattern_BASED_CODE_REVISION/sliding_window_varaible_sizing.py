#When the size of the window is not fixed, usually for problems involving conditions (sum, distinct,char, etc)
#Used in data stream analysis

def length_of_longest_sub_strings(s):
    left = 0
    max_len = 0
    char_set = set()

    for right in range(len(s)):
        while s[left] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_len = max(max_len, right-left+1)

    print(char_set)

    return max_len


print(length_of_longest_sub_strings("helloWorld"))



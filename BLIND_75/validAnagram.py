'''
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

Example 1:

Input: s = "racecar", t = "carrace"

Output: true
Example 2:

Input: s = "jar", t = "jam"

Output: false
Constraints:

1 <= s.length, t.length <= 5 * 10^4
s and t consist of lowercase English letters.

'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
#Python also like checks the compare the english characters also in ascending form
        # If the lengths are different,
        # they cannot be anagrams.
        if len(s) != len(t):
            return False

        # Convert strings into lists
        s = list(s)
        t = list(t)

        # -------------------------
        # Selection Sort for s
        # -------------------------
        n = len(s)

        for i in range(n - 1):

            # Assume current index is minimum
            min_idx = i

            # Find the actual minimum element
            for j in range(i + 1, n):
                if s[j] < s[min_idx]:
                    min_idx = j

            # Swap
            s[i], s[min_idx] = s[min_idx], s[i]

        # -------------------------
        # Selection Sort for t
        # -------------------------
        n = len(t)

        for i in range(n - 1):

            min_idx = i

            for j in range(i + 1, n):
                if t[j] < t[min_idx]:
                    min_idx = j

            t[i], t[min_idx] = t[min_idx], t[i]

        # Compare both sorted lists
        return s == t

        # Time Complexity:
        # O(n²) + O(n²) + O(n)
        # = O(n²)

        # Space Complexity:
        # O(n)

answer = Solution()
print(answer.isAnagram("racecar", "carrace"))





#optimized way to solve this problem
class Soultion_2:
    def anagram(self, s: str, t: str):
        #Now solving in the optimized way
        #Edge case
        if len(s) != len(t):
            return False

        #Creating 2 empty dictionary
        s_count = {}
        t_count = {}

        for ch in s:
            if ch in s_count:
                s_count[ch] += 1
            else:
                s_count[ch] = 1 #o(n) time

        for ch in t:
            if ch in t_count:
                t_count[ch] += 1
            else:
                t_count[ch] = 1


        '''
        racecar and carrace
        s_count = {                       
                                              
            r: 2,
            a: 2,
            c: 2,
            e: 1
            }
            
        t_count = {
            
            r: 2,
            a: 2,
            c: 2,
            e: 1
            }
        '''

        #Now we check the count of each characters count in the dictionary
        for key in s_count:

            if key not in t_count:
                return False

            if s_count[key] != t_count[key]:
                return False

        return True

ans2 = Soultion_2()
print(ans2.anagram("racecar", "carrace"))



















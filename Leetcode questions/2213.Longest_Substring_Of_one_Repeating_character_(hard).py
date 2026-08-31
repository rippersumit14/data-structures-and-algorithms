"""
LeetCode 2213 - Longest Substring of One Repeating Character
Difficulty: Hard

Problem:

You are given:

1. A string s.
2. A string queryCharacters.
3. An integer array queryIndices.

Each query changes one character inside the string.

For the ith query:

    queryIndices[i]
        -> tells us which index of s needs to be changed.

    queryCharacters[i]
        -> tells us the new character to place at that index.


After performing EACH query:

Find the longest continuous substring where all characters
are the same.

Store the length of that substring in the answer array.

Important:
The string does NOT reset after each query.
Every query works on the string produced by the previous query.


--------------------------------------------------

Example 1:

Input:

s = "babacc"

queryCharacters = "bcb"

queryIndices = [1, 3, 3]


Query 1:

index = 1
character = 'b'

Before:
"babacc"

After:
"bbbacc"

Repeating groups:

"bbb" -> length 3
"a"   -> length 1
"cc"  -> length 2

Longest = 3


--------------------------------------------------

Query 2:

index = 3
character = 'c'

Current string:
"bbbacc"

After:
"bbbccc"

Repeating groups:

"bbb" -> length 3
"ccc" -> length 3

Longest = 3


--------------------------------------------------

Query 3:

index = 3
character = 'b'

Current string:
"bbbccc"

After:
"bbbbcc"

Repeating groups:

"bbbb" -> length 4
"cc"   -> length 2

Longest = 4


Therefore:

Output:
[3, 3, 4]


--------------------------------------------------

Main Goal:

For every query:

1. Update the character at queryIndices[i].

2. Find the longest consecutive group containing
   only the same character.

3. Store its length in the answer array.

4. Continue with the updated string for the next query.

5. Return the answer array.


Constraints:

1 <= len(s) <= 10^5

1 <= number of queries <= 10^5


Important Observation:

A simple approach could update the character and scan the
entire string after every query.

However, because both the string and number of queries can
be as large as 100,000, repeatedly scanning the whole string
would be too slow.

Therefore, an optimized data structure/approach is required.
"""
"""
------------------------------------------------------------
Remove Outermost Parentheses
Easy
------------------------------------------------------------

Problem Statement

A valid parentheses string follows these rules:

1. An empty string "" is valid.
2. If A is a valid parentheses string,
   then "(" + A + ")" is also valid.
3. If A and B are valid parentheses strings,
   then A + B is also valid.

A primitive valid parentheses string is a
non-empty valid parentheses string that
cannot be split into two or more valid
parentheses strings.

Your task is to remove the outermost
parentheses from every primitive string
and return the final result.

------------------------------------------------------------
Example 1

Input:
s = "((()))"

Output:
"(())"

Explanation:

Primitive:

((()))

Remove the outermost '(' and ')'

Result:

(())

------------------------------------------------------------
Example 2

Input:
s = "()(()())(())"

Output:
"(()())()"

Explanation:

Primitive Strings:

()

(()())

(())

Remove the outermost parentheses
from each primitive:

()        -> ""
(()())    -> ()()
(())      -> ()

Final Answer:

(()())()

------------------------------------------------------------
Constraints

1 <= len(s) <= 10^5

s contains only '(' and ')'

s is always a valid parentheses string.

------------------------------------------------------------
Function Signature

class Solution:
    def removeOuterParentheses(self, s: str) -> str:

------------------------------------------------------------
Expected Time Complexity

O(n)

Expected Space Complexity

O(n)

------------------------------------------------------------
"""
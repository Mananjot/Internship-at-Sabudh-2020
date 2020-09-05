"""
Question1: Valid Parentheses

Given a string input_string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.

Example 1:
Input: input_string = "()"
Output: true

Example 2:
Input: input_string = "()[]{}"
Output: true

Example 3:
Input: input_string = "(]"
Output: false

Example 4:
Input: input_string = "([)]"
Output: false

Example 5:
Input: input_string = "{[]}"
Output: true

Constraints:
1 <= input_string.length <= 104
input_string consists of parentheses only '()[]{}'

"""

def solution(input_string):
    stack = []
    mappings = {
        "]" : "[",
        ")" : "(",
        "}" : "{"
    }

    for char in input_string:
        if char in mappings:
            if len(stack) != 0:
                top = stack.pop()
            else:
                return False
            
            if mappings[char] != top:
                return False
        else:
            stack.append(char)
    if len(stack) == 0:
        return True
    return False

print(solution("([)]"))
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.

Example 1:

    Input: s = "()"
    Output: true

Example 2:

    Input: s = "()[]{}"
    Output: true

Example 3:

    Input: s = "(]"
    Output: false

'''

song={'(':")","{":"}",'[':']'}

s="{}("
for i in s:
        
    if "()"==s:
        print(True)
    elif "[]"==s:
        print(True)
    elif "{}"==s:
        print(True)    
    else:
        print(False) 
    
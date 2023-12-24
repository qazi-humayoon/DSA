# In the Shunting Yard algorithm, when a closing parenthesis is encountered, the algorithm needs to pop operators
# from the stack and append them to the result until an opening parenthesis (() is encountered. The opening parenthesis
# is then popped from the stack and discarded.
# Time Complexity: O(N)

# Space Complexity: O(N) for using the stack

def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1

def infix_to_postfix(s):
    stack = []
    result = ""

    for i in range(len(s)):
        c = s[i]

        if c.isalnum():
            result += c

        elif c == '(':
            stack.append('(')

        elif c == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        else:
            while stack and prec(c) <= prec(stack[-1]):
                result += stack.pop()
            stack.append(c)

    while stack:
        result += stack.pop()

    print("Postfix expression:", result)

# Example usage
exp = "(p+q)*(m-n)"
print("Infix expression:", exp)
infix_to_postfix(exp)
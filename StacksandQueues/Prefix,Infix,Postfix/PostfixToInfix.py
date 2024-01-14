def posttoinfix(s):  
    operands = []

    # Iterating from right to left.
    for i in range(len(s)):
        # Check if the current character is an operator.
        if s[i] in ['+', '-', '*', '/']:
            # Taking last two operands from the stack.
            operand1 = operands.pop()
            operand2 = operands.pop()

            # Combining the two operands with the current operator
            # and pushing back to the stack.
            resultantOfTwo = "(" + operand2 + s[i] + operand1 + ")"
            operands.append(resultantOfTwo)
        else:
            # Pushing the character s[i] into the stack.
            operands.append(s[i])

    # Last operand in the stack will be the final answer.
    return operands[-1]

s = 'ab+c+'
checking = posttoinfix(s)
print(checking)

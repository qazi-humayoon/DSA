#Do this way blow is another approach to do it but this is almost same for all

def preToPost(s):
    st = []
    for i in range(len(s) - 1,-1,-1):
        if s[i] in ["*","+","-","/"]:
            op1 = st.pop()
            op2 = st.pop()
            st.append(op1+ op2 + s[i])

        else:
            st.append(s[i])

    return st[-1]


s = "-/A+BC*DE"
checking = preToPost(s)
print(checking)

# ABC+/DE*-

#_______________________________________________________________________________________________________

def preToPost(s: str) -> str:
    # Initializing a stack 'st'
    st = []
    
    # Reverse the string 's'
    s = s[::-1]
    
    # Initializing an array of operators
    o = ['+', '-', '/', '*']
    
    # Iterating over the string 's'
    for i in range(len(s)):
        # Initializing a boolean variable 'isOp'
        isOp = False
        
        # Iterating over the array 'o' to check whether the current character is an operator or not
        for j in range(4):
            if s[i] == o[j]:
                # We found an operator
                isOp = True
        
        # Declare a string 'cur' and append the current character to it
        cur = s[i]
        
        if not isOp:
            # Push 'cur' into the stack 'st'
            st.append(cur)
        else:
            # Pop the top element of the stack and assign it to 's1'
            s1 = st.pop()
            
            # Pop the top element of the stack and assign it to 's2'
            s2 = st.pop()
            
            # Push 's1 + s2 + cur' into the stack
            st.append(s1 + s2 + cur)
    
    # Return the top of the stack
    return st[-1]

s = "-/A+BC*DE"
checking = preToPost(s)
print(checking)


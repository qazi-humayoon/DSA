def posttopre(s):
    
    st = []
    

    
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
            st.append(cur + s2 + s1)
    
    # Return the top of the stack
    return st[-1]
    
    
    
s = "abc*+"
funct = posttopre(s)
print(funct)

def check(s):
    stack = []
    pairs = {
        '(':')',
        '{':'}',
        '[':']'

    }

    for bracket in s:
        if bracket in pairs:
            stack.append(bracket)
        elif len(stack) == 0 or bracket != pairs[stack.pop()]:
            return False
    return len(stack) == 0

s = '[()[{()}]]'
trying = check(s)
print(trying)


#________________________________________________________________________________________
# TC : 0(N)
# SC : 0(N)

def isValid(s: str) -> bool:
    st = []
    for it in s:
        if it == '(' or it == '{' or it == '[': #If opening then append to the stack
            st.append(it)
        else:
            if len(st) == 0: #If len is 0 then there was no opening in the string 
                return False
            ch = st[-1] #Get the last element in the stack and then pop that element from the stack
            st.pop()
            if (it == ')' and ch == '(') or (it == ']' and ch == '[') or (it == '}' and ch == '{'):
                continue #If the element we stored in ch and also popped is equal to any closing then continue and it keeps
            else:        #Pooping from the stack
                return False #If its not equal then return false
    return len(st) == 0 #If the len of the stack is again 0 then that means it is balanced




if __name__ == '__main__':
    s = "()[{}()]"
    if isValid(s):
        print("True")
    else:
        print("False")
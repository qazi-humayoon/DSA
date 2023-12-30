#Optimal
# TC O(N
# SC O(N)

def asteroid(asteroids):
    stack = []  # Initialize an empty stack to store asteroids.

    for ast in asteroids:  # Iterate through each asteroid in the given list 'asteroids'.
        while stack and ast < 0 and stack[-1] > 0 :  # Check if there are elements in the stack and the current asteroid is negative while the top of the stack is positive.
            if stack[-1] < abs(ast):  # If the absolute value of the current asteroid is greater than the top of the stack, pop the stack.
                stack.pop()
                continue
            elif stack[-1] == -ast:  # If the absolute value of the current asteroid is equal to the top of the stack, pop the stack and break the loop.
                stack.pop()
            break
        else:
            stack.append(ast)  # If the while loop completes without breaking, append the current asteroid to the stack.

    return stack  # Return the final stack containing surviving asteroids.

asteroids = [10,2,-5]
ans = asteroid(asteroids)
print(ans)

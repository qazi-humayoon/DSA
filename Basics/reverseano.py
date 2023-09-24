# Coding Ninja's Problem :- Printing 32 bit unsigned integer
binary = bin(n)[2:].zfill(32)
return int(binary[::-1],2)


# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

# Example 1:
# Input: x = 123
# Output: 321

MAX_INT = 2 ** 31 - 1 # 2,147,483,647
MIN_INT = -2 ** 31    #-2,147,483,648
reverse = 0

while x != 0:
    if reverse > MAX_INT / 10 or reverse < MIN_INT / 10:
        return 0
    digit = x % 10 if x > 0 else x % -10
    reverse = reverse * 10 + digit
    x = math.trunc(x / 10)

return reverse
        
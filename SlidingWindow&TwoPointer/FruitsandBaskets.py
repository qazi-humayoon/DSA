def totalFruit(arr):
    # Get the length of the input array
    n = len(arr)

    # Dictionary to keep track of the count of each fruit type in the current window
    fruit_count = {}

    # Variable to store the maximum number of fruits in both baskets
    max_fruits = 0

    # Pointer to the left end of the window
    left = 0

    # Iterate through the array using a sliding window
    for right in range(n):
        # Add the current fruit to the fruit_count dictionary
        fruit_count[arr[right]] = fruit_count.get(arr[right], 0) + 1

        # If the number of distinct fruits exceeds 2, move the left pointer to shrink the window
        while len(fruit_count) > 2:
            # Decrease the count of the leftmost fruit in the window
            fruit_count[arr[left]] -= 1

            # If the count becomes zero, remove the fruit from the dictionary
            if fruit_count[arr[left]] == 0:
                del fruit_count[arr[left]]

            # Move the left pointer to the right to shrink the window
            left += 1

        # Update the maximum number of fruits with the current window width
        max_fruits = max(max_fruits, right - left + 1)

    # Return the final result - the maximum number of fruits
    return max_fruits

# Example usage:
arr = [1, 2, 3]
result = totalFruit(arr)
print(result)

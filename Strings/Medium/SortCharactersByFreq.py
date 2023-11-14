# def strings(s):
#     n = len(s)
#     freq = {}
#     for i in s:
#         freq[i] = freq.get(i,0) + 1
#     freq_sort = sorted(freq)
        
#     return freq
        
    
# s = "aAbb"
# ans = strings(s)
# print(ans)

def strings(s):
    # Step 1: Count the frequency of each character
    freq = {}
    for char in s:
        freq[char] = freq.get(char, 0) + 1

    # Step 2: Sort characters based on frequency in descending order
    # Step 1: Get items from the dictionary
    items = freq.items()

    # Step 2: Sort the items based on the second element of each tuple (the frequency)
    sorted_freq = sorted(items, key=lambda x: x[1], reverse=True)
    
    # Step 3: Construct the result string by repeating characters according to their frequency
    result = ''
    for char, count in sorted_freq:
        result += char * count
    
    return result

# Example usage
s = "aAbb"
ans = strings(s)
print(ans)

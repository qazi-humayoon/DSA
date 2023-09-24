from collections import Counter
n = 6
v = [1,2,3,1,1,4]
freq = Counter(v)

    # Initializing variables to determine.
    # Maximum frequency and minimum frequency element.
maxFreq = 0
minFreq = float('inf')
maxElement = 0
minElement = float('inf')
    
    # Traverse through Counter to find the elements.
for element, count in freq.items():
        if count > maxFreq:
            # Found an element with frequency maximum among 
            # all elements found till now.
            maxElement = element
            maxFreq = count
        elif count == maxFreq:
            # Checking if the current element is smaller or not.     
            maxElement = min(maxElement, element)
        
        if count < minFreq:
            # Found an element with frequency minimum among 
            # all elements found till now.
            minElement = element
            minFreq = count
        elif count == minFreq:
            # Checking if the current element is smaller or not.         
            minElement = min(minElement, element)
    
ans = [maxElement, minElement]
print(ans) 

# N = 6
# nums = {1,1,1,2,2,3}
# k = 2
# um = {} # create an empty dictionary to store the count of each number
# n = len(nums) # get the length of the input array
# for i in range(n): # iterate through the array
#     if nums[i] in um: # if the number is already in the dictionary
#             um[nums[i]] += 1 # increment its count by 1
#     else: # if the number is not in the dictionary
#             um[nums[i]] = 1 # add it to the dictionary with a count of 1
# a = [0] * (len(um)) # create a new array with length equal to the number of unique numbers
# j = 0 # initialize a counter
# for i in um: # iterate through the dictionary
#     a[j] = [i, um[i]] # store the number and its count in the new array
#     j += 1 # increment the counter
# a = sorted(a, key = lambda x : x[0], reverse = True) # sort the array in descending order of numbers
# a = sorted(a, key = lambda x : x[1], reverse = True) # sort the array in descending order of counts
# res = [] # create an empty array to store the result
# for i in range(k): # iterate the indices from 0 to k-1
#     res.append (a[i][0]) # append the number at the ith index to the result array
# print(res) # return the

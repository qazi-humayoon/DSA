def uniqueSubstrings(input) :

    n = len(input)
    Set = set()

    ans = 0
    i = 0
    j = 0

    while(i < n and j < n) :
        
        # try to extend the range [i,j]
        if input[j] not in Set :

            Set.add(input[j])
            ans = max(ans, j - i + 1)
            j+=1
        
        else :
            Set.remove(input[i])
            i+=1

    return ans

input =  "abcabcbb"
ans = uniqueSubstrings(input)
print(ans)
# Write a function to find the longest common prefix string 
# amongst an array of strings.

# If there is no common prefix, return an empty string "".

def longest_common_prefix(strs):
    
    res = ""
    
    if not strs:
        return res
    
    for i in range(len(strs[0])):
        for s in strs:
            
            #Checks if we reached the end and if the s[i] which is like flower[i] is not equal to something so like the first
            # letter in a word
            if i == len(s) or s[i] != strs[0][i]:
                return res
            
        res += strs[0][i]
    
    return res
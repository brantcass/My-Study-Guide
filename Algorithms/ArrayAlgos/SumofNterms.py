# Given an array arr[] of size n-1 with distinct integers in the range of [1, n]. 
# This array represents a permutation of the integers from 1 to n with one element 
# missing. Find the missing element in the array.

#  Using Sum of n terms Formula - O(n) Time and O(1) Space

def missingNum(arr):
    n = len(arr) + 1
    
    #calculate the sum of array elements
    total_sum = sum(arr)
    
    #calculate the expected sum 
    exp_sum = n * (n + 1) // 2
    
    #return the missing number
    
    return exp_sum - total_sum

if __name__ == "__main__":
    arr = [8, 2, 4, 5, 3, 7, 1]
    print("The missing number is", missingNum(arr))
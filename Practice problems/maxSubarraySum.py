# Using Kadane's Algorithm - O(n) Time and O(1) Space
# The idea of Kadane's algorithm is to traverse over the array from left 
# to right and for each element,find the maximum sum among all subarrays ending at that element. 
# The result will be the maximum of all these values. 

def max_subarray_sum(arr):
    #stores the result (maximum sum found so far)
    res = arr[0]
    
    # Maximum sum of subarray ending at current position
    maxEnding = arr[0]
    
    for i in range(1, len(arr)):
        
        #Either extend the previous subarray or start
        # new subarray from curr element
        maxEnding = max(maxEnding + arr[i], arr[i])
        
        # Update the result if the new subarray sum is larger
        res = max(res, maxEnding)
        
    return res


if __name__ == "__main__":
    arr = [2, 3, -8, 7, -1, 2, 3]
    print("Maximum contiguous subarray sum is", max_subarray_sum(arr))
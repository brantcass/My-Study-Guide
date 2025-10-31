# Given a sorted array of distinct integers and a 
# target value, return the index if the target is found. 
# If not, return the index where it would be if it were inserted in order.

# You must write an algorithm with O(log n) runtime complexity.

 #BINARY SEARCH must use since we need O(log n) time complexity



def  searchInsert(nums, target):
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2 #using int division since we need an index and it floors value
        if nums[mid] == target: # Best case
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return left

def main():
    nums = [1, 3, 5, 6]

    target = 5
    print(searchInsert(nums, target))  # → 2

    target = 2
    print(searchInsert(nums, target))  # → 1

    target = 7
    print(searchInsert(nums, target))  # → 4

    target = 0
    print(searchInsert(nums, target))  # → 0

main()
    


numbers = [3,2,3, 3, 2, 4, 3, 2, 6, 5]
target = 5


def twoSum(nums, target):
    for i in range(0, len(nums)):
        temp = i
        k = i+1
        li = []
        while k < len(nums) and nums[temp]+nums[k] != target:
            k +=1
            return i, k

print(twoSum(numbers, target))


numbers = [3,2,3, 3, 2, 4, 3, 2, 6, 5]
target = 5


def twoSum(nums, target):
    for i in range(0, len(nums)):
        temp = i
        k = i+1
        li = []
        while k < len(nums):
            if nums[temp]+nums[k] == target:
                li.append(i)
                li.append(k)
                return li
            k +=1

# Approach 2
# def twoSum(nums, target):
#     for indx, num in enumerate(nums[:-1]):
#         for indx2, num2 in enumerate(nums[indx+1:]):
#             if num + num2 == target:
#                 return [indx, indx+indx2+1]


print(twoSum(numbers, target))

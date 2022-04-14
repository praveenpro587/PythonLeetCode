'''Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

'''
#First Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        lst=[]
        for m in range(len(nums)):
            if target - nums[m] in a:
                lst.append(a.get(target-nums[m]))
                lst.append(m)
            else:
                a[nums[m]] = m
        return lst
        
#Second Approach
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=[]
        l=len(lst)
        for i in range(0,l):
            for j in range(i+1,l):
                if lst[i]+lst[j]==t:
                    x.append(i)
                    x.append(j)
        return x

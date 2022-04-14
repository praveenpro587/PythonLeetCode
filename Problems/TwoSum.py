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

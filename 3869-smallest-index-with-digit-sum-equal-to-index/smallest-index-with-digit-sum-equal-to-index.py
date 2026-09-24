class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        ans= -1
        for i in range(len(nums)):
            temp = 0
            while nums[i]>0:
                temp += nums[i] % 10
                nums[i] //= 10
            if i == temp:
                return i
        return ans
        
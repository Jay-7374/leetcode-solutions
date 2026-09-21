class Solution:
    def resultArray(self, nums: List[int], k: int) -> List[int]:
        dp = [0] * k
        ans = [0] * k
        for num in nums:
            curr = [0] * k
            r = num % k
            curr[r] += 1
            for rem in range(k):
                if dp[rem]:
                    new_rem = (rem * r) % k
                    curr[new_rem] += dp[rem]
            dp = curr
            for rem in range(k):
                ans[rem] += dp[rem]
        return ans
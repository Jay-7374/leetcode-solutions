class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:

        import bisect

        n = len(intervals)

        arr = []

        for i in range(n):
            l, r, w = intervals[i]
            arr.append((r, l, w, i))

        arr.sort()

        ends = [x[0] for x in arr]

        dp = [[(0, []) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):

            r, l, w, idx = arr[i - 1]

            for k in range(1, 5):

                dp[i][k] = dp[i - 1][k]

                p = bisect.bisect_left(ends, l)

                prev_weight, prev_indices = dp[p][k - 1]

                take_weight = prev_weight + w
                take_indices = sorted(prev_indices + [idx])

                if take_weight > dp[i][k][0]:
                    dp[i][k] = (take_weight, take_indices)

                elif take_weight == dp[i][k][0]:
                    if take_indices < dp[i][k][1]:
                        dp[i][k] = (take_weight, take_indices)
        ans_weight = 0
        ans = []

        for k in range(1, 5):

            weight, indices = dp[n][k]

            if weight > ans_weight:
                ans_weight = weight
                ans = indices

            elif weight == ans_weight and indices < ans:
                ans = indices

        return ans
class Solution:
    def resultArray(self, nums: List[int], k: int, queries: List[List[int]]) -> List[int]:
        n = len(nums)
        tree = [None] * (4 * n)
        def merge(A, B):
            p1, pre1 = A
            p2, pre2 = B
            p = (p1 * p2) % k
            pre = pre1[:]
            for j in range(k):
                if pre2[j]:
                    r = (p1 * j) % k
                    pre[r] += pre2[j]
            return p, pre

        def build(node, l, r):
            if l == r:
                p = nums[l] % k
                pre = [0] * k
                pre[p] = 1
                tree[node] = (p, pre)
                return
            mid = (l + r) // 2
            build(node * 2, l, mid)
            build(node * 2 + 1, mid + 1, r)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def update(node, l, r, index, value):
            if l == r:
                p = value % k
                pre = [0] * k
                pre[p] = 1
                tree[node] = (p, pre)
                return
            mid = (l + r) // 2
            if index <= mid:
                update(node * 2, l, mid, index, value)
            else:
                update(node * 2 + 1, mid + 1, r, index, value)
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])

        def query(node, l, r, ql):
            if r < ql:
                return None
            if ql <= l:
                return tree[node]
            mid = (l + r) // 2
            left = query(node * 2, l, mid, ql)
            right = query(node * 2 + 1, mid + 1, r, ql)
            if left is None:
                return right
            if right is None:
                return left
            return merge(left, right)

        build(1, 0, n - 1)
        ans = []
        for index, value, start, x in queries:
            update(1, 0, n - 1, index, value)
            result = query(1, 0, n - 1, start)
            ans.append(result[1][x])
        return ans
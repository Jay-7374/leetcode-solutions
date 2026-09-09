class Solution:
    def countCommas(self, n: int) -> int:
        if n < 10**3:
            return 0
        elif n < 10**6:
            return n-999
        elif n < 10**9:
            return (n-999) + (n - 999999)
        elif n < 10**12:
            return (n-999) + (n - 999999) + (n - 999999999)
        elif n< 10**15:
            return (n-999) + (n - 999999) + (n - 999999999) + (n -999999999999)
        else:
            return (n-999) + (n - 999999) + (n - 999999999) + (n -999999999999) + (n - 999999999999999)
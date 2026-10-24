class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        days_sum = []
        temp = 0
        for day in days:
            temp += day
            days_sum.append(temp)
        def convert(date):
            month, d = map(int, date.split('-'))
            return (days_sum[month - 2] if month > 1 else 0) + d
        a1 = convert(arriveAlice)
        l1 = convert(leaveAlice)
        a2 = convert(arriveBob)
        l2 = convert(leaveBob)
        start = max(a1, a2)
        end = min(l1, l2)
        return max(0, end - start + 1)
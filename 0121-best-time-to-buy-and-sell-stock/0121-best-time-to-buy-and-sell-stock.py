class Solution:
    def __init__(self):
        ## YoU can have what ever you want here
        self._work_done = 0
        self.max_profit = 0

    def maxProfit(self, prices: List[int]) -> int:
        if False:
            [sellday, buyday, work] = self._nsquare_time_constant_space(prices)
        if True:
            [sellday, buyday, work] = self._nlogn_time_logn_space(prices)
        if False:
            [sellday, buyday, work] = self._ntime_constant_space(prices)
        print(prices, sellday, buyday)
        p = self._compute_profit(prices, sellday, buyday)
        return p
    
    def _compute_profit(self, a: List[int], s: "int", b: "int") -> "int":
        n = len(a)
        if n == 0:
            return 0
        # assert s >= 0 and s < n
        # assert b >= 0 and b < n
        # assert s >= b
        p = a[s] - a[b]
        return p

    def _nsquare_time_constant_space(self, a):
        maxProfit = 0
        buyday = 0
        sellday = 0

        n = len(a)
        for i in range(0, n-1):
            for j in range(i+1, n):
                self._increment_work_done()
                if a[j]-a[i] > maxProfit:
                    maxProfit = a[j]-a[i]
                    buyday = i
                    sellday = j
                    print(maxProfit)

        print(sellday, buyday, self._work_done)
        return sellday, buyday, self._work_done

    def _ntime_constant_space(self, a):
        if len(a) < 2:
            return 0, 0, 0

        maxProfit = 0
        buyday = sellday = -1
        i = 0
        j = 1

        while j < len(a):
            self._increment_work_done()
            if a[j] - a[i] >= 0 and a[j] - a[i] >= maxProfit:
                maxProfit = a[j] - a[i]
                sellday = j
                buyday = i
            elif a[j] - a[i] < 0:
                i = j
            j += 1

        print(sellday, buyday, self._work_done)
        return sellday, buyday, self._work_done

    def _nlogn_time_logn_space(self, a: List[int]):
        return self._calculate_profit(a, 0, len(a) - 1)

    def _calculate_profit(self, a: List[int], left, right):
        self._increment_work_done()
        if left >= right:
            return left, left, 0

        mid = (left + right) // 2

        left_sell, left_buy, left_profit = self._calculate_profit(a, left, mid)
        right_sell, right_buy, right_profit = self._calculate_profit(a, mid + 1, right)

        left_min = min(a[left:mid + 1])
        right_max = max(a[mid + 1:right + 1])

        cross_profit = right_max - left_min
        left_index = a.index(left_min, left, mid + 1)
        right_index = a.index(right_max, mid + 1, right + 1)

        if left_profit <= cross_profit and right_profit <= cross_profit:
            return right_index, left_index, cross_profit
        if cross_profit <= left_profit and right_profit <= left_profit:
            return left_sell, left_buy, left_profit
        if left_profit <= right_profit and right_profit >= cross_profit:
            return right_sell, right_buy, right_profit
        return left, left, 0
        
    def _increment_work_done(self):
        self._work_done = self._work_done + 1
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        stock = float("inf")
        profit = 0

        for p in prices:
            if p > stock:
                profit += p - stock
            stock = p
        
        return profit
                
                
            

            
        
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        l = 0 #[0]
        r = k

        while r < len(arr) and ((arr[r] == arr[l]) or abs(arr[r]-x) < abs(arr[l]-x)): 
                l+=1
                r+=1
        
        return arr[l:r]



        
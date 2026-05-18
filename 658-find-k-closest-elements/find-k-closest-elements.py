class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        #[1,1,2,2,3,3,4,5]
        l = 0
        r = k-1
        while r < len(arr):
            if r+1 < len(arr) and arr[l] == arr[r+1]:
                l+=1
                r+=1
                continue
            if not r+1 < len(arr) or not abs(arr[r+1]-x) < abs(arr[l]-x):
                return arr[l:r+1]
            l+=1
            r+=1
        
        return arr[l:]
                
            

            




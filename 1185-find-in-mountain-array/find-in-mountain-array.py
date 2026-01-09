# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()
        l = 1
        r = length - 2

        
        while l<=r:
            m = l + ((r-l)//2)
            left, middle, right =  mountainArr.get(m-1), mountainArr.get(m), mountainArr.get(m+1)
            if left > middle > right:
                r = m -1
            elif left < middle < right:
                l = m + 1
            else:
                break
        
        peak = m

        #search left
        l = 0
        r = peak
        while l <= r:
            m = l + ((r-l)//2)
            value = mountainArr.get(m)
            if  value == target:
                return m
            elif target > value:
                l = m + 1
            else:
                r = m - 1

        #search right
        l = peak + 1
        r = length - 1
        while l <= r:
            m = l + ((r-l)//2)
            value = mountainArr.get(m)
            if  value == target:
                return m
            elif target > value:
                r = m - 1
            else:
                l = m + 1
        
        return -1


        

        
        
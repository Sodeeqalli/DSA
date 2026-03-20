class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        greatest = -1

        for i in range(len(arr)-1, -1, -1):
            greatest, arr[i] = max(arr[i], greatest), greatest
        
        return arr
        
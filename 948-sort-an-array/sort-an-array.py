class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def merge(L,M,R,array):
            left,right = array[L:M+1], array[M+1:R+1]
            i,j,k = 0,0,L
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    array[k] = left[i]
                    i+=1
                else:
                    array[k] = right[j]
                    j+=1
                k+=1
            
            while i < len(left):
                array[k] = left[i]
                i,k = i+1, k+1
            
            while j < len(right):
                array[k] = right[j]
                j,k = j+1, k+1
                



        def mergeSort(l,r,arr):
            if l == r:
                return arr
            m = l + ((r-l)//2)
            mergeSort(l,m,arr)
            mergeSort(m+1,r,arr)
            merge(l,m,r,arr)
            return arr

        return mergeSort(0,len(nums)-1, nums)


        
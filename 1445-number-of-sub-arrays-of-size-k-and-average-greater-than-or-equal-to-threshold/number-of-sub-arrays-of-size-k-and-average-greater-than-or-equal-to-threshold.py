class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subSum = 0
        res = 0
        for i in range(k):
            subSum += arr[i]

        l = 0
        for r in range(k, len(arr)):
            average = subSum / k
            if average >= threshold:
                res+=1
            subSum -= arr[l]
            l+=1
            subSum += arr[r]
        
        return res + 1 if (subSum/k) >= threshold else res

        
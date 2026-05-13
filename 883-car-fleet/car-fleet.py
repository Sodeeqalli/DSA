class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        bundled = []
        for p,s in zip(position,speed):
            bundled.append([p,s])

        bundled.sort(reverse = True)

        times = []
        for p,s in bundled:
            timeOfArrival = (target - p) / s
            if times and timeOfArrival <= times[-1]:
                continue
            times.append(timeOfArrival)
        
        return len(times)


            
        
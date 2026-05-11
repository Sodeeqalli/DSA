class Solution:
    def compress(self, chars: List[str]) -> int:
        index = 0
        curr = chars[0]
        count = 1
        
        for i in range(1, len(chars)):
            if chars[i] == curr:
                count += 1
            else:
                chars[index] = curr
                index += 1
                if count > 1:
                    countStr = str(count)
                    for c in countStr:
                        chars[index] = c
                        index += 1
                curr = chars[i]
                count = 1

        chars[index] = curr
        index += 1
        countStr = str(count)
        if count > 1:
            countStr = str(count)
            for c in countStr:
                chars[index] = c
                index += 1

        return index



        
        
        


        

        
        
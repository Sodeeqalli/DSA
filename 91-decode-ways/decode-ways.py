class Solution:
    def numDecodings(self, s: str) -> int:
        #this one is a little tricky icl

        #so say we start at the first number at
        11106
        #when we start we see 1
        #do we need to know the previous number?
        #cause like the second number 1
        #at this point if we know the previous number is 1
        #we can decode as 1,1 or 11
        #say we have like 2 after
        #we can now pass 1 as a previous and 11 as previous
        #then we willl have 1, 1, 2 or 1, 12 or 11, 2
        #but if the previous number is 1 we can always pair
        #if it is 2, we can only pair if the current number is 1-6
        #if it is 3-9 we cannot pair
        #if it current is 0 previous must be 1 or 2 and we cannot continue on the single letter path

        #so lets walk through 06
        #we see 0 is current, if no previous or previous is not 1 or 2, we return 0 ways
        #thats the case here so we simply return 0 as we cannot continue

        #for 226
        #we see 2, no previous so we continue single letter path
        #we see 2 again, previous is 2 so we continue single letter path and a pair letter path
        #we see 6, previous is 2 so we continue single letter path, creates its pair letter path from single letter and continues the pair letter path of the last call.so 3 ways let me attempt the code

        
        n = len(s)
        memo = [None] * n
        def decode(i):
            if i == n:
                return 1
            if s[i] == "0":
                return 0
            if memo[i] != None:
                return memo[i]
            
            if s[i] == "1" and  i+1 < n:
                single = decode(i+1)
                double = decode(i+2)
                memo[i] = single + double
                return memo[i]

            if s[i] == "2" and i+1 < n:
                if int(s[i+1]) < 7:
                    single = decode(i+1)
                    double = decode(i+2)
                    memo[i] = single + double
                    return memo[i]
            
            memo[i] = decode(i+1)
            return memo[i]

        return decode(0)

            









            


        
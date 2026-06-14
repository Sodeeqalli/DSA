class FreqStack:
    #maintain maxfreq
    #create stacks for every frequency
    #maintain frequency of every value

    #1 : [5,7,4]
    #2: [5, 7]
    #3: [5]

    def __init__(self):
        self.freqMap = defaultdict(list) #mapping frequencies to map
        self.maxFreq = 0
        self.valFreq = defaultdict(int)
        

    def push(self, val: int) -> None:
        #when we push, we increase the frequency of that value
        oldFreq = self.valFreq[val]
        newFreq = self.valFreq[val] + 1
        self.maxFreq = max(self.maxFreq, newFreq)
        self.valFreq[val] = newFreq
        self.freqMap[newFreq].append(val)

    def pop(self) -> int:
        val = self.freqMap[self.maxFreq].pop()
        self.valFreq[val] -= 1
        if not self.freqMap[self.maxFreq]:
            self.maxFreq -= 1
        return val

        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
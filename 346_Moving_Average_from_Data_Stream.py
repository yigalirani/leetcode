class MovingAverage:
    def __init__(self, size: int):
        self.size=size
        self.total=0
        self.queue=[0]*size
        self.head=0
        self.sizesofar=0
    def next(self, val: int) -> float:
        last=self.queue[self.head]
        self.queue[self.head]=val
        self.head=(self.head+1)%self.size
        self.total=self.total-last+val
        self.sizesofar+=1
        return self.total/min(self.size,self.sizesofar)

        

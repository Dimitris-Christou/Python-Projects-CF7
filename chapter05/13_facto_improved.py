class FacorIterator:
    def __init__(self, n):
        if n < 0:
            raise ValueError("Factorial in not defined for negative numbers")
        self.n = n
        self.result = 1
        self.order = 0
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.order > self.n:
            raise StopIteration
        
        if self.order == 0:
            # 0! = 1
            self.order +=1
            return 1
        
        self.result *= self.order
        self.order += 1
        return self.result
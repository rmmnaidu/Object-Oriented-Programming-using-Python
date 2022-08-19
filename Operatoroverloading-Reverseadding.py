# Program to illustrate adding on Date Object
def __add__(self, num):
    self.d+= num
    if self.m != 2:
        max_days = Dict[self.m]
    elif self.m == 2:
        isLeap = chk_Leap_Year(self.y)
        if isLeap == 1:
            max_days = 29
        else:
            max_days = 28
    while self.d > max_days:
        self.d -= max_days
        self.m += 1
    while self.m > 12:
        self.m -= 12
        self.y += 1    
            

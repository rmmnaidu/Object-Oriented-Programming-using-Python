# Program to illustrate conversion of class objects
class Distance_m:
    def __init__(self, m):
        self.m = m
    def display(self):
        print("Distance in metres is:", self.m)
def mts(D):
    return D.km*1000
class Distance_km:
    def __init__(self, km):
        self.km = km
    def display(self):
        print("Distance in Kilometres is:", self.km)
def km(D):
    return D.m/1000
Dm = Distance_m(12345)
Dm.display()
print("Distance in Kilometers = ", km(Dm))
Dkm = Distance_km(13.0)
Dkm.display()
print("Distance in meters = ", mts(Dkm))

'''
OUTPUT:
Distance in metres is: 12345
Distance in Kilometers =  12.345
Distance in Kilometres is: 13.0
Distance in meters =  13000.0
'''

        
       

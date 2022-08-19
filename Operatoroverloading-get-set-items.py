# Program that overrides __getitem__() and __setitem__() methods in a class
class myList:
    def __init__(self, List):
        self.List = List
    def __getitem__(self, index):
        return self.List[index]
    def __setitem__(self, index, num):
        self.List[index] = num
    def __len__(self):
        return len(self.List)
    def display(self):
        print(self.List)
L = myList([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("List is:")
L.display()
index = int(input("Enter the index of List you want to access.."))
print(L[index])
index = int(input("Enter the index at which you want to modify.."))
num = int(input("Enter the updated number.."))
L[index] = num
L.display()
print("The length of my List is..",len(L))

'''
OUTPUT:
List is:
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
Enter the index of List you want to access..4
5
Enter the index at which you want to modify..6
Enter the updated number..70
[1, 2, 3, 4, 5, 6, 70, 8, 9, 10]
The length of my List is.. 10
'''

        
       

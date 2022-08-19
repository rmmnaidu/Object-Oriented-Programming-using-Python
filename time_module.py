# Write  a program to display the date and time using Time module.
import time
localtime = time.asctime(time.localtime(time.time()))
print("Local current time:", localtime)
'''
OUTPUT:
Local current time: Fri Jul  1 14:45:21 2022
'''

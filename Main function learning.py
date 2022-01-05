# learning what exactly __name__ == '__main__' is doing..

print("before import")
import math

print("before functionA")
def functionA():
    print("Function A")

print("before functionB")
def functionB():
    print("Function B {}".format(math.sqrt(100)))

print("before __name__ guard")
if __name__ == '__main__':
    functionA()
    functionB()
print("after __name__ guard")

# how I am understanding this is that the __main__ call pulls down the functions to the bottom. it leaves the explicit
# print commands at their appropriate lines. could be wrong on that but just learning it!
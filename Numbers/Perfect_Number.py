#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
"""If a number exactly equals the summary of its proper factor, we call it perfect number. 
Such as 28 = 1 + 2 + 4 + 7 + 14. Write a program and print all perfect number under 1000."""

def isPerfect(N):
    sum = 0
    for i in range(1,N):
        if N%i==0:
            sum +=i
    if N==sum:
        return True
    else:
        return False
    
if __name__ == "__main__":
    print "Perfect number under 1000 as following:"
    for Number in range(1,1001):
        if isPerfect(Number):
            print Number
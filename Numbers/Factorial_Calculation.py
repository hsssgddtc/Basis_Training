#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
"""Input a positive integer n and calculate the result of 1!+2!+3!+......+n!. Use both recursion and loops."""

#function to read integer number from keyboard
def readNumber():
    while(True):
        print  "Please input the N you want to calculate" 
        input_str = raw_input(">")
        if(input_str.isdigit()):
            return int(input_str)
        else:
            print "You need to enter a integer."
            
#Loops Solution
def factorialCalc(N):
    Sum = 0
    for i in range(1,N+1):
        Var = 1
        for j in range(1,i+1):
            Var*=j
        Sum+=Var
    return Sum

#Recursion Solution
def factorialRec(seq):
    if seq==1:
        return 1
    else:
        return seq*factorialRec(seq-1)

def factorialSum(Number):
    Sum=0
    for i in range(1,Number+1):
        Sum+=factorialRec(i)
    return Sum

#Interactive Interface
while(True):
    N = readNumber()
    if N==0:
        break
    else:
        print "The result of 1!+....+%d! is: %d" % (N, factorialSum(N))
    
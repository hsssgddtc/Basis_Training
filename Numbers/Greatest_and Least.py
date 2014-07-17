#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
""" Input two integer m and n, findout their greatest common divisor and least common multiple."""

def readNumber(seq):
    while(True):
        print  "Please input the No.%d value" %seq
        input_str = raw_input(">")
        if(input_str.isdigit()==True):
            return int(input_str)
        else:
            print "You need to enter a number."

def greatestAndLeast(m,n):
    max = m if m>n else n
    min = m if m<n else n
    greatest =  1
    least = m*n
    for i in range(1,min+1):
        if m%i==0 and n%i==0:
            greatest = i
    
    for j in range(max, least):
        if j%m==0 and j%n==0:
            least = j
            break
    
    return greatest,least
    

while(True):
    input_var1 = readNumber(1)   
    input_var2 = readNumber(2)
    if input_var1==0 or input_var2==0:
        break
    else:
        print "The greatest common divisor is %d and least common multiple is %d" % greatestAndLeast(input_var1,input_var2)
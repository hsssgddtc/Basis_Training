#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
""" Develop a converter to convert a decimal number to binary or a binary number to its decimal equivalent."""

def readNumber():
    while(True):
        input_str = raw_input(">")
        if(input_str.isdigit()):
            return int(input_str)
        else:
            print "You need to enter a integer."
            
def binary_to_decimal(N):
    result = 0
    while(N>0):
        for i in range(0,len(str(N))):
            result += pow(2,i) * (N%10)  
            N=N/10
    return result

def decimal_to_binary(N):
    result = []
    while(N>0):
        result.append(str(N%2))
        N=N/2
    result.reverse()
    return ("".join(result))

if __name__ == "__main__":
    while(True):
        print "Choose the calculation:"
        choice = readNumber()
        if choice==0:
            print"Goodbye!"
            break
        elif choice==1:
            print "Enter the binary you want to convert."
            Number = readNumber()
            print "The decimal of binary %d is :%d" % (Number, binary_to_decimal(Number))
        elif choice==2:
            print "Enter the decimal you want to convert."
            Number = readNumber()
            print "The binary of decimal {} is :{}".format(Number, decimal_to_binary(Number))
        else:
            print "Invalid choice!"
#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
"""Narcissistic Numbers, is defined as a three-digits-number, 
summary of each number's cube is the Narcissistic Numbers itself. 
For example, 153 is a Narcissistic Numbers, cause 153 = 1^3 + 5^3 + 3^3. 
Print all Narcissistic Numbers in a column."""

def isNarcissistic(N):
    if N==(pow(N%10,3)+pow(N%100/10,3)+pow(N%1000/100,3)):
        return True
    else:
        return False
    
print "All Narcissistic numbers as following:"
for Number in range(100,1000):
    if(isNarcissistic(Number)):
       print Number
    
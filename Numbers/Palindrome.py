#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
"""Checks if a number entered by the user is a palindrome number. That is that it reads the same forwards as backwards like 1234321."""

def readNumber():
    while(True):
        input_str = raw_input("Enter a number>")
        if(input_str.isdigit()):
            return int(input_str)
        else:
            print "You need to enter a integer."

def isPalindrome(N):
    box = []
    while(N>0):
        box.append(N%10)
        N=N/10
    for i in range(0,box.__len__()/2):
        if box[i] != box[box.__len__()-1-i]:
            return False
    return True

if  __name__ == "__main__":
    while(True):
        Number = readNumber()
        if Number==0:
            print"Goodbye!"
            break
        else:
            print isPalindrome(Number)
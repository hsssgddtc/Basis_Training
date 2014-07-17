
#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
Pi = 3.1415926    #define constant Pi

#function to read number from keyboard
def readNumber(seq):
    while(True):
        print  "Please input the No.%d value" %seq
        input_str = raw_input(">")
        if(input_str.isdigit()==True):
            input_var = float(input_str)
            break;
        else:
            print "You need to enter a number."
    return input_var


input_var1 = readNumber(1)   #assign input value to the 1st variable
input_var2 = readNumber(2)
input_var3 = readNumber(3)

#1. Find out the area of three circles. Print in one column and make the decimal point align. Keep 3 digits.
print "\n#1.The area of 3 circles are:\n{0:10.3f}\n{1:10.3f}\n{2:10.3f}\n".format(Pi*pow(input_var1,2),Pi*pow(input_var2,2),Pi*pow(input_var3,2))
#print "%10.3f \n%10.3f \n%10.3f".rjust(10) %(Pi*pow(input_var1,2), Pi*pow(input_var2,2), Pi*pow(input_var3,2))

#2. Find out the circle with maximum area, round-up and print its area.
bigger_radius = input_var1 if input_var1>input_var2 else input_var2
max_radius =  input_var3 if input_var3>bigger_radius else bigger_radius
print "#2.The area of maximum circle is:%d \n" % (Pi*pow(max_radius,2))

#3. Print the area of three circles in descent orders.
middle_radius = input_var3 if input_var3 < bigger_radius else bigger_radius
smaller_radius = input_var1 if input_var1<input_var2 else input_var2
min_radius =  input_var3 if input_var3<smaller_radius else smaller_radius
print "#3.The area of 3 circles in descent order: %f \n%f \n%f\n" %(Pi*pow(max_radius,2), Pi*pow(middle_radius,2), Pi*pow(min_radius,2))

""""4. Set the height of cylinder h=3.6, bottom radius is the radius of the circle with minimum area. 
Try to find out the circumference and cylindrical volume. Print out them with description and keep 2 digits."""
h=3.6
print "#4.The circumference of bottom is: %f" % (2*Pi*min_radius)
print "The volume of cylindrical is: %f" % (Pi*pow(min_radius,2)*h)
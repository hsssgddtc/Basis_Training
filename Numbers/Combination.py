#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
""" We have numbers 1,2,3,4. How many different three-digit numbers can they combined without duplicate digits? Print them all."""

Numbers = [1,2,3,4]
Combination = []
Sum = 0

for i in range(1,Numbers.__len__()+1):
  for j in range(1,Numbers.__len__()+1):
      for k in range(1,Numbers.__len__()+1):
          if(i!=j and j!=k and k!=i):
              Combination.append("{}{}{}".format(i,j,k))  
              Sum += 1
          
print "There are {} combinations as following:{}".format(Sum,Combination)
    
#print "{}{}{}".format(a,b,c)
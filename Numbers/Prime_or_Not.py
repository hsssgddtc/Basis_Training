#This is the solution under Numbers category for project https://github.com/hsssgddtc/Basis-Training
"""For the number between 101 and 200. Judge if it's prime number or not. If not, print all its positive divisor."""

def isPrime(Number):
	divisor = []
	for i in range(2,Number):
		if Number%i==0:
			divisor.append(i)
	if divisor.__len__()==0:
		return True
	else:
		return divisor
	
for i in range(101,201):
	result = isPrime(i)
	if result==True:
		print"%d is a Prime Number." % i
	else:
		print"{} is not a Prime Number.Its positive divisor as following: {}".format(i,result)
	
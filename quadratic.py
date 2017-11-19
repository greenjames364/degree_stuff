#
#Program takes quadratic equation, determines type of solution (no of roots) and calculates solution
#

#	
#Main block takes inputs from user and applies quad_solv function
#
def main():
	#Call for inputs from user
	print ("To solve the quadratic equation 'ax^2 + bx + c = 0', please enter the following")
	a = int(input("The value for a:"))
	b = int(input("The value for b:"))
	c = int(input("The value for c:"))
	
	quad_solv(a,b,c)


def quad_solv(a,b,c):
	"""
	Solves a quadratic equation in the form 'ax^2 + bx + c = 0'
	Solver prints the results and returns (discriminant, 1st root, 2nd root (where applicable))
	
	>>> quad_solv(1,4,5)
	Equation has two complex roots
	Root 1: (-2+1j)
	Root 2: (-2-1j)
	(-4, (-2+1j), (-2-1j))
	
	>>> quad_solv(0,4,3)
	Equation has single solution: x = -0.75
	-0.75
		
	"""	
	
	# Import sqrt funcitons from math and cmath
	from math import sqrt
	from cmath import sqrt as csqrt
	
	#Check inputs and deal with outliers 
	if a==b==0:
		if c!=0:
			print ("Not a valid equation")
			return()
		else:
			print ("Not interesting enough")
			return()
	if a==0:
		x1=-c/b
		print ("Equation has single solution: x =", x1)
		return(x1)
	
	#Calculate discriminant
	discr = b**2 - (4 * a * c )


	#Determine no of roots and calculate roots

	if discr > 0:
		x1 = ( -b + sqrt(discr))/ (2 * a)
		x2 = ( -b - sqrt(discr))/ (2 * a)
		print("Equation has two real roots")
		print("Root 1: " + str(x1))
		print("Root 2: " + str(x2))
		return (discr, x1, x2)

	elif discr == 0:
		x1 = ( -b + sqrt(discr))/ (2 * a)
		print("Equation has one real root")
		print("Root 1: " + str(x1))
		return (discr, x1)

	elif discr < 0:	
		x1 = ( -b + csqrt(discr))/ (2 * a)
		x2 = ( -b - csqrt(discr))/ (2 * a)
		print("Equation has two complex roots")
		print("Root 1: " + str(x1))
		print("Root 2: " + str(x2))
		return(discr, x1, x2)

	else:
		print("Something has gone horribly wrong.....")
		
		
if __name__ == "__main__": main()
	#import doctest
	#doctest.testmod()

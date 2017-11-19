import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import math as m
import cmath as cm


def main():
	while True:
		try:
			degree = int(input("Enter degree of polynominal: "))
		except ValueError:
			print("Please enter an integer")
			continue
		else: break
		
	while True:
		try:
			poly_coefs = [int(x) for x in input("Enter coefficients: ").split()]
		except ValueError:
			print("Please enter numbers only, seperated by a space")
			continue
		if len(poly_coefs) == degree+1:
			break
		else:
			print("Number of coeffeicients must equal degree + 1")
			continue
			
	while True:
		try:
			bLcorner = complex(input("Enter bottom left corner of the box: "))
		except ValueError:
			print("Please enter a complex number")
			continue
		else: break
		
	while True:
		try: width = int(input("Enter width of box: "))
		except ValueError:
			print ("Please enter an integer")
			continue
		else: break
		
	while True:
		try: numPix = int(input("Enter number of pixels of image: "))
		except ValueError:
			print("Please enter an inter")
			continue
		else: break
		
	
	
	data = newton_fractal(degree, poly_coefs, bLcorner, width, numPix)
	limits = [bLcorner.real, bLcorner.real+width, bLcorner.imag, bLcorner.imag+width]
	plt.pyplot.imshow(data, origin='upper', extent=limits)
	plt.pyplot.show()
	
def newton(poly_coefs, z0):
	"""
	This function takes in polynomial coefficients and starting point z0, and return the root and
	the number of iterations it performed
	>>> newton([-1, 0, 0, 1],complex(-1-1j))
	((-0.5-0.8660254037844386j), 6)
	"""
	
	h = 1e-10
	f= np.poly1d(poly_coefs)
	fDer = np.polyder(f)
	iterations = 0
	zN = z0
	zN1 = complex(-0-0j)
	while True:
		zN1 = zN - (f(zN)/fDer(zN))
		iterations = iterations + 1
		if abs(zN - zN1) < h: break
		if iterations > 1000: break
		zN = zN1
		

	return (zN1, iterations)
	
	

def newton_fractal(degree, poly_coefs, bLcorner, width, numPix):
	"""
	polynomial coefficients, number of pixels (width), corner of your square complex (z0),
	width, and whether to shade the image
	Calls the newton function, goes through the grid of the desired square in complew plane
	Finds root for each point
	Produces shaded or unshaded image of fractal
	"""
	
	
	row = np.linspace(bLcorner.real , bLcorner.real+ width, num = numPix)
	column =  np.linspace(bLcorner.imag+width, bLcorner.imag, num = numPix)
	
	A = []
	root_list = []
	colour_list = np.array([[0,0,1],[1,0,0],[0,1,0.2],[1,0.5,0],[0,1,0.5],[0.8,0,1]])
	for l in column:
		for k in row:
			colourUsed = False
			root, iterations = newton(poly_coefs, complex(k,l))
			for i in range(0,len(root_list)):
				if abs(root - root_list[i]) < 1e-2:
					A.append([colour_list[i,0],colour_list[i,1], colour_list[i,2]])
					colourUsed = True
			if colourUsed == False:
				root_list.append(root)
				
				A.append([colour_list[len(root_list)-1,0],colour_list[len(root_list)-1,1], colour_list[len(root_list)-1,2]])

	A = np.array(A)
	A = A.reshape(numPix,numPix,3)
	return A
	
	
	
	
	
	
	
if __name__ == "__main__":
	import doctest
	doctest.testmod()
	main()
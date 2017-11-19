import numpy as np
import matplotlib as plt
from matplotlib import pyplot
import math as m
import cmath as cm


def main():
	"""
	MAIN BLOCK
	Calls for inputs from user and passes them to the newton_fractal function
	Then outputs returned 3D matrix as an image
	
	"""
	
	# Passes inputs for a given fractal
	my_frac = input("If you would like to see my fractal, not make your own, enter 'y': ")
	if my_frac == 'y':
		degree = 8 
		poly_coefs = [1, 0, 0, 2, 3, 2, 0, 0, 1] 
		bLcorner = complex(-1-1j)
		width = 2
		print("Function input as: ")
		print( np.poly1d(poly_coefs))
	
	#
	#Takes inputs from user and checks them all if user wants to make own fractal
	#
	else:
		while True:
			try:
				degree = int(input("Enter degree of polynominal: "))
			except ValueError:
				print("Please enter an integer")
				continue
			if degree > 8:
				print("Max degree = 8")
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
		
	x = input("Shaded? [y/n]: ")
	if "y" in x:
		shaded = True
	else: shaded = False
	
	#
	#Passes inputs to newton_fractal function
	#
	print("-- Generating fractal. Please be patient...")
	data, root_list = newton_fractal(degree, poly_coefs, bLcorner, width, numPix, shaded)
	print ("-- Found roots: " + str(root_list))
	
	#
	#Creates image from newton_fractal's 3D array outputs
	#
	limits = [bLcorner.real, bLcorner.real+width, bLcorner.imag, bLcorner.imag+width]
	plt.pyplot.imshow(data, origin='upper', extent=limits)
	
	#Label image and save
	plt.pyplot.xlabel("Re(z)")
	plt.pyplot.ylabel("Im(z)")
	filename = input("Enter filename to save fractal image: ")
	plt.pyplot.savefig(filename)
	print ("-- Saved file: " + filename)
	
	
def newton(poly_coefs, z0, iterLim):
	"""
	This function takes in polynomial coefficients and starting point z0, and return the root and
	the number of iterations it performed
	>>> newton([-1, 0, 0, 1],complex(-1-1j), 1000)
	((-0.5-0.8660254037844386j), 6)
	"""
	#
	#Setup variables
	#
	h = 1e-10 #Tolerance value
	f= np.poly1d(poly_coefs) #Function
	fDer = np.polyder(f) #Derivative of function
	iterations = 0
	zN = z0
	zN1 = complex(-0-0j)
	
	#
	# Calculate root using Newton Raphson
	#
	while True:
		zN1 = zN - (f(zN)/fDer(zN)) #Newton Raphson function
		iterations = iterations + 1
		if abs(zN - zN1) < h: 		#See if within tolerance
			return zN1, iterations
			break
		elif iterations > iterLim:	#Stops calc if iterations get too big
			return 0, iterations	#Returns 0. This will be coloured black later
			break
		else:
			zN = zN1				#Setup for next iteration
 
	

def newton_fractal(degree, poly_coefs, bLcorner, width, numPix, shaded):
	"""
	Calculates the 3d array required to make an image of the fractal
	Inputs the polynomial coefficients, corner of your square, number of pixels, width,
	and whether to shade the image
	Calls the newton function, goes through the grid of the desired square in complex plane
	Finds root for each point
	Adds shaded or unshaded colour to list for array
	
	"""
	
	#Setup axes
	row = np.linspace(bLcorner.real , bLcorner.real+ width, num = numPix)
	column =  np.linspace(bLcorner.imag+width, bLcorner.imag, num = numPix)
	
	#Iteration limit for newton func
	iterLim = 1000
	
	#Set up items
	imageData= []
	root_list = []
	colour_list =[[0,0,1],[1,0,0],[0,1,0.2],[1,0.5,0],[0,1,0.5],[0.8,0,1],[0.5,1,0],[1,0,0.5],[0.5,0.5,0.5],[0.2,1,0.2],[0.8,0.2,0.6]]
	
	#Nested for loop used to iterated through every point in complex plane
	for l in column:
		for k in row:
			colourUsed = False #reset after each point
			
			#Run newton on each point
			root, iterations = newton(poly_coefs, complex(k,l), iterLim)
			
			if root == 0: #This is only when iterations took too long, colour set to black
				imageData.append([0,0,0])
			
			else:
				for i in range(0,len(root_list)): 
					if shaded == True:
						#If root is in the root list, use root's colour (rounded to eliminate small decimal changes)
						if abs(round(root*1e6)-(root_list[i]*1e6)) < 0.5: 
							imageData.append([i * (1-iterations/iterLim*100) for i in colour_list[i]])
							colourUsed = True
					elif abs(round(root*1e6)-(root_list[i]*1e6)) < 0.5: 
						imageData.append(colour_list[i]) 
						colourUsed = True
				if colourUsed == False: #Will be new root
					if shaded == True:
						root_list.append((round(root*1e6))/1e6)
						imageData.append([i * (1-iterations/iterLim*100) for i in colour_list[len(root_list)-1]])
					else:
						root_list.append((round(root*1e6))/1e6)
						imageData.append(colour_list[len(root_list)-1])
	
	#Turn imageDatainto array and reshape into 3D array for imshow
	imageData = np.array(imageData) 
	imageData = imageData.reshape(numPix,numPix,3)
	return imageData, root_list
	
if __name__ == "__main__":
	import doctest
	doctest.testmod()
	main()
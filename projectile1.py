import numpy as np
import math as m
import matplotlib.pyplot as plt

def main():
	vX = 30 #input("Enter the initial speed [m]:")
	y0 = 10 #input("Enter the height [m/s]:")
	g = 9.8
	
	theta = np.arange(m.pi/18, m.pi/2, m.pi/18)
	t = np.linspace(0, 10, num=2000)
	
	d1 =[]
	h1 =[]
	tRun1 =[]
	
	for i in theta:
		x1 = []
		y1 = []
		
		y=y0
		for k in t:
			x = ((vX*k)*np.cos(i))
			y = (y0 + (vX*k)*np.sin(i))-((g/2) * k**2)
			x1.append(x)
			y1.append(y)
		p = [i for i, j in enumerate(y1) if j < -0] # Don't fall through the floor
		for i in sorted(p, reverse=True):
			del x1[i]
			del y1[i]
		d1.append(max(x1))x
		h1.append(max(y1))
		
		#tRun1.append(0) #What to do here.....
		
		plt.plot(x1,y1)
	
	plt.title("Trajectories")
	plt.xlabel("Downrange distance [m]")
	plt.ylabel("Height [m]")
	hMax = (max(h1) + 9) // 10 * 10
	plt.ylim(0,hMax)
	
	
	#plt.show()
	output(theta, d1, h1, tRun1)
	
def output(ang, d, h, t):
	print("Angle [deg] Distance [m] Max height [m] Travel time [s]")
	print("-------------------------------------------------------")
	for i in range(0,len(ang)):
		print (str(round(ang[i]*180/m.pi)) + "     " + str(round(d[i])) + "      " + str(round(h[i])) + "      " + str(round(t[i])))
	
	
if __name__ == "__main__":
	main()
	import doctest
	doctest.testmod()
	
	
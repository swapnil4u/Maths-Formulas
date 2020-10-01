from math import pi 

radius = int(raw_input("Enter the radius : "))

def volume_of_sphere(radius):
	volume = 4/3 * pi * (radius **3)
	return "Volume of Sphere is %s" % (volume)

print volume_of_sphere(radius)

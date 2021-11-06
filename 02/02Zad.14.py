#####
# Calculation of the area and circumference of a circle
##

# determine radius and PI
r =input("Podaj promien: ")
pi=3.14


# calculate area 
pole=pi*int(r)**2

# calculate circumference 
obwod= 2*pi*int(r)

# display results 
print(pole)
print(obwod)
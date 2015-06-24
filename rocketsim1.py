import numpy as np
#initialize 3 lists
accel=list()
vel=list()
x=list()
ge=list()
gm=list()

#define constants as variables (g, mi)
g = 6.674*10**(-11)
moon = 7.347*10**(22)
earth = 5.972*10**(24)
leo = 6531
dtotal = 392508000
mi = 5200
fuelbr = 1.16*10**(-2) #This is the rate at which our rocket expends fuel in kg/s.
thrust = 10**8
vi = 11200

x.extend([160000])

gei = g*earth*mi/(x[0])**2
gmi = g*moon*mi/(dtotal-x[0])**2

accel.extend([0])
vel.extend([vi])
ge.extend([gei])
gm.extend([gmi])

#define dt, general unit of time for program
dt = 0.1 #0.1 seconds

#initialize time list and fill
time = list(np.arange(0,40,dt))

#define position, velocity, acceleration, and time dependent quantities
##for i in time:
##    mr = mi - fuelbr*i#This is the mass of the rocket as time goes on
##    a = (g*moon*mr + g*earth*mr )/mr
##    v = accel*i
##    x = vel*i

#begin to fill 3 main lists


#define functions and call in for loop for 400000 dt


#detect index of timestamp when velocity and acceleration are at zero. take this quantity and print it

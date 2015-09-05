import numpy as np
#initialize 3 lists
accel=list()
vel=list()
x=list()
ge=list()
gm=list()

#define constants as variables (g, mr)
g = 6.674*10**(-11)
moon = 7.347*10**(22)
earth = 5.972*10**(24)
leo = 6531
dtotal = 392508000
mr = 5200
fuelbr = 1.16*10**(-2) #This is the rate at which our rocket expends fuel in kg/s.
tr = 4.4*10**8
vi = 11200

#Here, we set the initial values and conditions
x.extend([160000])

gei = g*earth*mr/(x[0])**2
gmi = g*moon*mr/(dtotal-x[0])**2
a0 = (tr-gei+gmi)/mr

accel.extend([a0])
vel.extend([vi])
ge.extend([gei])
gm.extend([gmi])

#define dt, general unit of time for program
dt = 0.001 #0.1 seconds

#initialize time list and fill
time = list(np.arange(0,400,dt))

#define position, velocity, acceleration, and time dependent quantities
for i in range(1,len(time)+1):
    #Here we find the next position
    
    vnew=vel[i-1]+accel[i-1]*dt
    vel.extend([vnew])
    xnew=x[i-1]+vel[i-1]*dt
    x.extend([xnew])
    genew=g*earth*mr/(x[i])**2
    ge.extend([genew])
    gmnew=g*moon*mr/(dtotal-x[i])**2
    gm.extend([gmnew])
    accelnew=(tr+gm[i]-ge[i])/mr
    accel.extend([accelnew])
    
    #detect index of timestamp when velocity and acceleration are at zero. take     this quantity and print it
    timefinal=time[i]
    velfinal=vel[i]
    xfinal=x[i]
    accelfinal=accel[i]
    if x[-1]>dtotal:
        print"time=", timefinal
        print
        print"position=", xfinal
        print
        print"vel=", velfinal
        print
        print"accel=", accelfinal
        print
        break
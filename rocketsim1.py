import numpy as np
#initialize 3 lists
accel=list()
vel=list()
x=list()
ge=list()
gm=list()
mt=list() #this is list holding mass of wet rocket at given points in time

#define constants as variables (g, mr)
g = 6.674*10**(-11)
moon = 7.347*10**(22)
earth = 5.972*10**(24)
leo = 6531
dtotal = 392508000
md = 5200 #initial mass of dry rocket
mf = 52000 #initial mass of fuel
fuelbr = 0.001
tr = 4.4*10**8
vi = 11200

#Here, we set the initial values and conditions
x.extend([160000])
mt.extend([md+mf])

gei = g*earth*mt[0]/(x[0])**2
gmi = g*moon*mt[0]/(dtotal-x[0])**2
a0 = (tr-gei+gmi)/mt[0]

accel.extend([a0])
vel.extend([vi])
ge.extend([gei])
gm.extend([gmi])

#define dt, general unit of time for program
dt = .1 #0.1 seconds

#initialize time list and fill
time = list(np.arange(0,900,dt))

#define position, velocity, acceleration, and time dependent quantities
for i in range(0,len(time)):
    #Here we find the next position
    
    mtnew=md+(mf-fuelbr*dt)
    mt.extend([mtnew])
    vnew=vel[i]+accel[i]*dt
    vel.extend([vnew])
    xnew=x[i]+vel[i]*dt
    x.extend([xnew])
    genew=g*earth*mt[i]/(x[i])**2
    ge.extend([genew])
    gmnew=g*moon*mt[i]/(dtotal-x[i])**2
    gm.extend([gmnew])
    accelnew=(tr+gm[i]-ge[i])/mt[i]
    accel.extend([accelnew])
    
    print"these are our times:", time[-1]
    print""
    print"these are our masses:", mt[-1]
    print""
    print"these are our positions:", x[-1]
    print""
    print"these are our velocities:", vel[-1]
    print""
    print"these are our accelerations:", accel[-1]
    print""
    print"this is the total distance to the moon:", dtotal
    print""
    print""
    print""
    
    #detect index of timestamp when position is larger than the total distance between the moon and earth
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
        print"you made it to the moon"
        break
    
    elif x[-1]<dtotal:
        print"Haven't made it yet"

    if vel[-1]<0:
        print"you're dead"
        break
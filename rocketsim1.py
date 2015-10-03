import numpy as np
import matplotlib.pyplot as plt
#initialize 3 lists
accel=list()
vel=list()
x=list()
ge=list()
gm=list()
mt=list() #this is list holding mass of wet rocket at given points in time

#define constants as variables (g, mr)
g = 6.674*10**(-11) #N(m/kg)^2
moon = 7.347*10**(22) #kg, mass of moon
earth = 5.972*10**(24) #kg, mass of earth
radearth = 6371000 #meters
radmoon = 170000 #meters
semimajoraxis = 384403000 #meters
leo = 160000 #meters
dtotal = radearth + radmoon + semimajoraxis
md = 5200 #initial mass of dry rocket kg
mf = 52000 #initial mass of fuel kg
fuelbr = 1000 #kg/s
tr = 10**6 #Newtons
vi = 0 #m/s

#Here, we set the initial values and conditions
x.extend([radearth + leo])
mt.extend([md+mf])

gei = g*earth/(x[0])**2
gmi = g*moon/(dtotal-x[0])**2
a0 = (tr)/mt[0]-gei+gmi

accel.extend([a0])
vel.extend([vi])
ge.extend([gei])
gm.extend([gmi])

#define dt, general unit of time for program
dt = .1 #0.1 seconds

#initialize time list and fill
time = list(np.arange(0,10**5,dt))

#define position, velocity, acceleration, and time dependent quantities
for i in range(0,len(time)):
    #Here we find the next position
    
    if mt[-1] > md:
        mtnew=mt[-1]-fuelbr*dt
        mt.extend([mtnew])
    elif mt[-1]<= md:
        print"you ran out of gas, be careful"
        mt.extend([md])## Added by Aleks to prevent fuel burn overruns
    vnew=vel[i]+accel[i]*dt
    vel.extend([vnew])
    xnew=x[i]+vel[i]*dt
    x.extend([xnew])
    genew=g*earth/(x[i])**2
    ge.extend([genew])
    gmnew=g*moon/(dtotal-x[i])**2
    gm.extend([gmnew])
    accelnew=(tr)/mt[i]+gm[i]-ge[i]
    accel.extend([accelnew])
        #
    # print"length of times:", len(time)
    # print""
    # print"length of masses:", len(mt)
    # print""
    # print"Length of positions:", len(x)
    # print""
    # print"Length of velocities:", len(vel)
    # print""
    # print"Length of accelerations:", len(accel)
    # print gm[i]
#     print mt[i]
#     print ge[i]
    
    #detect index of timestamp when position is larger than the total distance between the moon and earth
    timefinal=time[i]
    velfinal=vel[i]
    xfinal=x[i]
    accelfinal=accel[i]
    etime=time[0:len(mt)]
    etime1=time[0:len(x)]
    etime2=time[0:len(vel)]
    etime3=time[0:len(accel)]
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
        print"you're dead. You stopped moving forward"
        break
        
# Start to draw plots of mass, velocity, acceleration, and position.
# fig=
plt.plot(etime, mt, linestyle='-', color='r', label='Mass')
# plt.axis([0, (max(etime)), 0, (max(mt))])
plt.title("Mass of rocket over time:")
plt.margins(0.1)
plt.xlabel("Time (.1 seconds)")
plt.ylabel("Mass (KG)")
plt.legend(loc="best")
plt.show()
# fig.savefig('mass.png')

# fig1=
plt.plot(etime1, x, linestyle='-', color='r', label='Position')
plt.title("Position of Rocket over time:")
plt.margins(0.1)
plt.xlabel("Time (.1 seconds)")
plt.ylabel("Position")
plt.legend(loc="best")
plt.show()
# fig1.savefig('position.png')

# fig2=
plt.plot(etime2, vel, linestyle='-', color='r', label='Velocity')
plt.title("Velocity of Rocket over time:")
plt.margins(0.1)
plt.xlabel("Time (.1 seconds)")
plt.ylabel("Velocity")
plt.legend(loc="best")
plt.show()
# fig2.savefig('velocity.png')

# fig3=
plt.plot(etime3, accel, linestyle='-', color='r', label='Acceleration')
plt.title("Acceleration of Rocket over time:")
plt.margins(0.1)
plt.xlabel("Time (.1 seconds)")
plt.ylabel("Acceleration")
plt.legend(loc="best")
plt.show()
# fig3.savefig('acceleration.png')
import matplotlib.pyplot as plt
x=[0,1,2,3,4,5,6,10]
y=[0,1,4,8,16,25,36,100]
plt.plot(x,y,marker='o', linestyle='-', color='r', label='Rocket Velocity')
# plt.axis([0, 6, 0, 36])
plt.title("y=x^2")
plt.margins(0.1)
plt.xlabel("label")
plt.ylabel("otherlabel")
plt.legend(loc="best")
plt.show()
import numpy as np
import matplotlib.pyplot as plt

plt.figure(1)
plt.ion()
#plt.hold(False)

#State=np.array([[1.0,1.0]])

Up=np.array([0.0,1.0])
Down=np.array([0.0,-1.0])
Right=np.array([1.0,0.0])
Left=np.array([-1.0,0.0])

Actions=np.array([Up,Right,Down,Left])
Goal=np.array([[19.0,19.0]])
XBarriers=np.append([np.linspace(0,20,21)],[[np.zeros(21)],[np.linspace(0,20,21)],[np.zeros(21)+20]])
YBarriers=np.append([np.zeros(21)],[[np.linspace(0,20,21)],[np.zeros(21)+20],[np.linspace(0,20,21)]])

Barriers=[[0,0]]
i=0
while (i<np.prod(YBarriers.shape)):
    Barriers=np.vstack((Barriers,[XBarriers[i],YBarriers[i]]))
    i=i+1

PotentialState=[[0,0]]

plt.plot(State[0][0],State[0][1],'ro')
#plt.hold(True)
plt.plot(Goal[0][0],Goal[0][1],'bo')
plt.plot(Barriers[:,0],Barriers[:,1],'ko')
plt.axis([-1,21,-1,21])
plt.draw()

while(1):
    Done=False
    Bad=True
    Check=0
    while not Done and Bad:
        p1=State[0][0]
        p2=State[0][1]
        p3=Actions[Check][0]
        p4=Actions[Check][1]
        PotentialState[0][0]=p1+p3
        PotentialState[0][1]=p2+p4
        Done=(Goal==State).all(1).any()


plt.ioff()
plt.show()

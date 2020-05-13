import numpy as np
import matplotlib.pyplot as plt
import random

plt.figure(1)
plt.ion()


State=np.array([[1.0,1.0]])

Up=np.array([0.0,1.0])
Down=np.array([0.0,-1.0])
Right=np.array([1.0,0.0])
Left=np.array([-1.0,0.0])

Actions=np.array([Up,Right,Down,Left])
Goal=np.array([[10.0,10.0]])
XBarriers=np.append([np.linspace(0,20,21)],[[np.zeros(21)],[np.linspace(0,20,21)],[np.zeros(21)+20]])
YBarriers=np.append([np.zeros(21)],[[np.linspace(0,20,21)],[np.zeros(21)+20],[np.linspace(0,20,21)]])

Barriers=[[0,0]]
i=0
while (i<np.prod(YBarriers.shape)):
    Barriers=np.vstack((Barriers,[XBarriers[i],YBarriers[i]]))
    i=i+1

Barriers=np.vstack((Barriers,[[1,8],[2,8],[3,8],[4,8],[5,8],[6,8],[7,8]]))
PotentialState=[[0,0]]

plt.plot(State[0][0],State[0][1],'ro')
plt.plot(Goal[0][0],Goal[0][1],'bo')
plt.plot(Barriers[:,0],Barriers[:,1],'ko')
plt.axis([-1,21,-1,21])
plt.draw()


Barriers=np.vstack((Barriers,State))
Moves=0
while(1):
    Done=False
    Bad=True
    #Check=0
    Check=random.choice([0,1,2,3])
    while not Done and Bad:
        p1=State[0][0]
        p2=State[0][1]
        p3=Actions[Check][0]
        p4=Actions[Check][1]
        PotentialState[0][0]=p1+p3
        PotentialState[0][1]=p2+p4
        Done=(Goal==State).all(1).any()
        Bad=(Barriers==PotentialState).all(1).any()
        #Check=Check+1
        Check=random.choice([0,1,2,3])
        if Check==4 and Bad:
            print('Stuck')
            break
        
    State[0][0]=p1+p3
    State[0][1]=p2+p4
    if Done:
        print('Goal achieved in ',Moves,'moves')
        break

    Moves=Moves+1
    print('State',State)
    plt.plot(State[0][0],State[0][1],'ro')
    plt.plot(Goal[0][0],Goal[0][1],'bo')
    plt.plot(Barriers[:,0],Barriers[:,1],'ko')
    plt.axis([-1,21,-1,21])
    plt.draw()
    plt.pause(0.1)
    plt.clf()

    Barriers=np.vstack((Barriers,State))



plt.ioff()
plt.show()

import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

fig=plt.figure()
ax=fig.add_subplot(111,projection='3d')

Color=np.array([1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3])
Sides=np.array([4,4,3,3,1,1,4,4,3,3,1,1,4,4,3,3,1,1])
Size=np.array([2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1])

Seed1=np.array([1,4,2]) #seed 1 is the big red square
Seed2=np.array([3,4,1]) #Seed 2 is the little blue circle



runs=0
while(runs<3):
	Seed1_Members_Color=[]
	Seed1_Members_Sides=[]
	Seed1_Members_Size=[]

	Seed2_Members_Color=[]
	Seed2_Members_Sides=[]
	Seed2_Members_Size=[]

	i=0
	while(i<np.prod(Color.shape)):

		dist_from_Seed1=np.sqrt((Color[i]-Seed1[0])**2+(Sides[i]-Seed1[1])**2+(Size[i]-Seed1[2])**2)
		dist_from_Seed2=np.sqrt((Color[i]-Seed2[0])**2+(Sides[i]-Seed2[1])**2+(Size[i]-Seed2[2])**2)

		if (dist_from_Seed1<dist_from_Seed2):
			Seed1_Members_Color=np.append(Seed1_Members_Color,[Color[i]])
			Seed1_Members_Sides=np.append(Seed1_Members_Sides,[Sides[i]])
			Seed1_Members_Size=np.append(Seed1_Members_Size,[Size[i]])
		else:
			Seed2_Members_Color=np.append(Seed2_Members_Color,[Color[i]])
			Seed2_Members_Sides=np.append(Seed2_Members_Sides,[Sides[i]])
			Seed2_Members_Size=np.append(Seed2_Members_Size,[Size[i]])

		i=i+1

	Seed1=np.array([np.mean(Seed1_Members_Color),np.mean(Seed1_Members_Sides),np.mean(Seed1_Members_Size)])
	Seed2=np.array([np.mean(Seed2_Members_Color),np.mean(Seed2_Members_Sides),np.mean(Seed2_Members_Size)])
	print('Seed1 = ',Seed1)
	print('Seed2 = ',Seed2)
	runs=runs+1


#ax.scatter(Color,Sides,Size)

ax.scatter(Seed1_Members_Color,Seed1_Members_Sides,Seed1_Members_Size,c='b')
ax.scatter(Seed2_Members_Color,Seed2_Members_Sides,Seed2_Members_Size,c='r')

ax.set_xlabel('Color')
ax.set_ylabel('Sides')
ax.set_zlabel('Size')

plt.show()
import numpy as np

rootLink=np.array([0.5,0,.05])
rootJoint=np.array([1,0,1])
links=[rootLink]
joints=[rootJoint]
for i in range(3):
    if i%2==0:
        links.append(links[-1]+np.array([1,0,1]))
    else:
        links.append(links[-1]+np.array([1,0,-1]))
    joints.append(np.array([1,0,0]))

print("links=",links)
print("joints=",joints)

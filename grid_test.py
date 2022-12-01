from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
from grid import g_grid,v_grid

fig = plt.figure()


ax = plt.axes(projection='3d')


n=3
gr=v_grid(n,1)
x=np.empty([len(gr)],float)
y=np.empty([len(gr)],float)
z=np.empty([len(gr)],float)
print(len(gr))

for i in range(len(gr)):
    x[i] = gr[i][0]
    y[i] = gr[i][1]
    z[i] = gr[i][2]


ax.scatter(x, y, z)


ax.set_title('grid')
plt.show()


import Intence
import numpy as np
from matplotlib import pyplot as plt


wavelen=1.4
values = Intence.intence(3, 1., 180, wavelen)

# Drawing data points
phi = np.linspace(0, 2 * np.pi, 180)
theta = np.linspace(0, np.pi, 180)
#

# Generate drawing two-dimensional data
p, t = np.meshgrid(phi, theta)

plt.figure(figsize=(6,6))
ax = plt.subplot(projection='polar')
plot = ax.contourf(p, t, values, cmap='gray')
plt.colorbar(plot)
plt.grid(c='black')
ax.set_title('interatomik distance = 1 A,wavelength =' + str(wavelen) + ' A')

plt.show()
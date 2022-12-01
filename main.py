import numpy as np
from Intence import intence ,int_show
from grid import make_grid, v_grid , g_grid


print('input number of points in edge, inter atomic distance, wavelength, number of angles')

points = int(input())
spacing = float(input())
wavelen = float(input())
nangle = int(input())

print('Saving files with data')


with open('crystal.txt', 'a') as f:

    for el in make_grid(points, spacing):
        f.write(str(el) + '\n')


mat = np.matrix(intence(points, spacing, nangle, wavelen))
with open('intenses.txt', 'a') as f:
    for line in mat:
        np.savetxt(f, line, fmt='%.2f')

print('Done!')

print('showing image')

int_show(points, spacing, nangle, wavelen)

print('Done!')

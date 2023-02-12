import grid
import math as m
import numpy as np
from matplotlib import pyplot as plt


def delta(theta, phi, x, y, z, wavelen):
    ans = (m.sin(theta) * (x * m.cos(phi) + y * m.sin(phi)) + z * m.cos(theta) - z) * 2 * m.pi / wavelen
    return ans


def intence(points, spacing, nangle, wavelen):
    gr = grid.make_grid(points, spacing)
    intenses = np.empty([nangle, nangle], float)
    cosum = 0.
    sinsum = 0.
    theta = np.linspace(0, np.pi, nangle)
    phi = np.linspace(0, 2 * np.pi, nangle)
    for i, t in enumerate(theta):
        for j, p in enumerate(phi):
            for k in range(points ** 3):
                x = gr[k][0]
                y = gr[k][1]
                z = gr[k][2]
                cosum = cosum + m.cos(delta(t,  p, x, y, z, wavelen))
                sinsum = sinsum + m.sin(delta(t,  p, x, y, z, wavelen))
            intenses[i][j] = m.sqrt(cosum ** 2 + sinsum ** 2)
    return intenses


def intencity(points, spacing, nangle, wavelen, taf):
    gr = grid.make_grid(points, spacing)
    intenses = np.empty([nangle, nangle], float)
    cosum = 0.
    sinsum = 0.
    theta = np.linspace(0, np.pi, nangle)
    phi = np.linspace(0, 2 * np.pi, nangle)
    for i, t in enumerate(theta):
        for j, p in enumerate(phi):
            for k in range(points ** 3):
                x = gr[k][0]
                y = gr[k][1]
                z = gr[k][2]
                cosum = cosum + m.cos(delta(t,  p, x, y, z, wavelen))
                sinsum = sinsum + m.sin(delta(t,  p, x, y, z, wavelen))
            arg_af = m.sin(t) / wavelen
            intenses[i][j] = m.sqrt(m.sqrt(cosum ** 2 + sinsum ** 2) * atom_factor(arg_af, taf) * spacing)
    print(atom_factor(arg_af, taf))
    return intenses


def atom_factor(arg, taf):
    dh = 0.05
    imax = 29
    if arg >= 0:
        i = m.trunc(arg / dh)
        if i > imax:
            return 0
        else:
            dx = (arg % dh)
            return taf[i] + (taf[i+1] - taf[i]) * dx



def int_show(points, spacing, nangle, wavelen):
    values = intence(points, spacing, nangle, wavelen)

    # Drawing data points
    phi = np.linspace(0, 2 * np.pi, 180)
    theta = np.linspace(0, np.pi, 180)
    #

    # Generate drawing two-dimensional data
    p, t = np.meshgrid(phi, theta)

    plt.figure(figsize=(5, 5))
    ax = plt.subplot(projection='polar')
    ax.contourf(p, t, values, cmap='gray')
    plt.grid(c='black')

    plt.show()


def atom_factor0(arg, taf):
    dh = 0.05
    imax = 29
    if arg >= 0:
        i = m.trunc(arg/dh)
    if i > imax:
        Result=0
    else:
        dx = (arg % dh)
        Result=taf[i]+(taf[i+1]-taf[i])*dx
    return Result


def Intensity1(A, L, T, Fi, c, taf):
    k= 2 * m.pi / L
    SinT = m.sin(T)
    CosT = m.cos(T)
    SinFi = m.sin(Fi)
    CosFi=m.cos(Fi)
    ReA=0
    ImA=0
    for i in range(len(c)):
        Arg=k*(SinT*(c[i][0]*CosFi+c[i][1]*SinFi)+c[i][2]*CosT-c[i][2])
        ReA= ReA + m.cos(Arg)
        ImA=ImA + m.sin(Arg)
        Sum = m.sqrt(ReA*ReA+ImA*ImA)
        ArgAF = m.sin(T)/L
        F = atom_factor0(ArgAF, taf)
    return m.sqrt(A*F*Sum)


def integral_inten(points, spacing, nangle, wavelen, taf):
    gr = grid.make_grid(points, spacing)
    intenses = np.empty([nangle, nangle], float)
    theta = np.linspace(0, np.pi, nangle)
    phi = np.linspace(0, 2 * np.pi, nangle)
    for i, t in enumerate(theta):
        for j, p in enumerate(phi):
                intenses[i][j] = Intensity1(1, wavelen, t, p, gr, taf)
    return intenses
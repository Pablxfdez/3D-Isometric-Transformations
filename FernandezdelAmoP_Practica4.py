import os
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from matplotlib import animation

from scipy.spatial import ConvexHull
from scipy.spatial import distance
from skimage import io, color

"""
PRÁCTICA 4: GEOMETRÍA COMPUTACIONAL

PABLO FERNÁNDEZ DEL AMO   04231435X
"""

# define functions to be used later

# calculate centroid of a set of points
def calcularCentroide(S):
    return np.mean(S,axis=0)

# calculate diameter of a set of points
# this function takes long to execute when considering large number of points, so we obtain the diameter from its convex hull (the same one)
def calcularDiametro(S):
    diameter = 0
    hull = ConvexHull(S)
    for i in range(len(hull.vertices)):
        for j in range(i+1,len(hull.vertices)):
            distance_max = distance.euclidean(S[hull.vertices[i]], S[hull.vertices[j]])
            if distance_max > diameter:               
                diameter = distance_max
    return diameter

# apply transformation on a set of points
# M is a matrix representing rotation and scaling
# v is a vector representing translation
# centroid is the center of the set of points
def transformation(S, M, centroid, v):
    return centroid + (np.matmul(M, (S - centroid).T)).T + v

# apply rotation and translation on a set of points
# theta is the angle of rotation
# num determines the type of translation
# S is the set of points
# centroid is the center of the set of points
# diameter is the diameter of the set of points
def rotation_translation(S, centroid, diameter, theta, num):
    M =  np.array([[np.cos(theta), -np.sin(theta), 0], [np.sin(theta), np.cos(theta), 0], \
                               [0, 0, 1]])
    if num == 1:  # for problem I
        v = np.array([0, 0, diameter])
    else:  # for problem
        v = np.array([diameter, diameter, 0])
    
    return transformation(S, M, centroid, v)

# animate first set of points (APARTADO I)
def animate1(t, S, centroid, diameter, theta, shape):
    St = rotation_translation(S, centroid, t * diameter, t * theta, num = 1)

    ax = plt.axes(projection='3d')
    ax.set_xlim(-30,30)
    ax.set_ylim(-30,30)
    ax.set_zlim(-60,240)
    cset = ax.contour(St[:, 0].reshape(shape), St[:, 1].reshape(shape), St[:, 2].reshape(shape),\
                       16, extend3d=True,cmap = plt.cm.get_cmap('viridis')) 
    ax.clabel(cset, fontsize=9, inline=1)
  


    return ax,

# animate second set of points (APARTADO II)
def animate2(t, S, centroid, diameter, theta):
    St = rotation_translation(S, centroid, t * diameter, t * theta, num = 2)
    
    ax = plt.axes(projection='3d')
    ax.set_xlim(0,700)
    ax.set_ylim(0,700)
    ax.set_zlim(-0.04,0.04)
    col = plt.get_cmap("viridis")(np.array(0.1+S[:,2]))

    ax.scatter(St[:, 0], St[:, 1],c=col,s=0.1,animated=True)
    return ax,

"""
APARTADO 1
"""
def apartado1():
    print ('APARTADO I:')
    theta = 3 * np.pi
    X, Y, Z = axes3d.get_test_data(0.05)
    shape = X.shape
    S = np.column_stack([X.flatten(),Y.flatten(),Z.flatten()])
    diameter = calcularDiametro(S)
    centroid = calcularCentroide(S)

    # Obtenemos la figura en inicio:
    
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    cset = ax.contour(X, Y, Z, 16, extend3d=True,cmap = plt.cm.get_cmap('viridis'))
    ax.clabel(cset, fontsize=9, inline=1)
    fig.savefig('Inicio.png',format='png')
    plt.show()

    St = rotation_translation(S, centroid, diameter, theta, num = 1)

    # Y la final

    fig = plt.figure()
    ax = plt.axes(projection='3d')
    cset = ax.contour(St[:, 0].reshape(shape), St[:, 1].reshape(shape), St[:, 2].reshape(shape),\
                       16, extend3d=True,cmap = plt.cm.get_cmap('viridis'))
    ax.clabel(cset, fontsize=9, inline=1)
    fig.savefig('Final.png',format='png')
    plt.show()

    # Creamos la animación
    fig = plt.figure(figsize=(6,6))
    ani = animation.FuncAnimation(fig, animate1,frames=np.arange(0,1.01,0.05),
                                fargs = (S,centroid, diameter, theta, shape), interval=20)
    ani.save('animacion_limited1.gif',fps=5)
    plt.show()



"""
Apartado II
"""
def apartado2():
    print ('APARTADO II:')
    os.getcwd()
    img = io.imread('arbol.png')
    #dimensions = color.guess_spatial_dimensions(img)
    #print(dimensions)
    #io.show()
    #io.imsave('arbol2.png',img)


    fig = plt.figure(figsize=(5,5))
    p = plt.contourf(img[:,:,0],cmap = plt.cm.get_cmap('viridis'), levels=np.arange(0,240,2))
    fig.savefig('Hoja1.png',format='png')
    plt.axis('off')

    xyz = img.shape

    x = np.arange(0,xyz[0],1)
    y = np.arange(0,xyz[1],1)
    xx,yy = np.meshgrid(x, y)
    xx = np.asarray(xx).reshape(-1)
    yy = np.asarray(yy).reshape(-1)
    z  = img[:,:,0]
    zz = np.asarray(z).reshape(-1)


    #Consideraremos sólo los elementos con zz < 240 

    #Variables de estado coordenadas
    x0 = xx[zz<240]
    y0 = yy[zz<240]
    z0 = zz[zz<240]/256.


    #Variable de estado: color
    col = plt.get_cmap("viridis")(np.array(0.1+z0))

    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(1, 2, 1)
    plt.contourf(x,y,z,cmap = plt.cm.get_cmap('viridis'), levels=np.arange(0,240,2))
    ax = fig.add_subplot(1, 2, 2)
    plt.scatter(x0,y0,c=col,s=0.1)
    fig.savefig('Hoja2.png',format='png')
    plt.show()


    #Calculamos el diametro de la hoja para hacer la transformación
    S = np.column_stack([x0, y0, z0])
    diameter = calcularDiametro(S)
    print(f'Diámetro: {diameter} ')

    centroid = calcularCentroide(S)
    #Calculamos el centroide de la hoja
    print(f"centroide: {centroid} ")

    theta = 3 * np.pi

    #Generamos la animación
    fig = plt.figure(figsize=(6,6))
    ani = animation.FuncAnimation(fig, animate2, frames=np.arange(0,1,0.025), fargs = (S,centroid, diameter, theta), \
                                interval=20)
    #os.chdir(vuestra_ruta)
    ani.save("Hoja_arbol_limited1.gif", fps = 10)  
    os.getcwd()


apartado1()
apartado2()
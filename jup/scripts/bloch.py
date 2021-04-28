import matplotlib.pyplot as plt
from matplotlib import cm, colors
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# makes a sphere mesh of radius 1
def make_sphere(r=1.0):
    phi, theta = np.mgrid[0.0:np.pi:100j, 0.0:2.0*np.pi:100j]
    x = r*np.sin(phi)*np.cos(theta)
    y = r*np.sin(phi)*np.sin(theta)
    z = r*np.cos(phi)
    return x, y, z

def to_bloch_vector(ket):
    rho = np.outer(ket,np.conj(ket))
    return np.array([
        2*np.real(rho[0,1]),
        2*np.imag(rho[1,0]),
        np.real(rho[0,0] - rho[1,1])
    ])
    

def plot_bloch_vector(ket, name=r'$|\psi\rangle$', 
                      title=None):
    
    # convert ket to bloch vector:
    vector = to_bloch_vector(ket)
    
    # plot sphere surface and axes:
    fig = plt.figure(figsize=(6.66,4))
    ax = fig.add_subplot(111, projection='3d')
    for e in np.eye(3):
        ax.plot([-e[0],e[0]], [-e[1], e[1]], [-e[2], e[2]],'k',linewidth=1)
    ax.plot_surface(*make_sphere(),  
        rstride=1, cstride=1, cmap='viridis', alpha=0.3, linewidth=0)
    
    # plot and label vectors:
    ax.quiver(0,0,0,*vector, color='r', arrow_length_ratio=0.15, lw=3)
    ax.text(*vector, name, fontsize=11.0)
    ax.text(0,0,1.2,r'$|0\rangle$',fontsize=11.0)
    ax.text(0,0,-1.2,r'$|1\rangle$',fontsize=11.0)
    ax.text(1.2,0,0,r'$|\plus\rangle$',fontsize=11.0)
    ax.text(-1.2,0,0,r'$|\minus\rangle$',fontsize=11.0)
    ax.text(0,0,-1.2,r'$|1\rangle$',fontsize=11.0)
    if not title:
        title = f'Bloch Sphere ({name})' 
    fig.suptitle(title, fontsize=16)
    
    # adjust axes ticks:
    axticks = [-1, 0, 1]
    neg_axticks = [1, 0, -1]
    ax.set_zticks(axticks)
    ax.set_xticks(axticks)
    ax.set_yticks(axticks)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.1])
    ax.set_zlim([-1, 1])
    ax.auto_scale_xyz([-1.1, 1.1], [-1.1, 1.1], [-1, 1])
    fig.tight_layout()
    ax.view_init(30,25)
    plt.show()
    
def plot_bloch_trajectory(kets, name=r'$|\psi\rangle$', 
                      title=None):
    
    # convert ket to bloch vector:
    vec_pts = np.array([ to_bloch_vector(k) for k in kets ])
    vector = vec_pts[-1]
    
    # plot sphere surface and axes:
    fig = plt.figure(figsize=(6.66,4))
    ax = fig.add_subplot(111, projection='3d')
    for e in np.eye(3):
        ax.plot([-e[0],e[0]], [-e[1], e[1]], [-e[2], e[2]],'k',linewidth=1)
    ax.plot_surface(*make_sphere(),  
        rstride=1, cstride=1, cmap='viridis', alpha=0.3, linewidth=0)
    
    # plot and label vectors:
    ax.plot(vec_pts[:,0], vec_pts[:,1], vec_pts[:,2], 'r')
    ax.quiver(0,0,0,*vector, color='r', arrow_length_ratio=0.15, lw=3)
    ax.text(*vector, name, fontsize=11.0)
    ax.text(0,0,1.2,r'$|0\rangle$',fontsize=11.0)
    ax.text(0,0,-1.2,r'$|1\rangle$',fontsize=11.0)
    ax.text(1.2,0,0,r'$|\plus\rangle$',fontsize=11.0)
    ax.text(-1.2,0,0,r'$|\minus\rangle$',fontsize=11.0)
    ax.text(0,0,-1.2,r'$|1\rangle$',fontsize=11.0)
    if not title:
        title = f'Bloch Sphere ({name})' 
    fig.suptitle(title, fontsize=16)
    
    # adjust axes ticks:
    axticks = [-1, 0, 1]
    neg_axticks = [1, 0, -1]
    ax.set_zticks(axticks)
    ax.set_xticks(axticks)
    ax.set_yticks(axticks)
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_xlim([-1.2, 1.2])
    ax.set_ylim([-1.2, 1.1])
    ax.set_zlim([-1, 1])
    ax.auto_scale_xyz([-1.1, 1.1], [-1.1, 1.1], [-1, 1])
    fig.tight_layout()
    ax.view_init(30,25)
    plt.show()

def _main():
    # Example plot:
    theta = np.pi/2
    phi = np.pi/2
    psi = np.array([
        np.cos(theta/2),
        np.exp(1j*phi)*np.sin(theta/2)
    ])
    plot_bloch_vector(psi)


if __name__ == '__main__':
    _main()

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mp
from matplotlib.path import Path
from matplotlib import animation,rc,transforms
rc('animation', html='jshtml')
plt.rcParams.update({"font.family" : "serif","mathtext.fontset" : "cm"})

#prameters
Nf = 200 #number of animation frames
theta = np.linspace(0,360,Nf) #angle to rotate
alpha=np.concatenate((np.linspace(0,np.pi/2,int(Nf/2)),np.linspace(np.pi/2,0,int(Nf/2))))
cls = ['r','lightgreen','b','c','yellow','orange','m','maroon','darkgreen','lightblue','pink','crimson','teal']
x=np.linspace(0,1,Nf)
fig = plt.figure(figsize=(9,16))
ax1=fig.add_axes((1/18,0,8/9,0.5),   xlim=[0,1], ylim=[-1,1])
ax2=fig.add_axes((1/18,0.5,8/9,0.5), xlim=[0,1], ylim=[-1,1])
fig.tight_layout()
ax1.axis('off')
ax2.axis('off')
P0 = (0.25,0)
P3= (0.75,0)

def animate(i): # animation function.  This is called sequentially
  ax1.clear()
  ax2.clear()
  P1 = (0.25*np.cos(x[i]*2*np.pi) + 0.25, 0.9*np.sin(x[i]*2*np.pi))
  P2 = (-0.25*np.sin(x[i]*2*np.pi) + 0.75, 0.9*np.cos(x[i]*2*np.pi))

  ax2.add_patch(mp.PathPatch(Path([P0,P1,P2,P3], [Path.MOVETO,Path.CURVE4,Path.CURVE4,Path.CURVE4]),
                             fc='none',ec='b',lw=5))
  ax1.add_patch(mp.PathPatch(Path([P0,P1,P2,P3], [Path.MOVETO,Path.CURVE4,Path.CURVE4,Path.CURVE4]),fc='none',ec='b',lw=4))
  ax1.plot([P0[0],P1[0],P2[0],P3[0]],[P0[1],P1[1],P2[1],P3[1]],'--x',color='orange',markersize=10)
  ax1.axis('off')
  ax1.set_xlim(0,1)
  ax1.set_ylim(-1,1)
  ax2.axis('off')
  ax2.set_xlim(0,1)
  ax2.set_ylim(-1,1)
  ax2.text(0.5,0.8,'Cubic Bézier Curve',size=22,ha='center')
  ax1.text(0.5,0.9,'Cubic Bézier Curve with Control Points Shown',size=22,ha='center')
  return

anim = animation.FuncAnimation(fig, animate, frames=Nf, interval=50)
# anim #uncomment to generate animation in the output area
# to save the animation, uncomment the following three lines
fn = r"BezierCurveCubic.mp4" 
writervideo = animation.FFMpegWriter(fps=50) #save the video at 50 frames per sec
anim.save(fn, writer=writervideo,dpi = 120)
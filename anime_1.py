import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import numpy as np

# Set up duration of animation
t0=0
t_end=2
dt=0.005

#Create array for time
t=np.arange(t0,t_end+dt,dt)

#create an x-array
x=10*800*t

#create y-array
altitude=2
y=np.ones(len(t))*altitude

frame_amount=int(len(t)/10)
dot=np.zeros(frame_amount)
n=2
for i in range(0,frame_amount):
    if i==n:
        dot[i]=x[i]
        n=n+2
    else:
        dot[i]=x[n-2]

def update_plot(num):

    plane_trajectory.set_data(dot[0:num],y[0:num])
    plane_1.set_data([x[num]-40,x[num]+20],[y[num],y[num]])
    plane_2.set_data([x[num]-20,x[num]],[y[num]+0.3,y[num]])
    plane_3.set_data([x[num]-20,x[num]],[y[num]-0.3,y[num]])
    plane_4.set_data([x[num]-40,x[num]-30],[y[num]-0.15,y[num]])
    plane_5.set_data([x[num]-40,x[num]-30],[y[num]+0.15,y[num]])

    stopwatch0.set_text(str(round(t[num],1))+' hrs')
    dist_counter0.set_text(str(round(x[num]))+' km')
    
    return plane_trajectory,plane_1,plane_2,plane_3,plane_4,plane_5,\
           stopwatch0,dist_counter0

fig=plt.figure(figsize=(16,9),dpi=120,facecolor=(0.8,0.8,0.8))
gs=gridspec.GridSpec(2,2)

ax0=fig.add_subplot(gs[0,:],facecolor=(0.9,0.9,0.9))
plane_trajectory,=ax0.plot([],[],'r:o',linewidth=2)
plane_1,=ax0.plot([],[],'k',linewidth=10)
plane_2,=ax0.plot([],[],'k',linewidth=5)
plane_3,=ax0.plot([],[],'k',linewidth=5)
plane_4,=ax0.plot([],[],'k',linewidth=3)
plane_5,=ax0.plot([],[],'k',linewidth=3)

#Draw houses
house_1,=ax0.plot([100,100],[0,1.0],'k',linewidth=7)
house_2,=ax0.plot([300,300],[0,1.0],'k',linewidth=7)
house_3,=ax0.plot([700,700],[0,0.7],'k',linewidth=15)
house_4,=ax0.plot([900,900],[0,0.9],'k',linewidth=10)
house_5,=ax0.plot([1300,1300],[0,1.0],'k',linewidth=20)

box_object=dict(boxstyle= 'circle',fc=(0.1,0.9,0.9),ec='r', lw=3)
stopwatch0=ax0.text(1400,0.65,'',size=10,color='g',bbox=box_object)

box_object2=dict(boxstyle='square',fc=(0.9,0.9,0.9),ec='g', lw=1)
dist_counter0=ax0.text(1000,0.5,'',color='r',bbox=box_object2)

plt.xlim(x[0],x[-1]/10)
plt.ylim(0,y[0]+1)
plt.xticks(np.arange(0,1601,400),size=15)
plt.yticks([0,1,2,3],size=15)
plt.xlabel('x-distance',fontsize=15)
plt.ylabel('y-distance',fontsize=15)
plt.title('Airplane',fontsize=20)
plt.grid(True)


#################Animation#################
plane_ani=animation.FuncAnimation(fig,update_plot,
        frames=frame_amount,interval=20,repeat=True,blit=True)
plt.show()

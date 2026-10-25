import math
import matplotlib.pyplot as plt
from matplotlib.patches import RegularPolygon

R=float(input("Enter the radius of the cell (in km): "))
N = 7
D = R * math.sqrt(3*N) 
colors = ['red', 'lightgreen', 'lightblue', 'yellow', 'cyan', 'white', 'orange']
f1 = []

fig,ax = plt.subplots(figsize=(10,5))

for row in range(-3,4):
    for col in range(-3,4):
        x = (col + (row%2)/2) * math.sqrt(3) * R
        y = row * 1.5 * R
        n = (col + 2*row) % N
        if n==0:
            f1.append((x,y))
        ax.add_patch(RegularPolygon(
            (x,y),6,radius=R,facecolor=colors[n],edgecolor='black'
        ))
        ax.text(x,y,f'f{n+1}')

if len(f1)>=6:
    p1,p2 = f1[4],f1[5]
    ax.plot([p1[0],p2[0]],[p1[1],p2[1]],'k--')
    x = (p1[0]+p2[0])/2
    y = (p1[1]+p2[1])/2
    ax.text(x,y,f'D={D:.2f}',bbox=dict(fc='white',ec='black'))

ax.axis('off')
plt.title(f"Frequency Reuse R={R}, D={D:.2f}, N=7")
plt.show()

        
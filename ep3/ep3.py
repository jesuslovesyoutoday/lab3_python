import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def data0_count(x, A, data):
    DATA = [np.array(data, dtype = np.float64)]
    for i in range(255):
        i  += 1
        tmp = np.array(DATA[i - 1] - 0.5 * A @ (DATA[i - 1]))
        DATA.append(tmp)
    return DATA 

def data_count(i, x, A, DATA):
	return [x, DATA[i]]

def init():
    line.set_data([], [])
    return line,
    
def animate(i, x, A, data):
	d = data_count(i, x, A, data)
	x = d[0]
	y = d[1]
	line.set_data(x, y)
	return line,


fig, ax = plt.subplots()
line, = ax.plot([], [], lw = 2)
ax.set_xlim(0, 50) 
ax.set_ylim(0, 10)
ax.grid()
 
"""with open("start.dat") as f:
		data = f.read().split('\n')"""
data = np.loadtxt("start.dat")
n = len(data)
A = np.diag(np.full(n, 1)) - np.eye(n, k = -1)
A[0][len(A[0]) - 1] = -1
x = np.linspace(0, 50, len(data))
print(A)

DATA = data0_count(x, A, data)
	
anim = animation.FuncAnimation(fig, animate, frames=256, init_func=init, interval=20, blit = True, fargs = [x, A, DATA])
#anim.save('a.gif')
plt.show()

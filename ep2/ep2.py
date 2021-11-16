import numpy as np
import matplotlib.pyplot as plt
import os

def read_file(filename):
	with open(filename) as f:
		data = np.array(f.read().split('\n'), dtype = np.float64)
	return data
		
def filter_signal(data):
	new_data = [data[0]]
	for i in range(1, len(data)):
		lim = i - 9
		if lim < 0:
			lim = 0
		new_data.append(np.mean(data[lim:i]))
	new_data = np.array(new_data)
	return new_data
	
def graph(data, new_data):
	fig, axs = plt.subplots(2, 2)
	x = np.linspace(0, len(new_data), len(data), dtype = np.int64)
	#print(x, len(x))
	#print(data, new_data, len(data), len(new_data))
	
	plt.subplot(1, 2, 1)
	plt.plot(x, data)
	plt.title("Noise signal", fontsize = 20)
	plt.grid()
	
	plt.subplot(1, 2, 2)
	plt.plot(x, new_data)
	plt.title("Filtered signal", fontsize = 20)
	plt.grid()
	
	plt.show()

files = next(os.walk("signals"))
file_count = len(files)
print(file_count)

for i in range(1, file_count + 1):
	filename = "signals/signal0" + str(i) + ".dat"
	data = read_file(filename)
	new_data = filter_signal(data)
	graph(data, new_data)

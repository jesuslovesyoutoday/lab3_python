import numpy as np
from PIL import Image
import matplotlib.pyplot as plt

import os

def contrast_fixing(filename):
    img = Image.open(filename)
    data = np.array(img)

    max_shade = np.max(data)
    min_shade = np.min(data)

    data1 = np.array(data - min_shade)
    k = (float(255 / (max_shade - min_shade)))
    updated_data = np.array(data1 * k)
    res_img = Image.fromarray(updated_data)
    
    if res_img.mode != 'RGB':
        res_img = res_img.convert('RGB')
    res_img.save("updated_" + filename)
    
    return updated_data, data1, k, data 

def intense_histogram(filename, updated_data):

    unique, counts = np.unique(updated_data, return_counts = True)
    res = dict(zip(unique, counts))

    y_pos = np.arange(len(res.keys()))
    plt.bar(range(len(res)), list(res.values()), align = 'center')
    plt.xticks(range(len(res)), list(np.round(unique,2)), rotation = 45)
    plt.title(filename + " intense")
    plt.show()
    
    
def losses_histogram(filename, updated_data, data1, k):

    data_int = np.array(data1 * k, dtype = np.int64)
    losses = data_int - updated_data
     
    unique, counts = np.unique(losses, return_counts = True)
    res = dict(zip(unique, counts))

    y_pos = np.arange(len(res.keys()))
    plt.bar(range(len(res)), list(res.values()), align = 'center')
    plt.xticks(range(len(res)), list(np.round(unique,2)), rotation = 45)
    plt.title(filename + " losses")
    plt.show()   
    
files = next(os.walk("lunar_images"))
file_count = len(files)

for i in range(1, file_count + 1):
    filename = "lunar_images/lunar0" + str(i) + "_raw.jpg"
    upd_data, data1, k, data = contrast_fixing(filename)
    intense_histogram(filename, upd_data)
    intense_histogram(filename, data)
    
    #losses_histogram(filename, upd_data, data1, k)

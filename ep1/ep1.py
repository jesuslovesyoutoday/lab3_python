import numpy as np
from PIL import Image

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
	

files = next(os.walk("lunar_images"))
file_count = len(files)

for i in range(1, file_count + 1):
	filename = "lunar_images/lunar0" + str(i) + "_raw.jpg"
	contrast_fixing(filename)

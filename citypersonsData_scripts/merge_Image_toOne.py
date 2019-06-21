# --------------------------------------------
# Merge all the image file into one directory "JPEGImages"
# Author: Guanghao Chen
# Date: May 1 2019
# --------------------------------------------

import os
import shutil
import pickle
ori_dir = "./oriImages/val"
des_dir = "./JPEGImages"
file_list = []

count = 0
for sub_dir in os.listdir(ori_dir):
	sub_dir_path = os.path.join(ori_dir, sub_dir)
	for file in os.listdir(sub_dir_path):
		filename = os.path.splitext(file)[0]
		file_path = os.path.join(sub_dir_path, file)
		shutil.copy(file_path, os.path.join(des_dir, file))
		count += 1
		file_list.append(filename)

	print("{} directory has done".format(sub_dir))

with open("test.pickle", "wb") as f:
	pickle.dump(file_list,f)
	
print("=================")
print("Image File total: {}".format(count))
print("=================")
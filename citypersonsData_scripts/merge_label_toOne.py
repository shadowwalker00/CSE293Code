# --------------------------------------------
# Merge all the label file into one directory
# Author: Guanghao Chen
# Date: May 1 2019
# --------------------------------------------

import os
import shutil

ori_dir = "./oriLabel/train"
des_dir = "./test"

count = 0
for sub_dir in os.listdir(ori_dir):
	if sub_dir == '._.DS_Store':
		continue
	sub_dir_path = os.path.join(ori_dir, sub_dir)
	for file in os.listdir(sub_dir_path):
		file_path = os.path.join(sub_dir_path, file)
		shutil.copy(file_path, os.path.join(des_dir, file))
		count += 1

print("=================")
print("File total: {}".format(count))
print("=================")
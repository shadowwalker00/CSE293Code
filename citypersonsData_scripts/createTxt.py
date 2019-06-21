import os
import pickle
filelist_name = "test.pickle"
with open(filelist_name, "rb") as f:
	file_list = pickle.load(f)
print("file number: {}".format(len(file_list)))
txt_name = "test.txt"
with open(txt_name,"w") as f:
	for item in file_list:
		f.write(item+"\n")
		
print("Finish Write in...")


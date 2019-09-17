import os
import sys

base_dir = sys.argv[1]

for path,pathname,filenames in os.walk(base_dir):
	for filename in filenames :
		with open(os.path.join(path,filename),'r')   as f:
			for line in f.readlines():
				with open(os.path.join(path,filename.replace(".txt","_1.txt")),"w") as f1:
					f1.write(line)
					print(line)
					break

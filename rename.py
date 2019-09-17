#coding=utf-8
import os
import sys

if 1:
	in_dir = sys.argv[1]
	out_dir = sys.argv[2]

	k = 0;
	with open(os.path.join(out_dir,"transcript.txt"),"w") as tfile:
	
		for path,pathname,filenames in os.walk(in_dir):
			for filename in filenames:
				if filename.endswith(".wav"):
					spkid = int(filename.split("car_conch_seq_speaker")[1].split("_")[1].replace(".wav",""))+4100
					pre="BAC009S%04dW%04d"%(spkid,k)
					k +=1
					os.popen("cp %s %s"%(os.path.join(path,filename),os.path.join(out_dir,pre+".wav")))
					with open(os.path.join(in_dir,filename.replace(".wav",".txt")),encoding='gb2312') as f:
						for line in f.readlines():
							tfile.write(pre +' ' + line.replace("\n","") +"\n")
							break
"""
						for line in  f.readlines():
							if len(line)>5:
								print(line.strip())
								tfile.write(pre +' ' + line +"\n")	
					print(pre)
"""

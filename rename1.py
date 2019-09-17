#encoding=utf-8
import os
import sys

if __name__ == "__main__":
	in_dir = sys.argv[1]
	out_dir = sys.argv[2]

	k = 0;
	with open(os.path.join(out_dir,"transcript.txt"),"w+") as tfile:

		with open(os.path.join(in_dir,"gc_1_2.txt"),"r",encoding="utf-8") as f1:
			for line in f1.readlines():
				print(line)
				filename  = line.split(" ")[0]
				biaozhu = line.split(" ")[1:]
				spkid = int(filename.split("car_conch_seq_speaker")[1].split("_")[1].replace(".wav",""))+4300
				pre="BAC009S%04dW%04d"%(spkid,k)
				tfile.write("%s %s"%(pre,str(" ".join(biaozhu)) ))
				os.popen("cp %s.wav %s"%(os.path.join(in_dir,filename),os.path.join(out_dir,pre+".wav")))
				k+=1




"""



	
		for path,pathname,filenames in os.walk(in_dir):
			for filename in filenames:
				if filename.endswith(".wav"):
					spkid = int(filename.split("car_conch_seq_speaker")[1].split("_")[1].replace(".wav",""))+4100
					pre="BAC009S%04dW%04d"%(spkid,k)
					k +=1
					os.popen("cp %s %s"%(os.path.join(path,filename),os.path.join(out_dir,pre+".wav")))
					with open(os.path.join(in_dir,filename.replace(".wav",".txt"))) as f:
						for line in  f.readlines():
							#tfile.write(pre +' ' + line )	
							print(pre +' ' + line )	
"""

#coding=utf8
#python3

import os
import sys
from pydub import AudioSegment
from pypinyin import lazy_pinyin

samplerate = 8000

# car_conch_iso_speaker1_24.wav
def wav2kws(file_path,wavfile,out_dir):
	global k
	
	tmp_count = 0;
	uttid = 65535

	sound = AudioSegment.from_file(os.path.join(file_path,wavfile))
	with open(os.path.join(file_path,wavfile.replace(".wav",".txt")),'r',encoding='gb2312') as f:
		with open(os.path.join(out_dir,"transcript.txt"),"a+") as tfile:
			for line in  f.readlines():
				tmp_uttid = line.split(":")[-2]
				if tmp_uttid == uttid:
					tmp_count +=1
				else:
					uttid = tmp_uttid
					tmp_count = 0
	
				flag  = 0

				tmp = line.split(":")
				tmp_start_ms = int(int(line.split(":")[0].split("~")[0])/samplerate*1000)
				tmp_end_ms = int(int(line.split(":")[0].split("~")[1])/samplerate*1000)
				

				tmp_text = line.split(":")[-1].split('，')
				print(wavfile)
				print(tmp_start_ms)
				print(tmp_end_ms)	
				tmp_filename = "BAC009" + 'S' + "%04d"%(int(wavfile.split('car_conch_iso_speaker')[1].split("_")[0])+4000) + "W"+ "%04d"%k
				print("%04d"%k)
#				print(tmp_uttid)
#				print(tmp_count)
#				print(tmp_text[tmp_count%(len(tmp_text))])


				tfile.write(tmp_filename + " " + tmp_text[tmp_count%(len(tmp_text))].strip().replace("，"," ") +"\n")
				

				sound[tmp_start_ms:tmp_end_ms].export(os.path.join(out_dir,tmp_filename+'.wav'),format='wav')

				
				

				k += 1




if __name__=="__main__":
	base_dir = "./kaichuang/guli/"
	out_dir = "./out"
	global k 
	k = 0
	wav2kws(base_dir,"car_conch_iso_speaker2_3.wav",out_dir)
'''
	for path,pathname,filenames in os.walk(base_dir):
		for filename in filenames:
			if filename.endswith(".wav"):
				wav2kws(path,filename,out_dir)
'''

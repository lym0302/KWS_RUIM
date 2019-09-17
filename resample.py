# resample
import librosa
import os
import sys

from scipy.io import wavfile

import numpy as np

def resample(in_dir,in_filename,in_sr,out_dir,out_filename,out_sr):

	
	y, sr = librosa.load(os.path.join(in_dir,in_filename), sr=in_sr)
	y_out = librosa.resample(y,sr,out_sr)
	wavfile.write(os.path.join(out_dir,out_filename),16000,(y_out*32768).astype(np.int16))

if __name__=="__main__":
	base_dir = sys.argv[1]
	out_dir = sys.argv[2]
	
	for path,pathname,filenames in os.walk(base_dir):
		for filename in filenames:
			resample_16(path,filename,8000,out_dir,filename,16000)

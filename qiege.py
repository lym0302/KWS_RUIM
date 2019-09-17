from pydub import AudioSegment

def qiege(in_dir,in_file,out_dir,out_file,start_ms,end_ms):
  sound = AudioSegment.from_file(os.path.join(in_dir,in_file))
  sound[start_ms:end_ms].export(os.path.join(out_dir,out_file),format='wav')

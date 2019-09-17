# coding=utf-8
# python3
# process result of kws

import os
from pydub import AudioSegment
from get_chong import *

pinyin_dict = {"jiba":"鸡巴","jibawaer":"鸡巴娃儿","jibaluan":"鸡巴卵","xiangtuoshi":"像砣屎","xiangtouzhu":"像头猪","rinima":"日你妈","rinimei":"日你妹","rimayo":"日妈哟","rinixianren":"日你仙人","rinixianren1":"日你仙人","shabi":"傻逼","doubi":"逗逼","hayaer":"哈鸭儿","haer":"哈儿","yashuadehen":"牙刷得很","yaerdehen":"牙儿得很","hamapi":"哈麻批","jianmapi":"贱麻批","lanmapa":"烂麻批","mamaipi":"妈卖批","gunnimamaipi":"滚你妈卖批","sharen":"杀人","shasi":"杀死","jianren":"贱人","jianxiang":"贱相","jianhuo":"贱货","zazhong":"杂种","gouzazhong":"狗杂种","zapi":"杂皮","guierzi":"龟儿子","guisun":"龟孙","guisunzi":"龟孙子","guaxixide":"瓜西西的","baopilong":"保批龙","shasiren":"杀死人","zacai":"杂菜","xiangtouzhuyiyang":"像头猪一样","xiangtuoshiyiyang":"像砣屎一样","haponiang":"哈婆娘","lanpilanka":"烂批烂胩","lanpi":"烂批","lanka":"烂胩","siponiang":"死婆娘","lanponiang":"烂婆娘","laozapi":"杂皮","shasini":"杀死","guaxixide1":"瓜西西的","tamade":"他妈的","gouride":"狗日的","jianponiang":"贱婆娘"}


right_dict={} # different value
for key,value in pinyin_dict.items():
	right_dict[value] = 0


num_kcgl = 0
num_kclx = 0
num_gcgl  = 0
num_gclx = 0
num_alltest = 0

biaozhu_dict = {}

in_dir = "/root/wtt2/ruiming/result/test_data_prename"
for path,pathname,filenames in os.walk(in_dir):
	for filename in filenames:
		if filename.endswith(".txt"):
			with open(os.path.join(path,filename),"r",encoding="gb2312") as f_pre:
				for line in f_pre:
					biaozhu_dict[line.replace("\n","").split(":")[-1]] =0
					num_alltest +=1
					if "开窗孤立" in path:
						num_kcgl +=1
					elif "关窗孤立" in path:
						num_gcgl  += 1
					elif "开窗连续" in path:
						num_kclx +=1
					elif "关窗连续" in path:
						num_gclx += 1

in_dir = "/root/wtt2/ruiming/result/test_data_prename"
for path,pathname,filenames in os.walk(in_dir):
	for filename in filenames:
		if filename.endswith(".txt"):
			with open(os.path.join(path,filename),"r",encoding="gb2312") as f_pre:
				for line in f_pre:
					biaozhu_dict[line.replace("\n","").split(":")[-1]] += 1
				



file_all = []

file_id_con = {}



# construct dict
in_dir = "./test_data"
out_dir = "./qiege_out"
out_dir1 = "./qiege_out1"

def qiege(in_dir,in_file,out_dir,out_file,start_ms,end_ms):
	sound = AudioSegment.from_file(os.path.join(in_dir,in_file))
	sound[start_ms:end_ms].export(os.path.join(out_dir,out_file),format='wav')


# build file_dict
filename_dic = {}
with open("file_trans.txt","r",encoding="gb2312") as f4:
	for line in f4.readlines():
		linesplit = line.replace("\n","").split(" ")
		aname  = linesplit[0]
		bname  = linesplit[1]
		filename_dic[aname] = bname
		

with  open("utter_id","r") as f3:
	for line in f3.readlines():
		line = line.replace("\n","")

		filename = line.split(" ")[0]
		file_id = int(line.split(" ")[1])
		file_id_con[file_id] = filename






num_right = 0

num_wrong = 0
num_kcgl_right = 0
num_kcgl_wrong = 0

num_gcgl_right  = 0
num_gcgl_wrong = 0

num_kclx_right = 0
num_kclx_wrong = 0

num_gclx_right  = 0
num_gclx_wrong  = 0


# slice wav  according kws result and check  performance
# 


wav_dir = "./test_data_prename"

kk = 0
with open("./result.2","w+",encoding="utf-8") as f2:
	for ii in range(1,75):
		
		with  open("result.1","r") as f1:
			for line in f1.readlines():
				line = line.replace("\n","")
				result=line.split(" ")
				fileid = int(result[1])

				if ii  == fileid:
					file_name = file_id_con[fileid]
					kword = result[0]

					start = int(int(result[2])*80)
					end = int(int(result[3])*80)
					print(filename_dic[file_name].replace("\\","/"))
					with  open(os.path.join(wav_dir,filename_dic[file_name].replace("\\","/")),encoding="gb2312") as f5:

						for line1 in f5.readlines():
							line1 = line1.replace("\n","")
							start_b = int(line1.split(":")[0].split("~")[0])
							end_b = int(line1.split(":")[0].split("~")[1])

							text_b =  line1.split(":")[-1]
							chongfu = get_chong(start,end,start_b,end_b)
							if chongfu > 0.6:
								

								if pinyin_dict[kword] in  text_b:
									right_dict[pinyin_dict[kword]] += 1
									print(pinyin_dict[kword])
									print(text_b)
									print(chongfu)
									num_right +=1	
									print('right')
									if "开窗孤立" in filename_dic[file_name]:
										num_kcgl_right += 1
									elif "关窗孤立" in filename_dic[file_name]:
										num_gcgl_right  += 1
									elif "开窗连续" in filename_dic[file_name]:
										num_kclx_right  += 1
									elif "关窗连续" in filename_dic[file_name]:
										num_gclx_right += 1

								else:
									num_wrong += 1
									print("wrong")
									if "开窗孤立" in filename_dic[file_name]:
										num_kcgl_wrong += 1
									elif "关窗孤立" in filename_dic[file_name]:
										num_gcgl_wrong  += 1
									elif "开窗连续" in filename_dic[file_name]:
										num_kclx_wrong  += 1
									elif "关窗连续" in filename_dic[file_name]:
										num_gclx_wrong += 1


					f2.write("%s %s %d %d\n"%(filename_dic[file_name].replace(".txt",".wav"),pinyin_dict[kword],start,end))	

					#qiege(in_dir,file_name+".wav",out_dir,file_name+"_"+str(kk)+".wav",start/8,end/8)
					#qiege(in_dir,file_name+".wav",out_dir,filename_dic[file_name].replace(".txt","").replace("\\","_")+"_"+str(kk)+".wav",start/8,end/8)
					qiege(in_dir,file_name+".wav",out_dir1,filename_dic[file_name].replace(".txt","").replace("\\","_")+"_"+ pinyin_dict[kword] +"_%dms_%dms"%(start/8,end/8)+"_"+str(kk)+".wav",start/8,end/8)

					kk +=1

print("num_right = %d, num_wrong = %d, num_all = %d, right_rage = %f"%(num_right,num_wrong,num_alltest,float(num_right)/num_alltest))
print("num_kcgl = %d, num_gcgl = %d , num_kclx = %d num_gclx = %d"%(num_kcgl,num_gcgl,num_kclx,num_gclx) )
print("num_kcgl_right = %d,num_gcgl_right = %d, num_kclx_right= %d ,num_gclx_right= %d"%(num_kcgl_right,num_gcgl_right,num_kclx_right,num_gclx_right)   )
print("num_kcgl_wrong = %d,num_gcgl_wrong = %d, num_kclx_wrong= %d ,num_gclx_wrong= %d"%(num_kcgl_wrong,num_gcgl_wrong,num_kclx_wrong,num_gclx_wrong)   )
print("kcgl = %f , gcgl = %f, kclx = %f  , gclx = %f"%( float(num_kcgl_right)/float(num_kcgl)  ,  float(num_gcgl_right)/float(num_gcgl)  , float(num_kclx_right)/float(num_kclx)  ,  float(num_gclx_right)/float(num_gclx)          ))

for key,value in right_dict.items():
	print("%s %d"%(key,value))
for key,value in biaozhu_dict.items():
	print("biaozhu %s %d"%(key,value))

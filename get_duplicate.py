# get repeated area 
def get_chong(a,b,a1,b1):
	
	if not (b > a  and b1 > a1):
		print("warnning, wrong input format")
		return 0
	all_len = b-a +b1-a1
	if a1<=a:
		if b1 <=a:
			return 0
		elif b1<=b:
			return 2*(b1-a)/all_len
		elif b1>b:
			return 2*(b-a)/all_len
		else: 
			return 0

	elif a1 <b :
		if b1 <=b:
			return 2*(b1-a1)/all_len
		elif b1>=b:
			return  2*(b-a1)/all_len
		else:
			return 0
	elif a1>b:
			return 0
			

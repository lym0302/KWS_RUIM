
keywords = ["鸡巴","鸡巴娃儿","鸡巴卵","大鸡吧","像坨屎","像头猪","日你妈","日你妹","日妈哟","日你先人","日你仙人","傻逼","逗逼","哈鸭儿","哈儿","牙刷得很","牙儿得很","哈麻批","贱麻批","烂麻批","妈卖批","滚你妈卖批","杀人","杀死","贱人","贱相","贱货","杂种","狗杂种","杂皮","龟儿子","龟孙","龟孙子","瓜西西的","保批龙","杀人了","杀人啦","杀死人了","杀死人","你个杂种","杂菜","狗杂皮","像头猪一样","像坨屎一样","哈婆娘","烂批烂胩","烂批","烂胩","死婆娘","烂婆娘","逗比","老杂皮","哈","杀死你","瓜兮兮的","他妈的","狗日的","烂哈婆娘","贱婆娘"]



with open("transcript_all.txt","r") as f:
	for line in f.readlines():
		vols =  line.replace("\n","").split(" ")[1:]
		for  vol in vols:
#			print(vol)
			for keyword in keywords:
				if keyword == vol:
					print("equal:%s"%vol)
					pass
				elif(keyword in vol):
					print(vol)
					print(" ".join(vol.split(keyword)))
					


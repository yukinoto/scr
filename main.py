import sys
import requests
import time

#url=sys.argv[1]
url='http://10.20.37.118'

class token:
	def __init__(self,url,client_id,uid):
		self.url=url
		self.__client_id=client_id
		self._uid=uid
		self.beft=time.time()
	def shoot(self,x,y,col):
		if time.time()-self.beft<30:
			time.sleep(30-time.time()+self.beft)
		data={'x':x,'y':y,'color':col}
		headers={'referer':'https://www.luogu.com.cn/paintBoard','user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36',
		'cookie':'__client_id='+self.__client_id+';_uid='+self._uid}
		res=requests.post(url+'/paintBoard/paint',data=data,headers=headers,timeout=10)
		self.beft=time.time()
		return res

g=[]
for i in range(10):
	g.append(token(url,str(i),str(i)))

now=0
while True:
	if now>=10:
		now=0
	print(g[now].shoot(1,1,1).text)
	now+=1
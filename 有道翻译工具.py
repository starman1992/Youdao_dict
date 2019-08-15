#有道翻译
import urllib.request as r
import urllib.parse as p
import json
import time

def process(url,data):
    #使用urlencode方法转换标准格式
    data = p.urlencode(data).encode('utf-8')
    #先定义header则需要在()中加入',head',后定义不用
    req = r.Request(url,data)   
        #后定义header则需要用到add_header函数
    req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
                    (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36')
    #传递Request对象和转换完格式的数据
    response = r.urlopen(req,data)
    #读取信息并解码
    html = response.read().decode('utf-8')
    #使用JSON
    target =json.loads(html)
    return target
    
def Youdao(onlyone=1,content=None):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    #去掉translate_o中的_o 可用
    ###先定义header
    ##head = {}
    ##head['User-Agent']= 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36\
    ##                    (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

    data = {}
    data['from']= 'AUTO'
    data['to']= 'AUTO'
    data['smartresult']= 'dict'    
    data['doctype']= 'json'
    data['version']= '2.1'
    data['keyfrom']= 'fanyi.web'
    data['action']= 'FY_BY_REALTlME'

    while onlyone==1:
        data['i'] = input('请输入要翻译的内容(输入"q!"结束)：')
        if data['i'] == 'q!':
            break
             
        target = process(url,data)
        print("有道翻译结果：%s" % (target['translateResult'][0][0]['tgt']))
        time.sleep(3)   #系统休息3秒钟
    

##url='http://www.whatismyip.com'
##
###如果用requests库可考虑下面方法
###response = requests.get('http://httpbin.org/ip',proxies={'http':'http://127.0.0.1:1080'})
##proxy_support= r.ProxyHandler({'http':'192.6.144.73:81'})
##opener = r.build_opener(proxy_support)
###opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36')]
##
##r.install_opener(opener)
##
##response = r.urlopen(url)
##html = response.read().decode('utf-8')
##
##print(html)
##






















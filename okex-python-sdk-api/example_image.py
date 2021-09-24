import urllib.request  #导入用于打开URL的扩展库模块
import urllib.parse
import re    #导入正则表达式模块
import requests
import certifi

headers={
  "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
  "Accept-Encoding": "gzip, deflate, br",
  "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
  "Connection":"keep-alive",
  "Host":  "36kr.com/newsflashes",
  "Upgrade-Insecure-Requests":"1",
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:55.0) Gecko/20100101 Firefox/55.0"
}

headers2 = {
    "Referer": "https://renren.com/album/843956671",
    "sec-ch-ua":'"Google Chrome";v="93", " Not;A Brand";v="99", "Chromium";v="93"',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "macOS",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}

def open_url(url):
  req=urllib.request.Request(url)   #将Request类实例化并传入url为初始值，然后赋值给req
  #添加header，伪装成浏览器
  req.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
  #.add_header('User-Agent','Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36 SE 2.X MetaSr 1.0')
  #访问url，并将页面的二进制数据赋值给page
  page=urllib.request.urlopen(req,cafile=certifi.where())
  #将page中的内容转换为utf-8编码
  html=page.read().decode('utf-8')

  print(html)
  return html

def open_url1(url):
    data = requests.get(url, headers=headers2)
    print( data.text)


def get_img(html):
  # [^"]+\.jpg 匹配除"以外的所有字符多次,后面跟上转义的.和png
  p=r'<img src="([^"]+\.jpg)"'
  #返回正则表达式在字符串中所有匹配结果的列表
  imglist=re.findall(p,html)

  #循环遍历列表的每一个值
  for each in imglist :
    print("1234567")
    #以/为分隔符，-1返回最后一个值
    filename=each.split("/")[-1]
    #访问each，并将页面的二进制数据赋值给photo
    photo=urllib.request.urlopen(each )
    w=photo.read()
    #打开指定文件，并允许写入二进制数据
    f=open('/Users/wujinquan/workspace/ex/V3-Open-API-SDK/okex-python-sdk-api/'+filename+'.jpg','wb')
    #写入获取的数据
    f.write(w)
    #关闭文件
    f.close()

def post():

    # 使用session共享cookie(一次post一次get，必须是同一个session)

    #url = "http://www.renren.com/login?to=http%3A%2F%2Fwww.renren.com%2F"
    url = "http://rrwapi.renren.com/account/v1/loginByPassword"
    #url = "http://www.renren.com/PLogin.do"

    # 这里的email 和 password 都需要填写自己的账号密码这样才能够模拟浏览器发送登录请求
    # 我这里 未写，你们需要自己写入
    data = {"user": "18627434480", 'password': "cyl900731"}
    data = {
        "appKey": "bcceb522717c2c49f895b561fa913d10",
        "callId": "1632073990775",
        "password": "b6ea505f949fcf3ba4cc7f5285c12a2d",
        "sessionKey": "",
        "sig": "0666ae3888c5ea0338c74255dec91bcf",
        "user": "18627434480"
    }
    #data = {"email": "18627434480", 'password': "b6ea505f949fcf3ba4cc7f5285c12a2d"}

    headers = {
        'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36"
    }

    # 登录:session.post
    session = requests.session()
    session.post(url, data=data, headers=headers)

    # 使用登录过的session访问大鹏个人中心:session.get
    resp = session.get('http://www.renren.com/album/843954099', headers=headers)

    print(resp.text)


#该模块既可以导入到别的模块中使用，另外该模块也可自我执行
if __name__=='__main__':
  #定义url
  #url="http://findicons.com/pack/2787/beautiful_flat_icons"
  #url="https://renren.com/album/843956671"
  url="https://hm.baidu.com/hm.js?ad6b0fd84f08dc70750c5ee6ba650172"
  #url="https://renren.com/static/js/chunk-vendors.70d5c2f408b27bd31dfdb7d7c5e5d584cd125b58e277df1cf68190a0cfc120cb6476ba70ec76a0adcbfbeec7dfc4882f5bb3051581a188cd9bf7660e8e651b44.js"
  #open_url(url)
  #open_url(url)
  #将url作为open_url()的参数，然后将open_url()的返回值作为参数赋给get_img()
  #get_img(open_url(url))
  post()

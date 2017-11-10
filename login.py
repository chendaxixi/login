import urllib
import urllib2
requrl = "https://net.tsinghua.edu.cn/do_login.php"
headers = {
    "Host": "net.tsinghua.edu.cn",
    "Connection": "Keep-Alive",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Accept-Language": "zh-CN,zh;q=0.8",
    "Accept-Encoding": "gzip, deflate",
    "Referer": "https://net.tsinghua.edu.cn/wireless/",
    "Origin": "https://net.tsinghua.edu.cn",
    "X-Requested-With": "XMLHttpRequest",
    "Accept": "*/*",
    "User-Agent": "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    }
data = {
    "action": "login",
    "username": "用户名",
    "password": "{MD5_HEX}密码的md5加密",
    "ac_id": "1"
    }
data_urlencode = urllib.urlencode(data)
req = urllib2.Request(url=requrl, data=data_urlencode, headers=headers)
res_data = urllib2.urlopen(req)
print res_data.read()

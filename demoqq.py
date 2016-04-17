import urllib,httplib,md5,time
class qq:
    def __init__(self,qq="",pwd=""):
        self.pwd=md5.new(pwd).hexdigest()
        self.headers=""
        self.qq=qq

    def getdata(self):
        self.conn= httplib.HTTPConnection("tqq.tencent.com:8000")#这里是tqq.tencent.com的ip地址，也可以直接用域名
        self.conn.request("POST","", self.headers)
        response = self.conn.getresponse()                                     
        print(response.read().decode('utf-8').encode("cp936"))
        self.conn.close

    def Login(self):#登陆
        self.headers=("VER=1.0&CMD=Login&SEQ="+\r
                      str(int(time.time()*100)%(10**5))+"&UIN="+\r
                      self.qq+"&PS="+\r
                      self.pwd+\r
                      "&M5=1&LC=9326B87B234E7235")
        self.getdata()     
         
         
    def Query_Stat(self):#在线好友
        self.headers=("VER=1.0&CMD=Query_Stat&SEQ="+\r
                      str(int(time.time()*100)%(10**5))+"&UIN="+\r
                      self.qq+"&TN=50&UN=0")
                       
        self.getdata()
         
    def List(self):#好友列表
        self.headers=("VER=1.0&CMD=List&SEQ="+\r
                      str(int(time.time()*100)%(10**5))+"&UIN="+\r
                      self.qq+"&TN=160&UN=0")
         
        self.getdata()
 
 
    def GetInfo(self,friend=""):#指定QQ号码的详细内容
        self.headers=("VER=1.0&CMD=GetInfo&SEQ="+\r
                      str(int(time.time()*100)%(10**5))+"&UIN="+\r
                      self.qq+"&LV=2&UN="+\r
                      friend)
         
        self.getdata()
 
 
    def AddToList(self,friend=""):#增加指定QQ号码为好友
        self.headers=("VER=1.0&CMD=AddToList&SEQ="+\r
                      str(int(time.time()*100)%(10**5))+"&UIN="+\r
                      self.qq+"&UN="+\r
                      friend)
         
        self.getdata()
 
 
    def GetMsg(self):#获取消息
        self.headers=("VER=1.0&CMD=GetMsgEx&SEQ="+\r
                      str(int(time.time()*100)%(10**5))+"&UIN="+\r
                      self.qq)
         
        self.getdata()
 
 
    def SendMsg(self,friend="",msg=""):#发送消息
        self.headers=("VER=1.0&CMD=CLTMSG&SEQ="+\r
                      str(int(time.time()*100)%(10**5))+"&UIN="+\r
                      self.qq+"&UN="+\r
                      friend+"&MG="+\r
                      msg.decode("cp936").encode('utf-8'))
         
        self.getdata()
 
 
    def Logout(self):#退出登陆 http://yige.org
        self.headers=("VER=1.0&CMD=Logout&SEQ="+\r
                      str(int(time.time()*100)%(10**5))+"&UIN="+\r
                      self.qq)
         
        self.getdata()
 
 
test=qq('号码','密码')
test.Login()
test.Query_Stat()
test.List()
test.GetInfo('他人QQ号码')
test.AddToList('他人QQ号码')
test.GetMsg()
i=0
while i<1000:
    print i
    time.sleep(0.9)
    test.SendMsg('他人QQ号码',"一共有1000条消息，这是第"+str(i)+"条消息")
    i = i+1
test.Logout()
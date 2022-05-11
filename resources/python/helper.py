import os,json,datetime

def getfiles():
    return (os.environ["TMPFILE"], os.environ["UPLOADEDFILE"])

def getcontentfile() : 
    return open(os.environ["CONTENTFILE"],"w+")

def getjson():
    (t, u) = getfiles()
    with open(u) as f:
        return json.load(f)

def writerest(s):
    (t, u) = getfiles()
    with open(t, "w+") as f:
        ss = json.dumps(s)
        f.write(ss)

def writedone(text=False) :
    res = { 'notification' : 
               { 'kind' : 'success',
                 'title' : { 'message' : 'done'},
                'description': {'message' : 'reportisready'} }
              }
    if text : res["text"] = True
    writerest (res)

class WJON :

  def __init__(self,jss=getjson()) :
    self.js = jss
    print(self.js)

  def haskey(self,n) :
    return n in self.js

  def get(self,n,defa=None) :
    if self.haskey(n): return self.js[n]
    else: return defa

  def getnumber(self,n) :
    s = self.get(n)
    if s is None : return s
    if isinstance(s, str) or  isinstance(s, unicode) : s = float(s)
    return s

  def getdate(self,n) :
    s = self.get(n)
    if s is None : return s
    return datetime.datetime.strptime(s,'%Y-%m-%d').date()
  
  def getdaterange(self,n) :
    s = self.get(n)
    if s is None : return s
    d1 = None if s[0] is None else datetime.datetime.strptime(s[0],'%Y-%m-%d').date()
    d2 = None if s[1] is None else datetime.datetime.strptime(s[1],'%Y-%m-%d').date()
    return [d1,d2]  

  def incheckbox(self,check,val) :
    if not self.js.has_key(check): return False
    return val in self.js[check]

  def dajchecklista(self,check) :
    return self.get(check,[])


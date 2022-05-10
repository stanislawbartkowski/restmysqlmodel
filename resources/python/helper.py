import os,json

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
        print(s)
        ss = json.dumps(s)
        print(ss)
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

  def __init__(self) :
    self.js = getjson()
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


  def incheckbox(self,check,val) :
    if not self.js.has_key(check): return False
    return val in self.js[check]

  def dajchecklista(self,check) :
    return self.get(check,[])


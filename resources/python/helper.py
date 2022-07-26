import os,json,datetime,logging,sys
import tempfile, shutil


# -------------
# TODO: REMOVE
# -------------

class XWJON :

  def __init__(self,js=None) :
    if js is None : js = getjson()
    self.js = js
    print(self.js)

  def haskey(self,n) :
    return n in self.js

  def get(self,n,defa=None) :
    if self.haskey(n): return self.js[n]
    else: return defa

  def getnumber(self,n) :
    s = self.get(n)
    if s is None : return s
    if isinstance(s, str) : s = float(s)
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
    pass

# ===================================    

# -------------------------
# Python3 specific
# -------------------------

def getuploadfile() :
   return os.environ["UPLOADEDFILE"]

def encodeutf8(s) :
  return s

def _tmpfile() :
  return os.environ["TMPFILE"]

def getfiles():
    return (_tmpfile(), os.environ["UPLOADEDFILE"])

def getcontentfile() : 
    return open(os.environ["CONTENTFILE"],"w+")

def getpar(p) :
  print("getpar="+p)
  val = os.environ[p]
  print(val)
  return val


# --------------
# logger
# -------------

def getlog(name) :
  log = logging.getLogger(name)
  log.setLevel(logging.DEBUG)
  stream = logging.StreamHandler(sys.stdout)
  stream.setLevel(logging.DEBUG)
  log.addHandler(stream)
  return log

_logg = getlog(__name__)

# ------------------
# common procs
# ------------------


def printlink(res,text=False) :
  dir = "/tmp/links"
  if not  os.path.isdir(dir) : os.mkdir(dir)
  z = tempfile.mkstemp(dir=dir,suffix=".txt" if text else ".html")
  sou = os.environ["CONTENTFILE"]
  fname = z[1]
  p = fname[1:].find("/")
  link = fname[p+1:]
  _logg.info("Copy {0} to {1}".format(sou,fname))
  shutil.copy(sou,fname)
  res["printlink"] = link


def getform():
    u = getuploadfile()
    with open(u) as f:
        return json.load(f)

def getjson():
    return getform()

def writerest(s) :
    t = _tmpfile()
    with open(t, "w+") as f:
        ss = json.dumps(s)
        f.write(ss)
        _logg.debug(s)

def writedone(text=False) :
    res = { 'notification' : 
               { 'kind' : 'success',
                 'title' : { 'message' : 'done'},
                'description': {'message' : 'reportisready'} }
              }
    if text : res["text"] = True
    printlink(res,text)
    writerest (res)

def toiso(s) :
  a = s.split('-')
  return datetime.date(int(a[0]),int(a[1]),int(a[2]))        

def gettmpdir() :
  return tempfile.gettempdir()

def fileintmpdir(f) :
  dir = gettmpdir()
  return os.path.join(dir,f)

def uploadfile() :
  filename = getpar("filename")
  _logg.info("Uploaded filename {0}".format(filename))
  upname = fileintmpdir(filename)
  head_tail = os.path.split(upname)
  dir = head_tail[0]
  try:
    os.mkdir(dir)
  except OSError as error:
    _logg.info("Directory {0} exists".format(dir))
  _logg.info("Copy {0} to {1}".format(getuploadfile(),upname))
  shutil.copyfile(getuploadfile(), upname)


#---------------

class _WWJON :

  def __init__(self,jss) :
    if jss is None: jss=getform()
    self.js = jss
    _logg.debug("WJON {0}".format(self.js))
#    print(self.js)

  def getnumber(self,n) :
    s = self.get(n)
    if s is None : return s
    if isinstance(s, str) : s = float(s)
    return s

  def set(self,n,v) :
    self.js[n] = v

  def haskey(self,n) :
    return self.js.get(n) is not None

  def getl(self,n) :
    a = self.get(n,[])
    return a

  def get(self,n,defa=None) :
    return self.js[n] if self.haskey(n) and self.js[n] is not None  else defa

  def gets(self,n,defa=None) :
    s = self.get(n,defa)
    if s is None: return s
    return encodeutf8(s)


  def isnone(self,n) :
    return self.get(n) is None

  def getd(self,n,defa=None) :
    da = self.get(n,defa)
    if da is None: return None
    return toiso(da)
# Python2 error - is not working in embedded Python    
#    return datetime.datetime.strptime(da, '%Y-%m-%d').date()

  def incheckbox(self,check,val) :
    if not self.haskey(check): return False
    return val in self.js[check]

  def dajchecklista(self,check) :
    return self.get(check,[])

  def writevars(self,f,var) :
    a = var if type(var) == list else [var]
    for v in a :
      s = self.gets(v,"")
      f.write("{0} : {1} \n".format(v,s))

  def writevarl(self,f,var) :
    a = var if type(var) == list else [var]
    for v in a :
      l = self.get(v,None)
      if l is None: f.write("{0} - wartosc logiczna pusta".format(v))
      else: f.write("{0} : wartosc logiczna {1} \n".format(v,"true" if l else "false"))


class UL :

  def __init__(self) :
    self.list = []

  def adds(self,s) :
    self.list.append(s)

  def addvars(self,w,var) :
    a = var if type(var) == list else [var]
    for v in a :
      self.adds("{} : {}".format(v,w.gets(v,None)))

  def addvar(self,w,var) :
    a = var if type(var) == list else [var]
    for v in a :
      self.adds("{} : {}".format(v,w.get(v,None)))

  def tos(self) :
    res = "<ul>"
    for s in self.list: res = res + "<li>" + s + "</li>"
    return res + "</ul>"

# ===========================

class WJON(_WWJON) :

  def __init__(self,js=None) :
    _WWJON.__init__(self,js)

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
    
    
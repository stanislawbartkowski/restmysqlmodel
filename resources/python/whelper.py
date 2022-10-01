import os, json, datetime, logging, sys
from typing import Dict, List
import functools
from enum import Enum

from sqlalchemy import create_engine

# ---------------
# sql
# ---------------


def dbengine():
    url = os.environ["ENV_alchemyconnect"]
    engine = create_engine(url)
    return engine


# decorator
def dbconnect(func):
    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):
        db = dbengine().connect()
        res = func(db, *args, **kwargs)
        db.close()
        return res

    return func_wrapper


# decorator
def respondrest(func):
    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):
        json: Dict = func(*args, **kwargs)
        writerest({} if json is None else json)

    return func_wrapper


# decorator
def validatefield(func):
    @functools.wraps(func)
    def func_wrapper(*args, **kwargs):
        errmess: str = func(*args, **kwargs)
        writerest({} if errmess is None else {"err": errmess})

    return func_wrapper


# ------------------
# logger
# ------------------


def getlog(name):
    log = logging.getLogger(name)
    log.setLevel(logging.DEBUG)
    stream = logging.StreamHandler(sys.stdout)
    stream.setLevel(logging.DEBUG)
    log.addHandler(stream)
    return log


_logg = getlog(__name__)

# -------------
# misc procs
# -------------


def _toiso(s):
    a = s.split("-")
    return datetime.date(int(a[0]), int(a[1]), int(a[2]))


def getuploadfile():
    return os.environ["UPLOADEDFILE"]


def _encodeutf8(s):
    return s


def _tmpfile():
    return os.environ["TMPFILE"]


def _getfiles():
    return (_tmpfile(), os.environ["UPLOADEDFILE"])


def _getcontentfile():
    return open(os.environ["CONTENTFILE"], "w+")


def getpar(p):
    val = os.environ[p]
    return val


def _getform():
    u = getuploadfile()
    with open(u) as f:
        return json.load(f)


def writerest(s: Dict):
    t = _tmpfile()
    with open(t, "w+") as f:
        ss = json.dumps(s)
        _logg.debug(ss)
        f.write(ss)


def generrfield(field: str, err: str) -> Dict:
    return {"field": field, "err": err}


def generrfields(errors: List[Dict]) -> Dict:
    if type(errors) == dict:
        errors = [errors]
    return {"error": errors}


class Notitication(Enum):
    SUCCESS = "success"


def gennotification(
    kind: Notitication, title: str, descr, close=True, refresh=True
) -> Dict:
    return {
        "close": close,
        "refresh": refresh,
        "notification": {
            "kind": kind.value,
            "title": title,
            "description": descr,
        },
    }


# -------------------
# JSON parameters
# -------------------


class WJON:
    def __init__(self, jss=None):
        if jss is None:
            jss = _getform()
        self.js = jss
        _logg.debug("WJON {0}".format(self.js))

    #    print(self.js)

    def getnumber(self, n):
        s = self.get(n)
        if s is None:
            return s
        if isinstance(s, str):
            s = float(s)
        return s

    def set(self, n, v):
        self.js[n] = v

    def haskey(self, n):
        return self.js.get(n) is not None

    def getl(self, n):
        a = self.get(n, [])
        return a

    def get(self, n, defa=None):
        return self.js[n] if self.haskey(n) and self.js[n] is not None else defa

    def gets(self, n, defa=None):
        s = self.get(n, defa)
        if s is None:
            return s
        return _encodeutf8(s)

    def isnone(self, n):
        return self.get(n) is None

    def getd(self, n, defa=None):
        da = self.get(n, defa)
        if da is None:
            return None
        return _toiso(da)

    # Python2 error - is not working in embedded Python
    #    return datetime.datetime.strptime(da, '%Y-%m-%d').date()

    def incheckbox(self, check, val):
        if not self.haskey(check):
            return False
        return val in self.js[check]

    def dajchecklista(self, check):
        return self.get(check, [])

    def writevars(self, f, var):
        a = var if type(var) == list else [var]
        for v in a:
            s = self.gets(v, "")
            f.write("{0} : {1} \n".format(v, s))

    def writevarl(self, f, var):
        a = var if type(var) == list else [var]
        for v in a:
            l = self.get(v, None)
            if l is None:
                f.write("{0} - wartosc logiczna pusta".format(v))
            else:
                f.write(
                    "{0} : wartosc logiczna {1} \n".format(v, "true" if l else "false")
                )

    def getdate(self, n):
        s = self.get(n)
        if s is None:
            return s
        return datetime.datetime.strptime(s, "%Y-%m-%d").date()

    def getdaterange(self, n):
        s = self.get(n)
        if s is None:
            return s
        d1 = (
            None
            if s[0] is None
            else datetime.datetime.strptime(s[0], "%Y-%m-%d").date()
        )
        d2 = (
            None
            if s[1] is None
            else datetime.datetime.strptime(s[1], "%Y-%m-%d").date()
        )
        return [d1, d2]


# ---------------------
# UL
# ---------------------


class UL:
    def __init__(self):
        self.list = []

    def adds(self, s):
        self.list.append(s)

    def addvars(self, w, var):
        a = var if type(var) == list else [var]
        for v in a:
            self.adds("{} : {}".format(v, w.gets(v, None)))

    def addvar(self, w, var):
        a = var if type(var) == list else [var]
        for v in a:
            self.adds("{} : {}".format(v, w.get(v, None)))

    def tos(self):
        res = "<ul>"
        for s in self.list:
            res = res + "<li>" + s + "</li>"
        return res + "</ul>"


# ---------------
# DISPATCH
# ---------------


class DISPATCH:
    def __init__(self):
        self._w = WJON()
        self._d: Dict = {}

    def registerwhat(self, what: str, func):
        self._d[what] = func

    def execute(self):
        what = getpar("what")
        func = self._d.get(what)
        if func is None:
            _logg.fatal("Cannot find dispatch for {what}")
            return
        func(self._w)
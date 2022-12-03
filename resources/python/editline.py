from whelper import *
from typing import List, Dict, Set
import testtable


LISTITEMS = "listitems"


@respondrest
def REMOVE_initvalues():
    val = [
        {"id": 1111, "name": "Abacki"},
        {"id": 2222, "name": "Babacki"},
    ]
    return {"listitems": val}


@respondrest
@dbconnect
def initvalues(db):
    query = "SELECT * FROM test"
    result = db.execute(query)
    res = result.fetchall()

    val = [{"id": e[0], "name": e[1]} for e in res]

    return {"listitems": val}


@respondrest
def _addline(w):
    ta: List[Dict] = w.get(LISTITEMS)
    ta.append({})
    print(ta)
    return {"vars": {LISTITEMS: ta}}


def _findpos(w, ta: List[Dict]) -> int:
    i: int = 0
    rowkey: int = w.getrowkey(LISTITEMS)
    for i in range(0, len(ta)):
        if rowkey == ta[i]["rowkey"]:
            return i


def _checkvalidity(ta : List[Dict]) :
    err = []
    for rowkey in range(0, len(ta)) :
        id = ta[rowkey]["id"]
        if id < 0 : 
            idpos = getedittablepos(LISTITEMS,"id",rowkey)
            err.append(generrfield(idpos, directmess="The number cannot be negative"))
    return None if len(err) == 0 else err

@respondrest
@dbsession
def _add(session, w):
    ta: List[Dict] = w.get(LISTITEMS)
    err : List[Dict] = _checkvalidity(ta)
    if err is not None :
        return generrfields(err)
    session.begin()
    session.execute("TRUNCATE TABLE test")
    for w in ta :
        id = w["id"]
        name = w.get("name")
        testtable.addrow(session,id,name)
    session.commit()

@validatefield
def _validateid(w):
    rowkey: int = w.getcurrentrowkey()
    id: int = w.getcurrent()
    ta: List[Dict] = w.get(LISTITEMS)
    for t in ta:
        if t["rowkey"] == rowkey:
            continue
        curid: int = t.get("id")
        if curid is not None and curid == id:
            return "duplicatedvalue"


@respondrest
def _delete(w):
    ta: List[Dict] = w.get(LISTITEMS)
    ind: int = _findpos(w, ta)
    print(ind)
    del ta[ind]
    return {"vars": {LISTITEMS: ta}}


@respondrest
def _insert(w):
    ta: List[Dict] = w.get(LISTITEMS)
    ind: int = _findpos(w, ta)
    print(ind)
    ta.insert(ind, {})
    return {"vars": {LISTITEMS: ta}}


if __name__ == "__main__":
    D = DISPATCH()
    D.registerwhat("addline", _addline)
    D.registerwhat("add", _add)
    D.registerwhat("validateid", _validateid)
    D.registerwhat("delete", _delete)
    D.registerwhat("insert", _insert)
    D.execute()

from whelper import *
import testtable

@respondrest
@dbconnect
def _testid(db,w):
      exist : bool = testtable.idexist(db,w.get('id'))
      return {"res" : "Exist" if exist else "Not exist"}

@respondrest
@dbconnect
def _deleteid(db,w):
    testtable.delrow(db,w.get('id'))

@respondrest
@dbconnect
def _addid(db,w):
    testtable.addrow(db,w.get('id'),w.get('name'))

if __name__ == "__main__":
    D = DISPATCH()
    D.registerwhat("testid", _testid)
    D.registerwhat("deleteid", _deleteid)
    D.registerwhat("addid", _addid)
    D.execute()

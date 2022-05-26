import os, sys, json
import jaydebeapi
from helper import *

# CREATE TABLE TEST (ID INT NOT NULL PRIMARY KEY, NAME VARCHAR(100));

def getfiles():
    return (os.environ["TMPFILE"], os.environ["UPLOADEDFILE"])

def getcontentfile() : 
    return open(os.environ["CONTENTFILE"],"w+")


def getconn():
    url = os.environ["ENV_url"]
    user = os.environ["ENV_user"]
    password = os.environ["ENV_password"]
    driverclass = os.environ["ENV_driverclass"]
    jdbcjar = os.environ["ENV_jdbcjar"]

    return jaydebeapi.connect(driverclass,url,[user,password],jdbcjar)

def getjson():
    (t, u) = getfiles()
    with open(u) as f:
        return json.load(f)

def writerest(s):
    (t, u) = getfiles()
    with open(t, "w+") as f:
        ss = json.dumps(s)
        print(ss)
        f.write(ss)

def iduniq() :
    da = getjson()
    print(da)
    id = da["id"]
    with getconn() as conn:
        with conn.cursor() as curs:
            curs.execute("SELECT ID FROM TEST WHERE ID=%s" % id)
            row = curs.fetchone()
            return row == None

def checkid() :
    if iduniq() : 
        writerest({})
        return True
    writerest({ 'error': [{ 'field' : 'id', 'err' : {'message' : 'duplicatedvalue' }}]})
    return False

def stepcheckid() :
    if iduniq() : 
        descr = "<H1> You are about to add new entry to testtable table</H1>"
        writerest({"next" : True, "vars" : {"descr" : descr}})
        return
    writerest({ 'error': [{ 'field' : 'id', 'err' : {'message' : 'duplicatedvalue' }}]})
 

# curs.execute("insert into CUSTOMER values (?, ?)", (1, 'John'))

def testsubmit() :
    print("submit")
    row = getjson()
    print(row)
    writerest({ 'error': [{ 'field' : 'id', 'err' : {'messagedirect' : 'Złe pole' }}]})


def get(row,key) :
    p = row.get(key)
    return p if p else ""

def submit() :
    if not checkid() : return
    row = getjson()
    print(row)
    id = row["id"]
    name = row.get("name")
    with getconn() as conn:
        with conn.cursor() as curs:
            if name == None: sql = "insert into TEST values ( %s, NULL )" % id
            else : sql = "insert into TEST values (%s ,'%s')" % (id,name)
            print(sql)
            curs.execute(sql)
            writerest ({ 'notification' : 
                { 'kind' : 'success',
                'title' : { 'message' : 'done'},
                'description': {'message' : 'youadded', 'params' : [id]} }
             })

def report() :
    row = getjson()
    print(row)
    writerest ({ 'notification' : 
                { 'kind' : 'success',
                'title' : { 'message' : 'done'},
                'description': {'message' : 'reportisready'} }
             })
    customerorder = row["customernumber"]
    orderdate = get(row,"orderdate")
    with getcontentfile() as f:
        f.write("My Report")
        f.write("<br/>")        
        f.write("<br/>"+customerorder)
        f.write("<br/>"+orderdate)
        f.write(str(row))
            
if __name__ == '__main__':
    what = sys.argv[1]
    print(what)
    if what == "checkid": checkid()
    if what == "submit": submit()
    if what == "report": report()
    if what == "stepcheckid" : stepcheckid()

import os, sys, json
import jaydebeapi

# CREATE TABLE TEST (ID INT NOT NULL PRIMARY KEY, NAME VARCHAR(100));

def getfiles():
    return (os.environ["TMPFILE"], os.environ["UPLOADEDFILE"])

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
    id = da["row"]["id"]
    with getconn() as conn:
        with conn.cursor() as curs:
            curs.execute("SELECT ID FROM TEST WHERE ID=%s" % id)
            row = curs.fetchone()
            return row == None

def checkid() :
    if iduniq() : 
        writerest({})
        return True
    writerest({ 'action': 'NO', 'error': [{ 'field' : 'id', 'mess' : 'duplicatedvalue' }]})
    return False

# curs.execute("insert into CUSTOMER values (?, ?)", (1, 'John'))

def submit() :
    print("submit")
    row = getjson()
    print(row)
    writerest({ 'action': 'NO', 'error': [{ 'field' : 'id', 'mess' : 'duplicatedvalue' }]})


def xsubmit() :
    if not checkid() : return
    row = getjson()["row"]
    print(row)
    id = row["id"]
    name = row.get("name")
    with getconn() as conn:
        with conn.cursor() as curs:
            if name == None: sql = "insert into TEST values ( %s, NULL )" % id
            else : sql = "insert into TEST values (%s ,'%s')" % (id,name)
            print(sql)
            curs.execute(sql)


if __name__ == '__main__':
    what = sys.argv[1]
    if what == "checkid": checkid()
    if what == "submit": submit()

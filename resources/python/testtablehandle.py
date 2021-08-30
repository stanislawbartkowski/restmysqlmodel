import os, sys, json
import jaydebeapi


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

def checkid() :
    da = getjson()
    print(da)
    id = da["row"]["id"]
    with getconn() as conn:
        with  conn.cursor() as curs:
            curs.execute("SELECT ID FROM TEST WHERE ID=%s" % id)
            row = curs.fetchone()
            print(row)
            if row == None: writerest({})
            else : writerest({ 'action': 'FORM', 'formaction': 'NO'})

if __name__ == '__main__':
    what = sys.argv[1]
    if what == "checkid": checkid()

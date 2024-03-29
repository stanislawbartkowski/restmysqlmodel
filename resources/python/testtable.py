from sqlalchemy.sql import text

from whelper import (
    DISPATCH,
    Notitication,
    dbconnect,
    generrfield,
    generrfields,
    gennotification,
    printcontent,
    respondrest,
    validatefield,
    wjon,
)


# CREATE TABLE TEST (ID INT NOT NULL PRIMARY KEY, NAME VARCHAR(100));

# -------------------
# helper functions
# -------------------


def addrow(conn, id: int, name: str):
    statement: str = text(
        "INSERT INTO test VALUES(:id,:name)"
        if name
        else "INSERT INTO test VALUES(:id,NULL)"
    )
    conn.execute(statement, {"id": id, "name": name})


def delrow(conn, id: int):
    statement: str = text("DELETE FROM test WHERE id= :id")
    conn.execute(statement, {"id": id})


def idexist(conn, id: int) -> bool:
    query = text("SELECT COUNT(*) FROM test WHERE id = :id")
    result = conn.execute(query, {"id": id})
    c: int = result.fetchone()[0]
    return c == 1


# ------------
# response
# ------------


@validatefield
@dbconnect
def _validateid(db, w):
    return "duplicatedvalue" if idexist(db, w.get("id")) else None


@respondrest
@dbconnect
def _addid(db, w):
    id: int = w.get("id")
    name: str = w.get("name")
    if idexist(db, id):
        err: dict = generrfield("id", "duplicatedvalue")
        return generrfields(err)
    addrow(db, id, name)
    return gennotification(
        Notitication.SUCCESS,
        "done",
        {"message": "youadded", "params": [id]},
        searchF={"id": id},
    )


@printcontent(text=True)
@dbconnect
def _printtest(db, f, li=None, title=None):
    if title:
        f.write("=== {0} ===\n".format(title))
    else:
        f.write("============================\n")

    result = db.execute(text("SELECT * FROM test"))

    no: int = 0
    for row in result:
        id = row[0]
        if li is not None and id not in li:
            continue
        name = row[1]
        f.write("{0} - {1} \n".format(id, name))
        no = no + 1

    if no == 0:
        f.write("  -- EMPTY CONTENT\n")
    f.write("============================\n")
    f.write("THE END\n")


def printall():
    _printtest()


@wjon
def printselected(w):
    l = w.getl("multichoice")
    _printtest(l)


@wjon
def printidmultiselect(w):
    l = w.getl("idchoice")
    title = w.get("title")
    _printtest(l, title=title)


@respondrest
def _updatestepsinit(w):
    return {
        "infoupdate": "<h3>You are about to modify the data.</h3> <p>Verify the data before submitting</p>"
    }


@respondrest
def _updatestepsstep1(w):
    return {
        "beforeupdate": "<h3>Check last time the data before update. There is no way back.</h3>",
        "next": True,
    }


@respondrest
def _updatestepsstep2init(w):
    return {"beforeupdate2": "<h1>Hello before update</h1>"}


@respondrest
@dbconnect
def _addstep1(db, w):
    if not idexist(db, w.get("id")):
        return {
            "vars": {
                "descr": "<H1> You are about to add new entry to testtable table</H1>",
            },
            "next": True,
        }
    err: dict = generrfield("id", "duplicatedvalue")
    return generrfields(err)


if __name__ == "__main__":
    D = DISPATCH()
    D.registerwhat("validateid", _validateid)
    D.registerwhat("addid", _addid)
    D.registerwhat("updatestepsinit", _updatestepsinit)
    D.registerwhat("updatestepsstep1", _updatestepsstep1)
    D.registerwhat("updatestepsstep2init", _updatestepsstep2init)
    D.registerwhat("addstep1", _addstep1)

    D.execute()

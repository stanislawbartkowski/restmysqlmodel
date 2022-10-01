from whelper import *
from sqlalchemy.sql import text

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


# response


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
        err: Dict = generrfield("io", "duplicatedvalue")
        return generrfields(err)
    addrow(db, id, name)
    #    return {
    #        "close": True,
    #        "refresh": True,
    #        "notification": {
    #            "kind": "success",
    #            "title": "done",
    #            "description": {"message": "youadded", "params": [id]},
    #        },
    return gennotification(
        Notitication.SUCCESS, "done", {"message": "youadded", "params": [id]}
    )


if __name__ == "__main__":
    D = DISPATCH()
    D.registerwhat("validateid", _validateid)
    D.registerwhat("addid", _addid)

    D.execute()

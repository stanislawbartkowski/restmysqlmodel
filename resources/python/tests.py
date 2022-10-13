from whelper import *

@respondlist
def getitems():

    list = []
    list.append({"id": "shipped", "name": "Name shipped"})
    list.append({"id": "delayed", "name": "Name delayed"})
    return list


@respondrest
def _getinitvalues():
    return {"id": "9999", "name": "I'm initiated as Python"}


@printcontent()
@wjon
def _printinitvalues(w, f):

    id = w.getnumber("id")
    name = w.get("name")
    f.write(f"id : {id} !\n")
    f.write(f"name : {name} !\n")


if __name__ == "__main__":
    D = GETDISPATCH()
    D.registerwhat("getinitvalues", _getinitvalues)
    D.registerwhat("printinitvalues", _printinitvalues)
    D.execute()

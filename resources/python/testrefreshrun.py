from whelper import *

@respondrest
def _testapiinit() :
    res = {}
    res["name"] = "XXXXXXX"
    res["descr"] = "<h3>Initialy set as empty and XXXXXX</h3> <br> Should retains new values after coming back from next step"
    return res

@respondrest
def _nextstep() :    
    res = {}
    res["infostep2"] = "<h1>This information is set after clicking next button in previous step</h1>"
    vars = { "vars" : res, "next" : True}
    return vars

@respondlist
@wjon
def _gettestdata(w) :
    name = w.get("name","<undefined>")
    table = []
    table.append({"id" : 1, "name": name})
    return table


if __name__ == '__main__':
    D = GETDISPATCH()
    D.registerwhat("testapiinit",_testapiinit)
    D.registerwhat("nextstep",_nextstep)
    D.registerwhat("gettestdata",_gettestdata)
    D.execute()
    

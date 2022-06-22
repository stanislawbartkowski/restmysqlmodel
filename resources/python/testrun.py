import os, sys, json
from helper import *

def testapiinit() :
    res = {}
    res["name"] = "XXXXXXX"
    res["descr"] = "<h3>Initialy set as empty and XXXXXX</h3> <br> Should retains new values after coming back from next step"
    
    writerest(res)

def nextstep() :    
    res = {}
    res["infostep2"] = "<h1>This information is set after clicking next button in previous step</h1>"
    vars = { "vars" : res, "next" : True}
    writerest(vars)

if __name__ == '__main__':
    what = getpar('what')
    if what == "testapiinit" : testapiinit()
    if what == "nextstep" : nextstep()
    

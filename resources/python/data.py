import os, sys, json
from helper import *

def employeedetails() :
    w = WJON()
    name = w.get("firstname")
    res = { "vars": { "helloname" : "<h3>Hello " + name + "</h3>" }}
    writerest(res)

if __name__ == '__main__':
    what = getpar('what')
    if what == "getdetailsemployee" : employeedetails()

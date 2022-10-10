from whelper import *


@printcontent(text=True)
@wjon
def printorders(w, f):

    f.write("Customer orders for the following ranges of customers:\n")
    list = w.get("names")
    if list is None or len(list) == 0:
        f.write("   (all customers)")
    else:
        for e in list:
            ew = WJON(e)
            name1 = ew.get("name1", "")
            name2 = ew.get("name2", "")
            f.write("From: {} to {} \n ".format(name1, name2))

@printcontent()
@wjon
def report(w,f) :
    customerorder = w.get("customernumber","")
    orderdate = w.get("orderdate","")

    f.write("My Report")
    f.write("<br/>")        
    f.write("<br/>"+customerorder)
    f.write("<br/>"+orderdate)
    w.writevarl(f,"allorders")

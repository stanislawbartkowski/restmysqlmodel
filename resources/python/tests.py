from helper import *
import sys

def getitems() :

    list = []
    list.append( {"id":"shipped", "name" : "Name shipped"} )
    list.append( {"id":"delayed", "name" : "Name delayed"} )
    res = {}
    res['res'] = list
    writerest(res)

def getinitvalues() :
    return writerest({ "id" : "9999","name" : "I'm initiated as Python"})

def printinitvalues() :
    w = WJON()
  
    with getcontentfile() as f:
      id = w.getnumber("id")
      name = w.get("name")
      f.write(f"id : {id} !\n")
      f.write(f"name : {name} !\n")
    writedone(True)         

if __name__ == '__main__':
    what = sys.argv[1]
    if what == "getitems": getitems()
    if what == "getinitvalues" : getinitvalues()
    if what == "printinitvalues" : printinitvalues()

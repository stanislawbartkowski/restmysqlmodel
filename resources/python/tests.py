import helper as h
import sys

def getitems() :

    list = []
    list.append( {"id":"shipped", "name" : "Name shipped"} )
    list.append( {"id":"delayed", "name" : "Name delayed"} )
    res = {}
    res['res'] = list
    h.writerestt(res)


if __name__ == '__main__':
    what = sys.argv[1]
    if what == "getitems": getitems()

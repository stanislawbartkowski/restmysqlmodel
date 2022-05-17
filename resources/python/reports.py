from helper import *
import sys

def printorders():
   w = WJON()

   with getcontentfile() as f:
      f.write("Customer orders for the following ranges of customers:\n")
      list = w.get("names")
      if list is None or len(list) == 0 :
         f.write("   (all customers")
      else:
         for e in list :
            ew = WJON(e)
            name1 = ew.get("name1","")
            name2 = ew.get("name2","")
            f.write('From: {} to {} \n '.format(name1,name2))


   writedone(True)         

if __name__ == '__main__':
    what = sys.argv[1]
    if what == 'printorders' : printorders()

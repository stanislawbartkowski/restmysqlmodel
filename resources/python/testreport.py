from helper import *

def report():
   w = WJON()

   with getcontentfile() as f:
      f.write("My Report\n")
      s = w.getnumber("testmoney")
      f.write(f"testmoney {s} \n")

   writedone(True)         

if __name__ == '__main__':
  report()

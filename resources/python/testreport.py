from helper import *

def report():
   w = WJON()

   with getcontentfile() as f:
      f.write("My Report\n")
      s = w.getnumber("testmoney")
      f.write(f"testmoney {s} \n")
      d = w.getdate("testdate")
      f.write(f"testdate {d}\n")
      dr = w.getdaterange("rangedate")
      f.write(f"rangedate {dr}\n")
      name1 = w.get("name1")
      name2 = w.get("name2")
      f.write(f"name1 = {name1} name2={name2}\n")


   writedone(True)         

if __name__ == '__main__':
  report()

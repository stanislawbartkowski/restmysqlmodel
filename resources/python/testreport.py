from helper import *

def report(w):

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
      namesearch = w.get("namesearch")
      f.write(f"name search = {namesearch}\n")

   writedone(True)         

def reportdynamic(w) :
   with getcontentfile() as f:
      f.write("Report from dynamic option\n")
      option = w.get('orderstatus1')
      f.write("Option:" + option + "\n" )

   writedone(True)

def uploadprint(w) :
   with getcontentfile() as f:
      f.write("Report with files uploaded\n")
      l = w.get("upload")
      for fname in l :
        f.write("======================\n") 
        f.write(fname + "\n")
        ffname = fileintmpdir(fname)
        with open(ffname) as ff :
          lines = ff.readlines()
          for l in lines:
             f.write(l + "\n")

        f.write("======================\n") 

        
   writedone(True)

if __name__ == '__main__':
   w = WJON()
   what = getpar('what')
   if what == "report" : report(w)
   if what == "dynamic" : reportdynamic(w)
   if what == "uploadprint" : uploadprint(w)

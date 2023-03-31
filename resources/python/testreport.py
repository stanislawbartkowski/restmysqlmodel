from whelper import DISPATCH, fileintmpdir, printcontent


@printcontent(text=True)
def _report(f, w):
    f.write("My Report\n")
    w.writevarn(f, "testmoney")
    d = w.getdate("testdate")
    f.write(f"testdate {d}\n")
    dr = w.getdaterange("rangedate")
    f.write(f"rangedate {dr}\n")
    name1 = w.get("name1")
    name2 = w.get("name2")
    f.write(f"name1 = {name1} name2={name2}\n")
    namesearch = w.get("namesearch")
    f.write(f"name search = {namesearch}\n")


@printcontent()
def reportdynamic(f, w):
    f.write("Report from dynamic option\n")
    option = w.get("orderstatus1")
    f.write("Option:" + (option if option is not None else "<nothing selected>") + "\n")


@printcontent(text=True)
def uploadprint(f, w):
    f.write("Report with files uploaded\n")
    l = w.get("upload")
    for fname in l:
        f.write("======================\n")
        f.write(fname + "\n")
        ffname = fileintmpdir(fname)
        with open(ffname) as ff:
            lines = ff.readlines()
            for l in lines:
                f.write(l + "\n")

            f.write("======================\n")


def multitestprint(w):
    pass


@printcontent(text=True)
def _reportinput(f, w):
    f.write("Input Report\n")
    f.write("======================\n")
    w.writevars(f, ["inputupper", "inputlower"])
    w.writerange(f, "range", "name1", "name2")
    w.writevars(f, "namesearch")


if __name__ == "__main__":
    D = DISPATCH()
    D.registerwhat("report", _report)
    D.registerwhat("dynamic", reportdynamic)
    D.registerwhat("uploadprint", uploadprint)
    D.registerwhat("multitestprint", multitestprint)
    D.registerwhat("reportinput", _reportinput)
    D.execute()

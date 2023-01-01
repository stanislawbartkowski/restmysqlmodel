from whelper import *
from typing import List, Dict, Set

LISTITEMS = "edititems"

@respondrest
def _getinitvalues():
    val = [
        {"id": 1111, "name": "Abacki"},
        {"id": 2222, "name": "Babacki"},
    ]
    return {LISTITEMS: val}

if __name__ == "__main__":
    D = GETDISPATCH()
    D.registerwhat("getinitvalues", _getinitvalues)
    D.execute()

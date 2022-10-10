from whelper import *
from typing import List, Dict
from random import random

@respondlist
def _createlist():
    t: List[Dict] = []
    sum1: float = 0
    sum2: float = 0
    for i in range(0, 60):
        val1: float = random() * 100
        val2: float = random() * 100
        sum1 += val1
        sum2 += val2
        t.append({"id": i, "val1": val1, "val2": val2})
    return (t, {"sum1": sum1, "sum2": sum2})


if __name__ == "__main__":
    _createlist()

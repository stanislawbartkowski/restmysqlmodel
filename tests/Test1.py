import unittest
from typing import Dict,List
import sys,os

sys.path.append(os.getcwd())

from tests.testmixin import TestMixin

ID=99

class DatabaseTest(unittest.TestCase, TestMixin) :

    @unittest.skip("Skipping")
    def test1(self) :
        list : List[Dict] = self._getrequestres("employee")
        print(list)
        self.assertTrue(len(list) > 1 )

    def test2(self) :
        data : Dict = {"id" : ID}
        r = self._postresttest(data, "testid")
        print(r["res"])        
        if r["res"] == "Exist" :
            r = self._postresttest(data, "deleteid")
            print(r)        
        r = self._postresttest(data, "testid")
        print(r["res"])
        self.assertEqual("Not exist",r["res"]) 
        data : Dict = {"id" : ID, "name" : "Test name"}
        r = self._postresttest(data, "addid")
        print(r)
        r = self._postresttest(data, "testid")
        print(r["res"])
        self.assertEqual("Exist",r["res"]) 



if __name__ == '__main__':
    unittest.main()          
import requests
from typing import Dict, List
import functools

BASEURL = "http://localhost:8999"


def _getparams(param: str, val: str) -> Dict:
    return None if param is None else {param: val}


class TestMixin:
    def _request(func):
        @functools.wraps(func)
        def func_wrapper(self, *args, **kwargs):
            r = func(self, *args, **kwargs)
            self.assertEqual(r.status_code, 200)
            return r.json()

        return func_wrapper

    @_request
    def _getrequest(self, meth: str) -> Dict:
        return requests.get(f"{BASEURL}/{meth}")

    def _getres(self, r):
        return r["res"]

    def _getrequestres(self, meth: str) -> Dict:
        return self._getres(self._getrequest(meth))

    @_request
    def _postrequest(self, meth: str, data: Dict, param: str = None, val: str = None) -> Dict :
        return requests.post(
            f"{BASEURL}/{meth}", params=_getparams(param, val), json=data
        )

    def _postrequestwhat(self, meth: str, data: Dict, what: str) -> Dict :
        return self._postrequest(meth, data, "what", what)

    def _postresttest(self, data: Dict, what: str) -> Dict :
        return self._postrequestwhat("testrest/testaction", data, what)

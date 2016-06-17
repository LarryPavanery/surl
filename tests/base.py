import falcon
import unittest
import surl.api.server as server
from falcon import testing

class TestBase(unittest.TestCase):

    def setUp(self):
        self.app = server.launch(None)
        self.srmock = falcon.testing.StartResponseMock()

    def simulate_request(self, path, **kwargs):
        env = falcon.testing.create_environ(path=path, **kwargs)
        return self.app(env, self.srmock)

    def simulate_get(self, *args, **kwargs):
        kwargs['method'] = 'GET'
        return self.simulate_request(*args, **kwargs)

    def simulate_post(self, *args, **kwargs):
        kwargs['method'] = 'POST'
        return self.simulate_request(*args, **kwargs)

    def simulate_put(self, *args, **kwargs):
        kwargs['method'] = 'PUT'
        return self.simulate_request(*args, **kwargs)

    def simulate_delete(self, *args, **kwargs):
        kwargs['method'] = 'DELETE'
        return self.simulate_request(*args, **kwargs)
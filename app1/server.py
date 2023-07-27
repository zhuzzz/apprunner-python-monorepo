import sys
sys.path.append('../')

import random
from libs.base import adder2
from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
import os

def hello_world(request):
    x, y = random.randint(1, 100), random.randint(1, 100)
    res = adder2.add2(x, y)
    name = os.environ.get('NAME')
    if name == None or len(name) == 0:
        name = "world"
    message = "Hello, " + name + "!\nThe sum of " + str(x) + " and " + str(y) + " is " + str(res)
    return Response(message)

if __name__ == '__main__':
    port = 8080
    with Configurator() as config:
        config.add_route('hello', '/')
        config.add_view(hello_world, route_name='hello')
        app = config.make_wsgi_app()
    server = make_server('0.0.0.0', port, app)
    server.serve_forever()

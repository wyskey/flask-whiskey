from flask_restplus import Api #part1

from .namespace1 import api as ns1 #part2 -- loop through models
from .namespace2 import api as ns2

api = Api(      # part3 -- pull from whiskey.json
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas

    doc='/api/v1'
)

api.add_namespace(ns1, path='/api/v1/cats') #part4 -- loop through models
api.add_namespace(ns2, path='/api/v1/todos')
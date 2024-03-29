# Python imports

# Lib imports

# Application imports
from .singleton import Singleton



class EndpointRegistry(Singleton):
    def __init__(self):
        self._endpoints = {}

    def register(self, rule, **options):
        def decorator(f):
            self._endpoints[rule] = f
            return f

        return decorator

    def get_endpoints(self):
        return self._endpoints

import falcon

from .images import Resource



api = application = falcon.API()
#images=Resource()
images = Resource(storage_path='.')
api.add_route('/images',images)

'''
add_route() expects an instance of the resource class, not the class itself. The same instance is used for all requests. This strategy improves performance and reduces memory usage, but this also means that if you host your application with a threaded web server, resources and their dependencies must be thread-safe.'''


#https://falcon.readthedocs.io/en/stable/user/tutorial.html


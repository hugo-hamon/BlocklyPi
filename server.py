from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer
from robot.controller.controller import Controller
from http.server import SimpleHTTPRequestHandler
import logging



# We define a custom server request handler, capable of both handling GET and XML-RPC requests.
class RequestHandler(SimpleXMLRPCRequestHandler, SimpleHTTPRequestHandler):
    rpc_paths = ('/RobotControlService',)

    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)


LOGGING_CONFIG = {
    'level': logging.INFO,
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'datefmt': '%d-%b-%y %H:%M:%S',
    'filename': 'log/log.log',
    'filemode': 'w'
}


if __name__ == "__main__":
    # configure logging
    logging.basicConfig(**LOGGING_CONFIG)

    # Create our XML-RPC server.using out custom request handler that is also able to serve web pages over GET.
    port = 8090
    server = SimpleXMLRPCServer(("", port), RequestHandler, allow_none=True)

    # Register standard XML-RPC methods.
    server.register_introspection_functions()

    # Register function for all robots.
    server.register_instance(Controller())

    # Start to server.
    server.serve_forever()

from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer
from robot.controller.controller import Controller
from http.server import SimpleHTTPRequestHandler
import logging
import socket


# We define a custom server request handler, capable of both handling GET and XML-RPC requests.
class RequestHandler(SimpleXMLRPCRequestHandler, SimpleHTTPRequestHandler):
    rpc_paths = ('/RobotControlService',)

    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)


LOGGING_CONFIG = {
    'level': logging.INFO,
    'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    'filename': 'log/log.log',
    'filemode': 'w'
}


if __name__ == "__main__":
    # configure logging
    logging.basicConfig(**LOGGING_CONFIG)

    # Create our XML-RPC server.using out custom request handler that is also able to serve web pages over GET.
    port = 8090
    blockly_server = SimpleXMLRPCServer(
        ("", port), RequestHandler, allow_none=True)

    # Register standard XML-RPC methods.
    blockly_server.register_introspection_functions()

    # Network configuration.
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        host = s.getsockname()[0]
        s.close()
    except Exception as e:
        raise e
    port = 4005
    print(f"The client is running on {host}:{port}")
    server_host = input("Enter the server host:\n:>")
    server = (server_host, 4000)

    # Register function for all robots.
    blockly_server.register_instance(
        Controller(host=host, port=port, server=server)
    )

    print(f"Client connected to {server[0]}:{server[1]}")

    # Start to server.
    blockly_server.serve_forever()

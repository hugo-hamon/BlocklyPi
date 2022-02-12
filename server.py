from http.server import SimpleHTTPRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer
from robot import francasterSpeech
from robot import robotController, francasterController, allbotsController


def register_robot_xmlrpc_methods(server: SimpleXMLRPCServer):
    server.register_function(robotController.set_motor_position, 'robotController.set_motor_position')
    server.register_function(robotController.shift_motor_position, 'robotController.shift_motor_position')

    server.register_function(francasterController.walk_n_steps, 'FrancasterController.walk_n_steps')
    server.register_function(francasterController.do_hi, 'FrancasterController.do_hi')
    server.register_function(francasterController.reset_position, 'FrancasterController.reset_position')
    server.register_function(francasterController.walk_n_steps_with_knee_lift,
                             'FrancasterController.walk_n_steps_with_knee_lift')
    server.register_function(francasterController.do_yes, 'FrancasterController.do_yes')
    server.register_function(francasterController.do_no, 'FrancasterController.do_no')
    server.register_function(francasterSpeech.speak, 'FrancasterController.speak')
    server.register_function(francasterSpeech.repeat, 'FrancasterController.repeat')
    server.register_function(francasterSpeech.answer, 'FrancasterController.answer_question')

    server.register_function(allbotsController.reset_position, 'AllbotsController.reset_position')


# We define a custom server request handler, capable of both handling GET and XML-RPC requests.
class RequestHandler(SimpleXMLRPCRequestHandler, SimpleHTTPRequestHandler):
    rpc_paths = ('/RobotControlService',)

    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    # Create our XML-RPC server.using out custom request handler that is also able to serve web pages over GET.
    port = 8080
    server = SimpleXMLRPCServer(("", port), RequestHandler, allow_none=True)

    # Register standard XML-RPC methods.
    server.register_introspection_functions()

    register_robot_xmlrpc_methods(server)

    # Start to server.
    server.serve_forever()

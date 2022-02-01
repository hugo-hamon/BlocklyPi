from http.server import SimpleHTTPRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer
import robot.francasterController as FrancasterContoller
from robot import francasterSpeech


def register_francaster_xmlrpc_methods(server: SimpleXMLRPCServer):
    # Register the motor power command function.
    FrancasterContoller.init()
    server.register_function(FrancasterContoller.set, 'setRobotMotorPower')
    server.register_function(FrancasterContoller.set2, 'setRobotMotorPower2')
    server.register_function(FrancasterContoller.delay, 'setDelay')
    server.register_function(FrancasterContoller.marche, 'doWalk')
    server.register_function(FrancasterContoller.do_hi, 'doHi')
    server.register_function(FrancasterContoller.init, 'do_init')
    server.register_function(FrancasterContoller.marche_gn_cd, 'doWalk_gn_cd')
    server.register_function(FrancasterContoller.motor_dc, 'motor_dc')
    server.register_function(FrancasterContoller.say_yes, 'do_yes')
    server.register_function(FrancasterContoller.say_no, 'do_no')
    server.register_function(francasterSpeech.francaster_speak, 'speak')
    server.register_function(francasterSpeech.francaster_repeat, 'repeat')
    server.register_function(francasterSpeech.answer, 'quest')


# We define a custom server request handler, capable of both handling GET and XML-RPC requests.
class RequestHandler(SimpleXMLRPCRequestHandler, SimpleHTTPRequestHandler):
    rpc_paths = ('/RobotControlService',)

    def do_GET(self):
        SimpleHTTPRequestHandler.do_GET(self)


if __name__ == "__main__":
    # Create our XML-RPC server.using out custom request handler that is also able to serve web pages over GET.
    port = 8080
    server = SimpleXMLRPCServer(("", port), RequestHandler)

    # Register standard XML-RPC methods.
    server.register_introspection_functions()

    # Register the Francaster XML-RPC methods
    register_francaster_xmlrpc_methods(server)

    # Register the Francaster XML-RPC methods
    register_francaster_xmlrpc_methods(server)

    # Start to server.
    server.serve_forever()

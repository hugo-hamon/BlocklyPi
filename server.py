from http.server import SimpleHTTPRequestHandler
from xmlrpc.server import SimpleXMLRPCRequestHandler, SimpleXMLRPCServer
import robot.francasterController as FrancasterContoller
from robot import francasterSpeech


def register_francaster_xmlrpc_methods(server: SimpleXMLRPCServer):
    # Register the motor power command function.
    FrancasterContoller.init()
    server.register_function(FrancasterContoller.set_motor_power, 'FrancasterController.setMotorPower')
    server.register_function(FrancasterContoller.shift_motor_position, 'FrancasterController.shiftMotorPosition')
    server.register_function(FrancasterContoller.delay, 'FrancasterController.setDelay')
    server.register_function(FrancasterContoller.walk_n_steps, 'FrancasterController.walk')
    server.register_function(FrancasterContoller.do_hi, 'FrancasterController.doHi')
    server.register_function(FrancasterContoller.init, 'FrancasterController.init')
    server.register_function(FrancasterContoller.walk_n_steps_with_knee_lift, 'FrancasterController.walkNStepsWithKneeLift')
    server.register_function(FrancasterContoller.motor_dc, 'motor_dc')
    server.register_function(FrancasterContoller.do_yes, 'FrancasterController.doYes')
    server.register_function(FrancasterContoller.do_no, 'FrancasterController.doNo')
    server.register_function(francasterSpeech.speak, 'FrancasterController.speak')
    server.register_function(francasterSpeech.repeat, 'FrancasterController.repeat')
    server.register_function(francasterSpeech.answer, 'FrancasterController.answerQuestion')


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

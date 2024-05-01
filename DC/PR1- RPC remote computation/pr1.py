from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler


class FactorialServer:
    def calculate_factorial(self, n):
        if n < 0:
            raise ValueError("Input must be a non-negative integer.")
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


# Create an XML-RPC server
with SimpleXMLRPCServer(('localhost', 8000), requestHandler=RequestHandler) as server:
    server.register_introspection_functions()

    # Register the FactorialServer class
    factorial_server = FactorialServer()
    server.register_instance(factorial_server)

    print("FactorialServer is ready to accept requests.")

    # Register a range of factorial calculation method
    for i in range(1, 101):
        server.register_function(factorial_server.calculate_factorial, f'factorial_{i}')

    server.serve_forever()



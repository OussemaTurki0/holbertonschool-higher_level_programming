#!/usr/bin/python3
"""
   function file for http.server
"""


import json
from http.server import BaseHTTPRequestHandler, HTTPServer


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self._send_response(200, 'text/plain',
                                b"Bonjour, ceci est une API simple!")
        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_response(200, 'application/json',
                                json.dumps(data).encode())
        elif self.path == '/status':
            status = {"status": "OK"}
            self._send_response(200, 'application/json',
                                json.dumps(status).encode())
        else:
            error_message = {"error": "Endpoint not found"}
            self._send_response(404, 'application/json',
                                json.dumps(error_message).encode())

    def _send_response(self, code, content_type, content):
        self.send_response(code)
        self.send_header('Content-type', content_type)
        self.end_headers()
        self.wfile.write(content)


def run(server_class=HTTPServer,
        handler_class=SimpleHTTPRequestHandler,
        port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Démarrage du serveur HTTP sur le port {port}')
    httpd.serve_forever()


if __name__ == "__main__":
    run()

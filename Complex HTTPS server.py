import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import ssl
import socket
import subprocess

class ServerHTTPS(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/h':
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Commands:\n\n".encode())
            self.wfile.write("/ipconfig: returns ip\n".encode())
            self.wfile.write("/library: returns content from library\n".encode())
            self.wfile.write("upload file: do it with the html page\n".encode())
            return
        if self.path == '/ipconfig':
            ip = subprocess.run(args=["ipconfig"], capture_output=True, text=True)
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("ip data:\n".encode())
            self.wfile.write(f"{ip.stdout}\n".encode())
            return
        if self.path == '/library':
            return SimpleHTTPRequestHandler.do_GET(self)

        else:
            self.send_response(200)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write("Invalid path".encode())
            return

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        upload_dir = f'{os.getcwd()}\\test'
        if not os.path.exists(upload_dir):
            os.makedirs(upload_dir)
        with open(os.path.join(upload_dir, 'uploaded_file'), 'wb') as f:
            f.write(data)
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        self.wfile.write('File uploaded successfully'.encode())

class httpsipv6(HTTPServer):
    address_family = socket.AF_INET6

if __name__ == "__main__":
    Port = 8000
    server_address = ('::', Port)
    certfile = "server2.crt"
    key = "server2.key"
    httpd = httpsipv6(server_address, ServerHTTPS)
    ctx = ssl.SSLContext(protocol=ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(certfile=certfile, keyfile=key)
    httpd.socket = ctx.wrap_socket(httpd.socket, server_side=True)
    httpd.serve_forever()

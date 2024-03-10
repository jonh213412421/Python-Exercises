from http.server import SimpleHTTPRequestHandler, HTTPServer
import os
import sys
import socket
from datetime import datetime

port = 8000 #port. Change as you will

class server(SimpleHTTPRequestHandler): #handles GET requests
    def do_GET(self):
        if self.path == '/ip':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(f"GET request for {self.path}".encode("utf-8"))
            return
        else:
            return SimpleHTTPRequestHandler.do_GET(self)

def log_login(): #simple login registration
    now = datetime.now()
    if os.path.exists("log.txt"):
        with open("log.txt", "a") as f:
            f.write(f"{now.strftime("%m/%d/%Y, %H:%M:%S")}")
            f.write("-> ")
            f.write("HTTP server started\n")
    else:
        with open("log.txt", "a") as f:
            f.write(f"{now.strftime("%m/%d/%Y, %H:%M:%S")}")
            f.write("-> ")
            f.write("HTTP server started\n")

def log_logoff(): #simple logoff registration
    now = datetime.now()
    with open("log.txt", "a") as f:
        f.write(f"{now.strftime("%m/%d/%Y, %H:%M:%S")}")
        f.write("-> ")
        f.write("HTTP server shut down\n")

def login(): #crude login control with password implementation
    if os.path.exists("pw.txt"):
        with open("pw.txt", "r") as f:
            password = f.read()
            f.close()
            temp = input("Password: ")
            if temp != password:
                print("Error: incorrect password")
                sys.exit()
    else:
        with open("pw.txt", "w") as f:
            password = input("Create an password: ")
            f.write(password)
            f.close()
        print("[STARTING SERVER]")

class httpv6(HTTPServer): #this server uses ipv6. change it if you like
    address_family = socket.AF_INET6

def run(handler=server, port=port): #runs server
    server_address = ('::', port)
    httpd = httpv6(server_address, handler)
    try:
        print("[SERVER STARTED]")
        httpd.serve_forever()
    except Exception as e:
        print(f"Error: {e}")
    finally:
        log_logoff()

if __name__ == '__main__': #main
    login()
    log_login()
    run()



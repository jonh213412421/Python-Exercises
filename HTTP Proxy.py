import os
from http.server import SimpleHTTPRequestHandler, HTTPServer
import socket
from pyhtml2pdf import converter
import urllib.parse
import webbrowser

class ProxyHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        if self.path == "/test/":
            return SimpleHTTPRequestHandler.do_GET(self)
        if self.path == "/ip":
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(b"requisicao recebida")  # Modify this line based on your response
        else:
            try:
                parsed_url = urllib.parse.urlparse(self.path)
                query_params = urllib.parse.parse_qs(parsed_url.query)
                url = query_params['url'][0]
                url = "https://" + url
                print(f"URL recebida: {url}")
                converter.convert(url, "downloaded_site.pdf")
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"requisicao servida")  # Modify this line based on your response
            except KeyError:
                # Handle the case where 'url' is not present in query_params
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(b"Bad request - 'url' parameter missing")

class HTTPv6Server(HTTPServer):
    address_family = socket.AF_INET6

def get_ip():
    hostname = socket.gethostname()
    ip_host = socket.getaddrinfo(hostname, None, socket.AF_INET6)[4][4][0]
    return ip_host

def open_browser(path):
    webbrowser.open(path)

if __name__ == "__main__":
    PORT = 8000
    server_address = ('::', PORT)
    server = HTTPv6Server(server_address, ProxyHandler)
    print(f"[SERVER RUNNING - PORT 8000]")
    print(f"link for browser: {os.getcwd()}\\server_html.html")
    open_browser(f"{os.getcwd()}\\server_html.html")
    print(f"link for repo: http://[{get_ip()}]:{PORT}/test")
    print(f"link for log: http://[{get_ip()}]:{PORT}/ip")
    server.serve_forever()

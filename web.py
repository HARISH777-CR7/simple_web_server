from django.shortcuts import render
from http.server import HTTPServer, BaseHTTPRequestHandler

content = '''<html>
<body>
    <h1>List of Protocols in TCP/IP Protocol Suite</h1>
    
        <h1>Application Layer:</b> HTTP, FTP, SMTP, DNS, Telnet</h1>
        <h1><b>Transport Layer:</b> TCP, UDP</h1>
        <h1><b>Internet Layer:</b> IP, ICMP, ARP</h1>
        <h1><b>Network Access Layer:</b> Ethernet, Wi-Fi</h1>
    
    
     
</body>
 
</html>'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200)
        self.send_header("content-type", "text/html")
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver")
server_address = ('',8000)
httpd = HTTPServer(server_address, MyServer)
httpd.serve_forever()
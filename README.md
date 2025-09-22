# EX01 Developing a Simple Webserver

# Date:19/09/2025
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:

````
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

````
# OUTPUT:
![alt text](<Screenshot 2025-09-19 115010.png>)
![alt text](<Screenshot 2025-09-19 115032.png>)
<img width="1684" height="911" alt="Screenshot 2025-09-22 102602" src="https://github.com/user-attachments/assets/01373ae9-41f6-4589-9dbd-892ac3a88b66" />

# RESULT:
The program for implementing simple webserver is executed successfully.

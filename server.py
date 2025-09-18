#!/usr/bin/env python3
"""
Simple HTTP server to serve the Legal Boolean Search Builder HTML application.
Serves on 0.0.0.0:5000 to work with Replit's environment.
"""

import http.server
import socketserver
import os
from http.server import SimpleHTTPRequestHandler

class CustomHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add cache control headers to prevent caching issues in Replit's iframe
        self.send_header('Cache-Control', 'no-cache, no-store, must-revalidate')
        self.send_header('Pragma', 'no-cache')
        self.send_header('Expires', '0')
        super().end_headers()

    def do_GET(self):
        # Serve index.html for root path
        if self.path == '/':
            self.path = '/index.html'
        return super().do_GET()

if __name__ == "__main__":
    PORT = 5000
    HOST = "0.0.0.0"
    
    # Change to the directory containing our files
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    with socketserver.TCPServer((HOST, PORT), CustomHandler) as httpd:
        print(f"Server running at http://{HOST}:{PORT}/")
        print("Serving Legal Boolean Search Builder...")
        httpd.serve_forever()
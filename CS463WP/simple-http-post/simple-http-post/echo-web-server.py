#!/usr/bin/python

# echo-web-server.py

# NOTE: python 3 users will have provide slightly different import.
from http.server import BaseHTTPRequestHandler, HTTPServer

import http.server
from urllib.parse import parse_qs    

PORT = 8080

#This class will handle any incoming request from the browser 
class SimpleHttpPostHandler(http.server.SimpleHTTPRequestHandler):
        
    def do_POST(self):
        # Get ready for response by setting up response header values
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Get the length of submitted data
        content_length = int(self.headers['Content-Length']) 
        
        # Get the data (it is a string!)
        post_data = self.rfile.read(int(content_length))

        # 'deserialize' data string into dict -- using parse_qs method
        data = parse_qs(post_data, keep_blank_values=1)

        out = '<div style="text-align: center; font-family: \'arial\';">'
        try:
            # Access the 'message' variable from data (name in form)
            f = data[b'message'][0].decode("utf-8")           
            out += '<p>'+ ''.join(f) +'</p>'
            out += '<a href="/echo.html">New Message?</a>'

        except:
            out += '<p>Cannot make sense of the submitted form.</p>'
            out += '<a href="/echo.html">Fix it!</a>'
        
        out += '</div>'

        self.wfile.write(bytes(out,"utf-8"))



if __name__ == '__main__':
    
    try:
        # Create a web server and define our handler to manage the
        # incoming request
        server = HTTPServer(('', PORT), SimpleHttpPostHandler)
        print('Started httpserver on port ' , PORT)
        
        #Wait forever for incoming http requests
        server.serve_forever()

    except KeyboardInterrupt:
        print('^C received, shutting down the web server')
        server.socket.close()
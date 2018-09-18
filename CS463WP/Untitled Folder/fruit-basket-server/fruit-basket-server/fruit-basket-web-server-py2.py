#!/usr/bin/python

# fruit-basket-web-server-py2.py

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer

import SimpleHTTPServer
from urlparse import parse_qs    

PORT_NUMBER = 8080

#This class will handle any incoming request from the browser 
class SimpleHttpPostHandler(HTTPServer.SimpleHTTPRequestHandler):
        
    def do_POST(self):
        fruit_basket = {'oranges': 'yummy', 'grapes': 'wine is fine', 'apples': 'too tart', 'peaches': 'just peachee!', 'plums': 'great but no prunes'}
        # Get ready for response by setting up response header values
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Get the length of submitted data
        content_length = int(self.headers['Content-Length']) 
        
        # Get the data (it is a string!)
        post_data = self.rfile.read(content_length)

        # 'deserialize' data string into dict -- using parse_qs method
        data = parse_qs(post_data, keep_blank_values=1)

        out = '<div style="text-align: center; font-family: \'arial\';">'
        try:
            # Access the 'message' variable from data (name in form)
            f = data['message']           
            out += '<p>'+ ''.join(f) +'</p>'
            out += '<a href="/fruity.html">New Message?</a>'

        except Exception as e:
            out += '<p>Cannot make sense of the submitted form.</p>'
            out += '<a href="/fruity.html">Fix it!</a>'
        
        out += '</div>'

        self.wfile.write(out)



if __name__ == '__main__':
    
    try:
        # Create a web server and define our handler to manage the
        # incoming request
        server = HTTPServer(('', PORT_NUMBER), SimpleHttpPostHandler)
        print ('Started httpserver on port ' , PORT_NUMBER)
        
        #Wait forever for incoming http requests
        server.serve_forever()

    except KeyboardInterrupt:
        print ('^C received, shutting down the web server')
        server.socket.close()
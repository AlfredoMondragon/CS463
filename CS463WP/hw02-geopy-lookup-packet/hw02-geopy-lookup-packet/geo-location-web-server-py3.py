#!/usr/bin/python

# geo-location-web-server-py3.py

from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

from geopy_handler import query_handler

PORT_NUMBER = 8080

#This class will handle any incoming request from the browser 
class SimpleHttpPostHandler(SimpleHTTPRequestHandler):
    
    # Overriding the post handler from HTTPServer
    def do_POST(self):
        # Get ready for response by setting up response header values
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Get the length of submitted data
        content_length = int(self.headers['Content-Length']) 
        
        # Get the data (it is a string!)
        post_data = self.rfile.read(content_length)
       
        # 'deserialize' data string into dict -- using parse_qs method
        data = parse_qs(post_data.decode(),keep_blank_values=1)
        
        out = '<div style="text-align: center; font-family: \'arial\';">'
        try:
            # Access the variable (by name) from form data.            
            f = data['query_addr'][0]
            
            # Prepare HTML output for response.            
            out += '<p>'+ 'LATITUDE?' +'</p>'
            out += '<p>'+ 'LONGITUDE?' +'</p>'
            out += '<a href="./geo-lookup.html">New Query?</a>'

        except Exception as e:
            # Prepare HTML output for error response.
            out += '<p>Cannot make sense of the submitted form.</p>'
            out += '<p>' + str(e) + '</p>'
            out += '<a href="/geo-lookup.html">Fix it!</a>'
        
        out += '</div>'

        # Send the response out through the socket (back to client)
        self.wfile.write(out.encode())



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
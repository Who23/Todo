# this simple server and website act as a todo list. The todos are read from the todos.txt
# and sent to the website. when a todo is added on the website, a post request
# is also sent to the server to add it to the todos.txt file.

import http.server, socketserver, json, os
from http import HTTPStatus
from collections import namedtuple

# TODO: use threading so that you can have a main reponse thread as well as a websocket thread for 
# sending 'live' updates
# https://stackoverflow.com/questions/268629/how-to-stop-basehttpserver-serve-forever-in-a-basehttprequesthandler-subclass
# import threading
# import queue

MIMETYPES = {"html" : "text/html",
             "txt"  : "text/plain",
             "js"   : "text/javascript",
             "png"  : "image/png",
             "css"  : "text/css",
             "ico"  : "image/x-icon",
             "map"  : "application/json"}

class Handler (http.server.BaseHTTPRequestHandler):
    def __init__(self, request, client_address, server):
        super().__init__(request, client_address, server)

    def do_GET(self):
        global todos

        # return index.html
        if self.path.endswith("/"):

            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", 'text/html; charset=utf-8')
            self.end_headers()

            with open('../dist/index.html', 'rb') as f:
                self.wfile.write(f.read())
            
            return

        # return the todos from the todos.txt
        elif self.path.endswith("todos"):

            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", "text/plain")
            self.end_headers()

            self.wfile.write(bytes(json.dumps(todos), "utf-8"))

            return

        # return 404 if the path doesn't exist
        if not os.path.exists("../dist/" + self.path) or self.path.split("/")[-1] in MIMETYPES.keys():

            self.wfile.write(self.return404())

        # return the file needed
        else:
            
            self.send_response(HTTPStatus.OK)
            self.send_header("Content-type", MIMETYPES[self.path.split(".")[-1]])
            self.end_headers()

            with open("../dist/" + self.path, 'rb') as f:
                self.wfile.write(f.read())


    def do_POST(self):
        global todos

        if self.path == "/todos/add":

            data = json.loads(self.getPostData())
            todos.append(data["todo"])

            with open("./todos.txt", "w") as f:
                json.dump(todos, f)

        elif self.path == "/todos/remove":

            data = json.loads(self.getPostData())
            del todos[int(data['todoIndex'])]

            with open("./todos.txt", "w") as f:
                json.dump(todos, f)

        elif self.path == "/todos/edit":
            
            data = json.loads(self.getPostData())
            todos[int(data['todoIndex'])] = data['todo']

            with open("./todos.txt", "w") as f:
                json.dump(todos, f)

        elif self.path == "/todos/tags/update":

            # for adding, editing, and removing tags
            data = json.loads(self.getPostData())
            todos[int(data['todoIndex'])]['tags'] = data['tags']
            
            with open("./todos.txt", "w") as f:
                json.dump(todos, f)

        else:
            self.return404()


    def return404(self):
        self.send_response(HTTPStatus.NOT_FOUND)
        self.send_header('Connection', 'close')
        self.send_header("Content-Type", self.error_content_type)
        self.end_headers()

        with open('./404.html', 'rb') as f:
            contents = f.read()

        return contents


    def getPostData(self):
        length = int(self.headers['Content-Length'])
        data = self.rfile.read(length)
        self.send_response(HTTPStatus.OK)
        self.end_headers()

        return data



with open("./todos.txt", "r") as f:
    try:
        todos = json.load(f)
    except json.decoder.JSONDecodeError:
        todos = []
        print("File Contents empty or invalid")

addr = ('', 8000)
httpd = http.server.HTTPServer(addr, Handler)

try:
    print("Running on http://localhost:8000")
    httpd.serve_forever()
except KeyboardInterrupt:
    httpd.server_close()


with open("./todos.txt", "w") as f:
    json.dump(todos, f)
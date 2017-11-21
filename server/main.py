# Coding : UTF-8

import mydb
from wsgiref.simple_server import make_server
import cgi

def app(environ, start_response):
    path = environ["PATH_INFO"]
    print(path)
    request_method = environ["REQUEST_METHOD"]
    if path == "/db":
        if request_method == "POST":
            return insert_data(environ, start_response)
        elif request_method == "GET":
            return index(environ, start_response)
        else:
            return bad_request(environ, start_response)
    elif path in ["", "/"]:
        if request_method == "GET":
            return index(environ, start_response)
        else:
            return bad_request(environ, start_response)
    else:
        return bad_request(environ, start_response)

def bad_request(environ, start_response):
    headers = [('Content-type', 'text/html; charset=utf-8')]
    with open("400.html", "r") as f:
        status = "200 OK"
        start_response(status, headers)
        return [f.read().encode("utf-8")]

def insert_data(environ, start_response):
    wsgi_input = environ["wsgi.input"]
    form = cgi.FieldStorage(fp=wsgi_input, environ=environ, keep_blank_values=True)
    data = {k: form[k].value for k in form}
    mydb.insert_data(data["data"])
    status = "302 Found"
    start_response(status, [("Location", "http://localhost:8000")])
    return []

def index(environ, start_response):
    ret = mydb.select_data()
    print(ret)
    headers = [('Content-type', 'text/html; charset=utf-8')]
    with open("index.html", "r") as f:
        status = "200 OK"
        start_response(status, headers)
        return [f.read().format(ret).encode("utf-8")]

if __name__ == "__main__":
    httpd = make_server("", 8000, app)
    print("Serving on port 8000....")
    mydb.initialize_db()
    httpd.serve_forever()

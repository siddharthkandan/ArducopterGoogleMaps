import tornado.ioloop
import tornado.web
from tornado.options import define, options
import os

class LatLngHandler(tornado.web.RequestHandler):
    def post(self):
        # get the POST body, this will be our JSON string
#         content = self.get_argument('body', "No data received")
        content = self.request.body
        print content       
        self.write(content)

class MainHandler(tornado.web.RequestHandler):
    def set_default_headers(self):
        self.add_header('Access-Control-Allow-Origin', self.request.headers.get('Origin', '*'))
    
    def get(self):
        self.render("PolyMarker.html")      

# define all the application settings and options
define("port", default=8888, help="run on the given port", type=int)
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            (r"/upload", LatLngHandler),
            (r"/", MainHandler),
        ]
        settings = dict(
            debug="True",
            template_path=os.path.join(os.path.dirname(__file__), "templates"),
            static_path=os.path.join(os.path.dirname(__file__), "static"),
        )
        tornado.web.Application.__init__(self, handlers, **settings) 
        
def main():
    Application().listen(options.port)
    print "Server started, let's do this: %d" % options.port

    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    main()     
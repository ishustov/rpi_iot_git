# make_server is used to create this simple python webserver
from wsgiref.simple_server import make_server
# import led control library
import ilja

# Function that is ran when a http request comes in
def light_app(env, start_response):

    # set some http headers that are sent to the browser
    status = '200 OK'
    headers = [('Content-type', 'text/html')]
    start_response(status, headers)

    # Checks what path is sent via GET
    if env["PATH_INFO"] == "/on":
        print("user asked for /on")
        ilja.cleanLed()
        ilja.redOn()
        return '<!DOCTYPE html>'\
                '<html>'\
                    '<head>'\
                        '<title>"Lights"</title>'\
                    '</head>'\
                    '<body>'\
                        '<a title="off" href="/off">Off</a>'\
                    '</body>'\
                '</html>'

    elif env["PATH_INFO"] == "/off":
        print("user asked for /off")
        ilja.cleanLed()
        return '<!DOCTYPE html>'\
                '<html>'\
                    '<head>'\
                        '<title>"Lights"</title>'\
                    '</head>'\
                    '<body>'\
                        '<a title="On" href="/on">On</a>'\
                    '</body>'\
                '</html>'
    else:
        print("user asked for something else")
        return '<!DOCTYPE html>'\
                '<html>'\
                    '<head>'\
                        '<title>"Lights"</title>'\
                    '</head>'\
                    '<body>'\
                        '<a title="On" href="/on">On</a>'\
                    '</body>'\
                '</html>'

# Create a small python server
httpd = make_server("", 8437, light_app)
print "Serving on port 8437..."
print "You can open this in the browser http://192.168.1.xxx:8437 where xxx is your rpi ip aadress"
print "Or if you run this server on your own computer then http://localhost:8437"
httpd.serve_forever()

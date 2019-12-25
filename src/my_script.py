from http.server import BaseHTTPRequestHandler, HTTPServer
import signal
import sys
import json


class HttpProcessor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.command == 'GET' and self.path[0:7] == '/?year=':
            try:
                year = int(self.path[7:])
            except:
                self._send_all(1, "BAD YEAR NUMBER")
                return

            if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
                self._send_all(200, "12/09/%d" % year)
            else:
                self._send_all(200, "13/09/%d" % year)
        else:
            self._send_all(2, "BAD REQUEST")

    def _send_all(self, errorCode, dataMessage):
        self.send_response(200)
        self.send_header('content-type', 'text/json')
        self.end_headers()
        self.wfile.write(json.dumps({"errorCode": errorCode, "dataMessage": dataMessage}).encode())


def signal_handler(sig, frame):
    print('Exiting server')
    sys.exit(0)


def main():
    print("Starting simple http server...")

    signal.signal(signal.SIGINT, signal_handler)
    print("SIGINT handler created")

    serv = HTTPServer(('', 8080), HttpProcessor)
    print("Port setted\nRunning server...")

    serv.serve_forever()


if __name__ == '__main__':
    main()


print("Starting simple http ser111.")
